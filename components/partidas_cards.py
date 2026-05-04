import streamlit as st


def render_card_partida(row):
    col_time, col_placar, col_adv = st.columns(
        [2.2, 1, 2.2],
        vertical_alignment="center",
    )

    with col_time:
        c1, c2 = st.columns([0.45, 2], vertical_alignment="center")
        c1.image(row["escudo_time"], width=34)
        c2.markdown(f"**{row['nome_time']}**")

    with col_placar:
        st.markdown(
            f"""
            <div style='text-align:center; font-size:22px; font-weight:700;'>
                {row['gols_time_exibicao']} x {row['gols_adversario_exibicao']}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_adv:
        c1, c2 = st.columns([0.45, 2], vertical_alignment="center")
        c1.image(row["escudo_adversario"], width=34)
        c2.markdown(f"**{row['nome_adversario']}**")

    st.caption(
        f"Rodada {int(row['rodada_partida'])} | "
        f"{row['mando']} | "
        f"{row['resultado_time']}"
    )

    st.markdown(
        "<hr style='margin: 6px 0px 10px 0px;'>",
        unsafe_allow_html=True,
    )