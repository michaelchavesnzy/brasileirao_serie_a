import pandas as pd


def obter_id_time(df_classificacao, nome_time):
    row = df_classificacao.loc[df_classificacao["nome_time"] == nome_time]

    if row.empty:
        return None

    return row.iloc[0]["id_time"]


def adicionar_escudos_partidas(df_partidas, df_classificacao):
    df = df_partidas.copy()

    df_escudos = (
        df_classificacao[["id_time", "link_escudo"]]
        .drop_duplicates("id_time")
        .copy()
    )

    df = df.merge(
        df_escudos.rename(
            columns={
                "id_time": "id_time_casa",
                "link_escudo": "escudo_time_casa",
            }
        ),
        on="id_time_casa",
        how="left",
    )

    df = df.merge(
        df_escudos.rename(
            columns={
                "id_time": "id_time_fora",
                "link_escudo": "escudo_time_fora",
            }
        ),
        on="id_time_fora",
        how="left",
    )

    return df


def preparar_partidas_time(df_partidas, df_classificacao, nome_time):
    df = adicionar_escudos_partidas(df_partidas, df_classificacao)

    df_time = df.loc[
        (df["nome_time_casa"] == nome_time)
        | (df["nome_time_fora"] == nome_time)
    ].copy()

    if df_time.empty:
        return df_time

    df_time["time_eh_casa"] = df_time["nome_time_casa"] == nome_time

    df_time["nome_time"] = df_time.apply(
        lambda row: row["nome_time_casa"]
        if row["time_eh_casa"]
        else row["nome_time_fora"],
        axis=1,
    )

    df_time["nome_adversario"] = df_time.apply(
        lambda row: row["nome_time_fora"]
        if row["time_eh_casa"]
        else row["nome_time_casa"],
        axis=1,
    )

    df_time["escudo_time"] = df_time.apply(
        lambda row: row["escudo_time_casa"]
        if row["time_eh_casa"]
        else row["escudo_time_fora"],
        axis=1,
    )

    df_time["escudo_adversario"] = df_time.apply(
        lambda row: row["escudo_time_fora"]
        if row["time_eh_casa"]
        else row["escudo_time_casa"],
        axis=1,
    )

    df_time["mando"] = df_time["time_eh_casa"].map(
        {
            True: "Casa",
            False: "Fora",
        }
    )

    df_time["gols_time"] = df_time.apply(
        lambda row: row["gols_time_casa"]
        if row["time_eh_casa"]
        else row["gols_time_fora"],
        axis=1,
    )

    df_time["gols_adversario"] = df_time.apply(
        lambda row: row["gols_time_fora"]
        if row["time_eh_casa"]
        else row["gols_time_casa"],
        axis=1,
    )

    df_time["gols_time_exibicao"] = df_time.apply(
        lambda row: int(row["gols_time"])
        if row["status_partida"] == "FINISHED" and pd.notnull(row["gols_time"])
        else 0,
        axis=1,
    )

    df_time["gols_adversario_exibicao"] = df_time.apply(
        lambda row: int(row["gols_adversario"])
        if row["status_partida"] == "FINISHED"
        and pd.notnull(row["gols_adversario"])
        else 0,
        axis=1,
    )

    df_time["resultado_time"] = df_time.apply(calcular_resultado_time, axis=1)

    return df_time


def calcular_resultado_time(row):
    if row["status_partida"] != "FINISHED":
        return "⚪ A jogar"

    if row["gols_time"] > row["gols_adversario"]:
        return "🟢 Vitória"

    if row["gols_time"] < row["gols_adversario"]:
        return "🔴 Derrota"

    return "🟡 Empate"


def obter_ultimos_jogos(df_time, qtd=3):
    return (
        df_time.loc[df_time["status_partida"] == "FINISHED"]
        .sort_values("rodada_partida", ascending=False)
        .head(qtd)
        .sort_values("rodada_partida", ascending=True)
    )


