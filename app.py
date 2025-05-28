import streamlit as st
import pandas as pd
import base64
import seaborn as sns
import numpy as np
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go

st.title('S&P 500 App')

st.markdown("""
Cette application récupère la liste des entreprises du **S&P 500** (issue de Wikipédia) et leur **cours de clôture** (cumul annuel) !
* **Bibliothèques Python :** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Source des données :** [Wikipédia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('Entrées Paramètres Utilisateur')

# Web scraping des données S&P 500 
#
@st.cache_data
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - Selection du secteur 
sorted_sector_unique = sorted( df['GICS Sector'].unique() )
selected_sector = st.sidebar.multiselect('Secteur', sorted_sector_unique, sorted_sector_unique)

# Filtrage des données
df_selected_sector = df[ (df['GICS Sector'].isin(selected_sector)) ]

st.header('Affichage des Entreprises dans le Secteur Selectionné')
st.write('Dimension des Données: ' + str(df_selected_sector.shape[0]) + ' lignes et ' + str(df_selected_sector.shape[1]) + ' colonnes.')
st.dataframe(df_selected_sector)

# Download S&P500 data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# https://pypi.org/project/yfinance/

data = yf.download(
        tickers = list(df_selected_sector[:10].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

# Plot Closing Price of Query Symbol
def price_plot(symbol):
    df_plot = pd.DataFrame(data[symbol].Close)
    df_plot['Date'] = df_plot.index

    fig = px.line(df_plot, x='Date', y='Close', title=symbol)
    fig.update_traces(line=dict(color='skyblue'))
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        xaxis_title='Date',
        yaxis_title='Prix de clôture',
        template='plotly_white'
    )

    st.plotly_chart(fig, use_container_width=True)

num_company = st.sidebar.slider("Nombre d'entreprise", 1, 5)

if st.button('Afficher Graphiques'):
    st.header('Prix de clôture des actions')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)