import streamlit as st
from services.data_loader import load_data
from components.classificacao import render_classificacao
from components.artilharia import render_artilharia
from components.time import render_time


if __name__ == "__main__":

    try:

        with st.spinner("Carregando campeonato...", show_time=True):
            
            dados = load_data()

    except Exception as e:

        st.error(str(e))
        st.stop()

    st.set_page_config(layout="wide")

    st.markdown("# Campeonato Brasileiro 202: BSA")

    tab_geral, tab_time = st.tabs([

        "📊 Geral",
        "⚽ Time"
    ])

    with tab_geral:

        info = dados["brasileirao"].iloc[0]

        col1, col2, col3 = st.columns(3)
        col1.metric("📅 Início", info["dt_inicio_temporada_atual"])
        col2.metric("🏁 Final", info["dt_fim_temporada_atual"])
        col3.metric("⚽ Rodada Atual", int(info["rodada_atual"]))

        st.divider()

        render_classificacao(dados["classificacao"])

        st.divider()

        render_artilharia(dados["artilheiros"],dados["classificacao"])

        st.caption("Desenvolvimento por Michael Chaves")

    with tab_time:

        lista_times = (
            dados["classificacao"]["nome_time"]
            .sort_values()
            .unique()
            .tolist()
        )

        time = st.selectbox(
            "Selecione um time",
            lista_times
        )

        render_time(
            dados["partidas"],
            dados["classificacao"],
            time
        )