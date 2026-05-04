# 📊 Campeonato Brasileiro Série A --- Dashboard Interativo

Aplicação desenvolvida com **Python + Streamlit** para acompanhamento do
Campeonato Brasileiro Série A, com foco em análise de times,
classificação, artilharia e próximos jogos.

🔗 **Acesse o projeto online:**\
👉 https://projeto-michael-brasileirao-serie-a.streamlit.app/

------------------------------------------------------------------------

## 🎯 Objetivo do Projeto

A ideia deste projeto é construir uma aplicação simples e interativa
para:

-   Acompanhar a **classificação do campeonato**
-   Visualizar **artilharia (gols, assistências, pênaltis)**
-   Analisar um time específico:
    -   Últimos jogos
    -   Próximos jogos
    -   Desempenho recente
-   Comparar o time com o **próximo adversário**
-   Explorar dados de forma visual e intuitiva

------------------------------------------------------------------------

## ⚙️ Tecnologias Utilizadas

-   Python
-   Streamlit
-   Pandas
-   Plotly
-   API externa de dados esportivos

------------------------------------------------------------------------

## 🌐 Fonte de Dados

Os dados são consumidos da API pública:

👉 https://api.football-data.org/v4/

------------------------------------------------------------------------

## 📡 Principais Endpoints Utilizados

### 📊 Classificação do Campeonato

GET /competitions/BSA/standings

### ⚽ Partidas

GET /competitions/BSA/matches

### 👤 Artilharia

GET /competitions/BSA/scorers

------------------------------------------------------------------------

## 🚀 Como rodar localmente

    clone o repositório do GitHub na sua máquina
    crie um ambiente virtual: python -m venv venv
    ative o ambiente virtual: venv\Scripts\activate
    instale as dependências: pip install -r requirements.txt
    execute o comando no python: streamlit run app.py

------------------------------------------------------------------------

## 👨‍💻 Autor

Projeto desenvolvido por **Michael Chaves**
