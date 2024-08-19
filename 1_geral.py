import pandas as pd
import streamlit as st

df = pd.read_csv("zomato.csv")

st.header("Visao geral")

#bara lateral 

list_pa =["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"]


st.sidebar.header('Filtros')
st.sidebar.markdown('## selecine um pais para ver as informações')
pais = st.sidebar.multiselect('quais paises deseja ver?', list_pa, default=list_pa)

linhas_selc = df['Country'].isin(pais)
df = df.loc[linhas_selc,:]


st.dataframe(df)


#layout

st.header('Visão Geral')


restaurants, countries, cities, ratings, cuisines = st.columns(5)

unicos = df['Restaurant ID'].unique()
restaurants.metric(
        "Restaurantes Cadastrados",
        len(unicos),
    )
          

unicos_paies = df['Country Code'].unique()
countries.metric(
        "Paises Cadastrados",
        len(unicos_paies),
)




unicos_cidade = df['City'].unique()
cities.metric(
        "Cidades Cadastradas",
        len(unicos_cidade),
)

total_Avaliçao=df.loc[:, "Votes"].sum()
ratings.metric(
        "Avaliações",
        total_Avaliçao,
)


culianria=df.loc[:, "Cuisines"].nunique()
cuisines.metric(
        "Culinarias Cadastradas",
        culianria,
)

