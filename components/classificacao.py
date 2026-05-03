import streamlit as st

def render_classificacao(df_classificacao):

    st.subheader("Tabela")

    # Cabeçalho
    header = st.columns([0.45, 0.35, 0.7, 2.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])

    header[3].markdown("**Clube**")
    header[4].markdown("**Pts**")
    header[5].markdown("**PJ**")
    header[6].markdown("**VIT**")
    header[7].markdown("**E**")
    header[8].markdown("**DER**")
    header[9].markdown("**GM**")
    header[10].markdown("**GC**")
    header[11].markdown("**SG**")

    st.divider()

    # Linhas
    for _, row in df_classificacao.iterrows():

        # classificação
        if row["posicao"] <= 4:
            cor = "🟦"
        elif row["posicao"] <= 6:
            cor = "🟧"
        elif row["posicao"] >= 17:
            cor = "🟥"
        else:
            cor = "🟩"

        cols = st.columns([0.45, 0.35, 0.7, 2.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])

        # posição
        cols[0].write(f"**{row['posicao']}**")

        # faixa classificação
        cols[1].write(cor)

        # escudo
        cols[2].image(row["link_escudo"], width=35)

        # time
        cols[3].write(f"**{row['nome_time']}**")

        # stats
        cols[4].write(f"**{row['pontos']}**")
        cols[5].write(f"**{row['PJ']}**")
        cols[6].write(f"**{row['VIT']}**")
        cols[7].write(f"**{row['E']}**")
        cols[8].write(f"**{row['DER']}**")
        cols[9].write(f"**{row['GM']}**")
        cols[10].write(f"**{row['GC']}**")
        cols[11].write(f"**{row['SG']}**")

        st.markdown(
            "<hr style='margin:2px 0px;'>",
            unsafe_allow_html=True
        )