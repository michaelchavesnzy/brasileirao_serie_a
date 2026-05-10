import streamlit as st

from components.partidas_cards import render_card_partida

from components.time_analysis import (
    preparar_partidas_time,
    obter_ultimos_jogos,
    obter_proximos_jogos,
    montar_comparativo_time_adversario,
)


def render_bloco_metricas(metricas, titulo):
    st.markdown(f"### {titulo}")

    col_logo, col_nome = st.columns([0.25, 1], vertical_alignment="center")

    with col_logo:
        st.image(metricas["link_escudo"], width=48)

    with col_nome:
        st.markdown(f"#### {metricas['nome_time']}")
        st.caption(f"{metricas['posicao']}º colocado")

    c1, c2, c3 = st.columns(3)
    c1.metric("Posição", f"{metricas['posicao']}º")
    c2.metric("Rodadas", metricas["rodadas"])
    c3.metric("Vitórias", metricas["vitorias"])

    c4, c5, c6 = st.columns(3)
    c4.metric("Empates", metricas["empates"])
    c5.metric("Derrotas", metricas["derrotas"])
    c6.metric("Ataque", f"{metricas['ranking_ataque']}º")

    c7, c8, c9 = st.columns(3)
    c7.metric("Defesa", f"{metricas['ranking_defesa']}º")
    c8.metric("Vitórias casa", f"{metricas['aproveitamento_casa']}%")
    c9.metric("Vitórias fora", f"{metricas['aproveitamento_fora']}%")

    st.caption(
        f"GM: {metricas['gols_marcados']} | "
        f"GC: {metricas['gols_sofridos']}"
    )


def render_comparativo_time_adversario(df_classificacao, df_partidas, nome_time):
    comparativo = montar_comparativo_time_adversario(
        df_classificacao=df_classificacao,
        df_partidas=df_partidas,
        nome_time=nome_time,
    )

    if comparativo is None:
        st.info("Não foi possível montar a análise do próximo adversário.")
        return

    proximo_jogo = comparativo["proximo_jogo"]
    metricas_time = comparativo["metricas_time"]
    metricas_adversario = comparativo["metricas_adversario"]

    st.markdown("## 📊 Time x Próximo Adversário")

    st.caption(
        f"Próximo jogo: Rodada {int(proximo_jogo['rodada_partida'])} — "
        f"{proximo_jogo['nome_time_casa']} x {proximo_jogo['nome_time_fora']}"
    )

    col_time, col_adversario = st.columns(2, vertical_alignment="top")

    with col_time:
        render_bloco_metricas(
            metricas=metricas_time,
            titulo="Time selecionado",
        )

    with col_adversario:
        render_bloco_metricas(
            metricas=metricas_adversario,
            titulo="Próximo adversário",
        )


def render_lista_partidas(titulo, df_jogos, mensagem_vazia):
    st.markdown(titulo)

    if df_jogos.empty:
        st.info(mensagem_vazia)
        return

    for _, row in df_jogos.iterrows():
        render_card_partida(row)


def render_jogos_time(df_time):
    df_ultimos = obter_ultimos_jogos(df_time, qtd=3)
    df_proximos = obter_proximos_jogos(df_time, qtd=3)

    col_ultimos, col_proximos = st.columns(2, vertical_alignment="top")

    with col_ultimos:
        render_lista_partidas(
            titulo="### ✅ Últimos 3 jogos",
            df_jogos=df_ultimos,
            mensagem_vazia="Ainda não há jogos finalizados para esse time.",
        )

    with col_proximos:
        render_lista_partidas(
            titulo="### 📅 Próximos 3 jogos",
            df_jogos=df_proximos,
            mensagem_vazia="Não há próximos jogos encontrados para esse time.",
        )


def render_time(df_partidas, df_classificacao, nome_time):
    st.subheader(f"⚽ Análise do {nome_time}")

    render_comparativo_time_adversario(
        df_classificacao=df_classificacao,
        df_partidas=df_partidas,
        nome_time=nome_time,
    )

    st.divider()

    df_time = preparar_partidas_time(
        df_partidas=df_partidas,
        df_classificacao=df_classificacao,
        nome_time=nome_time,
    )

    if df_time.empty:
        st.warning("Nenhuma partida encontrada para esse time.")
        return

    render_jogos_time(df_time)