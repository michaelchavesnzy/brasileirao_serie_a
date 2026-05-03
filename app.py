import streamlit as st
from services.data_loader import load_data
from components.classificacao import render_classificacao
from components.artilharia import render_artilharia

if __name__ == "__main__":

    try:

        with st.spinner("Carregando campeonato...", show_time=True):
            
            dados = load_data()

    except Exception as e:

        st.error(str(e))
        st.stop()

    st.set_page_config(layout="wide")

    st.markdown("# Campeonato Brasileiro 2026")

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


    with tab_time:

        st.subheader("Análise do Time")

        time = st.selectbox(
            "Selecione um time",
            [
                "Palmeiras",
                "Flamengo",
                "São Paulo"
            ]
        )

        st.write(f"Análise do {time}")