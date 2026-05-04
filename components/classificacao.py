import streamlit as st

def render_classificacao(df_classificacao):
    
    st.subheader("Tabela Brasileirão")
    
    colunas_tabela = ['posicao', 'faixa', 'link_escudo', 'nome_time', 'pontos', 'PJ', 'VIT', 'E', 'DER', 'GM', 'GC', 'SG']

    st.dataframe(
        df_classificacao[colunas_tabela],
        hide_index=True,
        width='stretch',
        column_config={
            "posicao": st.column_config.NumberColumn(
                "#",
                width="small",
            ),
            "faixa": st.column_config.TextColumn(
                "",
                width="small",
            ),
            "link_escudo": st.column_config.ImageColumn(
                "Escudo",
                width="small",
            ),
            "nome_time": st.column_config.TextColumn(
                "Clube",
                width="medium",
            ),
            "pontos": st.column_config.NumberColumn(
                "Pts",
                width="small",
            ),
            "PJ": st.column_config.NumberColumn(
                "PJ",
                width="small",
            ),
            "VIT": st.column_config.NumberColumn(
                "VIT",
                width="small",
            ),
            "E": st.column_config.NumberColumn(
                "E",
                width="small",
            ),
            "DER": st.column_config.NumberColumn(
                "DER",
                width="small",
            ),
            "GM": st.column_config.NumberColumn(
                "GM",
                width="small",
            ),
            "GC": st.column_config.NumberColumn(
                "GC",
                width="small",
            ),
            "SG": st.column_config.NumberColumn(
                "SG",
                width="small",
            ),
        },
    )

    st.caption("🟦 G4 | 🟧 Pré-Libertadores | 🟩 Meio da tabela | 🟥 Rebaixamento")