import streamlit as st
import pandas as pd
import plotly.express as px

def render_artilharia(df_artilharia, df_classificacao):

    st.subheader("⚽ Artilharia")

    df = df_artilharia.merge(df_classificacao[["id_time", "link_escudo"]],on="id_time",how="left")

    # Ordena por gols e cria ranking
    df = df.sort_values("gols", ascending=False).reset_index(drop=True)

    df["ranking"] = df.index + 1
    df["assistencias"] = df["assistencias"].fillna(0).astype(int)
    df["gols_penaltis"] = df["gols_penaltis"].fillna(0).astype(int)

    colunas_tabela = [
        "ranking",
        "link_escudo",
        "nome_jogador",
        "gols",
        "assistencias",
        "gols_penaltis"
    ]

    col_tabela, col_grafico = st.columns(
        [1.25, 1],
        vertical_alignment="top"
    )

    # Tabela artilharia
    with col_tabela:

        st.markdown("### 🏆 Top 15")

        st.dataframe(
            df[colunas_tabela],
            hide_index=True,
            width='stretch',
            column_config={
                "ranking": st.column_config.NumberColumn(
                    "#",
                    width="small",
                ),
                "link_escudo": st.column_config.ImageColumn(
                    "Escudo",
                    width="small",
                ),
                "nome_jogador": st.column_config.TextColumn(
                    "Jogador",
                    width="medium",
                ),
                "gols": st.column_config.NumberColumn(
                    "Gols",
                    width="small",
                ),
                "assistencias": st.column_config.NumberColumn(
                    "Assist.",
                    width="small",
                ),
                "gols_penaltis": st.column_config.NumberColumn(
                    "Pênaltis",
                    width="small",
                ),
            },
        )

    # Gráfico artilharia
    with col_grafico:

        st.markdown("### 📊 Gols por Jogador")

        df_graph = df.sort_values("gols", ascending=True).copy()

        fig = px.bar(
            df_graph,
            x="gols",
            y="nome_jogador",
            orientation="h",
            text="gols",
            height=420,
        )

        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Gols",
            yaxis_title="",
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20),
        )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )