import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("C:\\Users\\Tiago\\OneDrive\\Documentos\\repos\\ftc_progama\\dataset\\desafio_do_aluno\\zomato.csv")


#bara lateral 


list_pa =["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"]


st.sidebar.header('Filtros')
st.sidebar.markdown('## selecine um pais para ver as informações')
pais = st.sidebar.multiselect('quais paises deseja ver?', list_pa, default=list_pa)

linhas_selc = df['Country'].isin(pais)
df = df.loc[linhas_selc,:]


list_c =[
            "Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
        ]

cuisines = st.sidebar.multiselect('quais tipos de cuilinario deseja ver?', list_c, default= list_c)
linhas_selc_cuisine = df['Cuisines'].isin(cuisines)
df = df.loc[linhas_selc,:]
#layout

st.header('Visão Restaurantes')

#Restaurantes
#1. Qual o nome do restaurante que possui a maior quantidade de avaliações?


st.markdown('## top 100 restaurantes com mais avaliações')
cols = [
    "Restaurant ID",
    "Restaurant Name",
    "Country",
    "City",
    "Cuisines",
    "Average Cost for two",
    "Aggregate rating",
    "Votes",]


dataframe = df.loc[:, cols].sort_values(["Aggregate rating", "Restaurant ID"], ascending=[False, True])
st.dataframe(dataframe.head(100))


cols1 , cols2 = st.columns(2)
#top 10 melhores tipos de cuilinario

couls1 = ['Cuisines','Aggregate rating']
group_cuisine = df.loc[:,couls1].groupby('Cuisines').count().sort_values(by='Aggregate rating', ascending=False).reset_index()
group_cuisine.columns = couls1
fig = px.bar(group_cuisine.head(10), x='Cuisines', y='Aggregate rating')
cols1.markdown('## Top 10 melhores tipos de cuilinario')
cols1.plotly_chart(fig, use_container_width=True)

#top 10 piores tipos de cuilinario

couls2 = ['Cuisines','Aggregate rating']
group_cuisine = df.loc[:,couls2].groupby('Cuisines').count().sort_values(by='Aggregate rating', ascending=True).reset_index()
group_cuisine.columns = couls2
fig = px.bar(group_cuisine.head(10), x='Cuisines', y='Aggregate rating')
cols2.markdown('## Top 10 piores tipos de cuilinario')
cols2.plotly_chart(fig, use_container_width=True)