def obter_proximos_jogos(df_time, qtd=3):
    return (
        df_time.loc[df_time["status_partida"] != "FINISHED"]
        .sort_values("rodada_partida", ascending=True)
        .head(qtd)
    )


def obter_proximo_jogo(df_partidas, id_time):
    df_proximos = df_partidas.loc[
        (
            (df_partidas["id_time_casa"] == id_time)
            | (df_partidas["id_time_fora"] == id_time)
        )
        & (df_partidas["status_partida"] != "FINISHED")
    ].copy()

    if df_proximos.empty:
        return None

    return (
        df_proximos
        .sort_values("rodada_partida", ascending=True)
        .iloc[0]
    )


def obter_id_adversario(proximo_jogo, id_time):
    if proximo_jogo["id_time_casa"] == id_time:
        return proximo_jogo["id_time_fora"]

    return proximo_jogo["id_time_casa"]


def calcular_aproveitamento_vitorias_mando(df_partidas, id_time, mando):
    if mando == "casa":
        df_jogos = df_partidas.loc[
            (df_partidas["id_time_casa"] == id_time)
            & (df_partidas["status_partida"] == "FINISHED")
        ].copy()

        if df_jogos.empty:
            return 0

        vitorias = (df_jogos["resultado_partida"] == "HOME_TEAM").sum()

    else:
        df_jogos = df_partidas.loc[
            (df_partidas["id_time_fora"] == id_time)
            & (df_partidas["status_partida"] == "FINISHED")
        ].copy()

        if df_jogos.empty:
            return 0

        vitorias = (df_jogos["resultado_partida"] == "AWAY_TEAM").sum()

    return round((vitorias / len(df_jogos)) * 100, 1)


def adicionar_rankings_ataque_defesa(df_classificacao):
    df = df_classificacao.copy()

    df["ranking_ataque"] = (
        df["GM"]
        .rank(method="min", ascending=False)
        .astype(int)
    )

    df["ranking_defesa"] = (
        df["GC"]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    return df


def calcular_metricas_time(df_classificacao, df_partidas, id_time):
    df_rank = adicionar_rankings_ataque_defesa(df_classificacao)

    row = df_rank.loc[df_rank["id_time"] == id_time]

    if row.empty:
        return None

    row = row.iloc[0]

    return {
        "id_time": row["id_time"],
        "nome_time": row["nome_time"],
        "link_escudo": row["link_escudo"],
        "posicao": int(row["posicao"]),
        "rodadas": int(row["PJ"]),
        "vitorias": int(row["VIT"]),
        "empates": int(row["E"]),
        "derrotas": int(row["DER"]),
        "aproveitamento_casa": calcular_aproveitamento_vitorias_mando(
            df_partidas,
            id_time,
            "casa",
        ),
        "aproveitamento_fora": calcular_aproveitamento_vitorias_mando(
            df_partidas,
            id_time,
            "fora",
        ),
        "ranking_ataque": int(row["ranking_ataque"]),
        "ranking_defesa": int(row["ranking_defesa"]),
        "gols_marcados": int(row["GM"]),
        "gols_sofridos": int(row["GC"]),
    }


def montar_comparativo_time_adversario(df_classificacao, df_partidas, nome_time):
    id_time = obter_id_time(df_classificacao, nome_time)

    if id_time is None:
        return None

    proximo_jogo = obter_proximo_jogo(df_partidas, id_time)

    if proximo_jogo is None:
        return None

    id_adversario = obter_id_adversario(proximo_jogo, id_time)

    metricas_time = calcular_metricas_time(
        df_classificacao,
        df_partidas,
        id_time,
    )

    metricas_adversario = calcular_metricas_time(
        df_classificacao,
        df_partidas,
        id_adversario,
    )

    return {
        "proximo_jogo": proximo_jogo,
        "metricas_time": metricas_time,
        "metricas_adversario": metricas_adversario,
    }