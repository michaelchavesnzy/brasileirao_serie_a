import streamlit as st
import pandas as pd
import plotly.express as px

def render_artilharia(df_artilharia,df_classificacao):

    st.subheader("⚽ Artilharia")

    df = df_artilharia.merge(df_classificacao[["id_time", "link_escudo","nome_time"]], on="id_time",how="left")

    df = df.sort_values("gols",ascending=False)

    col_tabela, col_grafico = st.columns([1.2, 1])

    #Tabela artilharia
    with col_tabela:

        header = st.columns([0.4,0.8,2.8,0.8,0.8,0.8])

        header[2].markdown("**Jogador**")
        header[3].markdown("**Gols**")
        header[4].markdown("**Assistências**")
        header[5].markdown("**Penaltis**")

        st.divider()

        for idx, row in df.head(10).iterrows():

            cols = st.columns([0.4,0.8,2.8,0.8,0.8,0.8])

            # ranking
            cols[0].write(f"**{idx + 1}**")

            # escudo
            cols[1].image(row["link_escudo"],width=28)

            # jogador
            cols[2].write(f"**{row['nome_jogador']}**")

            # gols
            cols[3].write(f"**{row['gols']}**")

            # assistências
            cols[4].write(f"**{int(row['assistencias']) if pd.notnull(row['assistencias']) else 0}**")

            # gols de pênalti
            cols[5].write(f"**{int(row['gols_penaltis']) if pd.notnull(row['gols_penaltis']) else 0}**")

            # divisor compacto
            st.markdown("<hr style='margin:2px 0px;'>",unsafe_allow_html=True)


    # Gráfico
    with col_grafico:

        st.markdown("### 📊 Gols por Jogador")

        df_graph = (df.head(10).sort_values("gols",ascending=True))

        df_graph["label"] = df_graph["nome_jogador"]

        fig = px.bar(

            df_graph,
            x="gols",
            y="label",
            orientation="h",
            text="gols",
            height=420
        )

        fig.update_layout(

            template="plotly_dark",

            xaxis_title="Gols",
            yaxis_title="",

            showlegend=False,

            margin=dict(l=20,r=20,t=40,b=20)
            
            )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )