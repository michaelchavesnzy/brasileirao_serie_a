import pandas as pd

def transform_bsa(raw_json):

    df = pd.json_normalize(raw_json)

    df = df[['area.id', 'currentSeason.id', 'currentSeason.startDate', 'currentSeason.endDate', 'currentSeason.currentMatchday', 'currentSeason.winner']]

    df.rename(columns={
        'area.id':'id_campeonato',
        'currentSeason.id':'id_temporada_atual',
        'currentSeason.startDate':'dt_inicio_temporada_atual',
        'currentSeason.endDate':'dt_fim_temporada_atual',
        'currentSeason.currentMatchday':'rodada_atual',
        'currentSeason.winner':'time_campeao'
        }, inplace=True)
    
    return df

def transform_standings(raw_json):

    df = pd.json_normalize(raw_json['standings'][0]['table'])

    # Faixa de classificação
    def get_faixa(posicao):
        if posicao <= 4:
            return "🟦"
        elif posicao <= 6:
            return "🟧"
        elif posicao >= 17:
            return "🟥"
        else:
            return "🟩"

    df["faixa"] = df["position"].apply(get_faixa)

    df = df[['team.id', 'position', 'faixa', 'team.shortName', 'points', 'playedGames', 'won', 'draw', 'lost', 'goalsFor', 'goalsAgainst', 'goalDifference', 'team.crest']]

    df.rename(columns={
        'team.id':'id_time',
        'position':'posicao',
        'team.shortName':'nome_time',
        'points':'pontos',
        'playedGames':'PJ',
        'won':'VIT',
        'draw':'E',
        'lost':'DER',
        'goalsFor':'GM',
        'goalsAgainst':'GC',
        'goalDifference':'SG',
        'team.crest':'link_escudo'
        }, inplace=True)
    
    return df

def transform_mactches(raw_json):

    df = pd.json_normalize(raw_json['matches'])

    df = df[['id', 'status', 'matchday','homeTeam.id', 'homeTeam.shortName', 'awayTeam.id', 'awayTeam.shortName', 'score.winner', 'score.fullTime.home', 'score.fullTime.away']]

    df.rename(columns={
        'id':'id_partida',
        'status':'status_partida',
        'matchday':'rodada_partida',
        'homeTeam.id':'id_time_casa',
        'homeTeam.shortName':'nome_time_casa',
        'awayTeam.id':'id_time_fora',
        'awayTeam.shortName':'nome_time_fora',
        'score.winner':'resultado_partida',
        'score.fullTime.home':'gols_time_casa',
        'score.fullTime.away':'gols_time_fora'
        }, inplace=True)
    
    return df

def transform_scorers(raw_json):

    df = pd.json_normalize(raw_json['scorers'])

    df = df[['player.id', 'player.name', 'team.id', 'team.shortName', 'playedMatches', 'goals', 'assists', 'penalties']]

    df.rename(columns={
        'player.id':'id_jogador',
        'player.name':'nome_jogador',
        'team.id':'id_time',
        'team.shortName':'nome_time',
        'playedMatches':'rodadas_jogadas',
        'goals':'gols',
        'assists':'assistencias',
        'penalties':'gols_penaltis'
        }, inplace=True)
    
    return df

