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

#layout

st.header('Visão Cidade')



#Cidade

#1. Qual o nome da cidade que possui mais restaurantes registrados?

st.markdown("## Quantidade de Restaurantes por Cidade")
couls = ['Restaurant ID','City']
group_cidade = df.loc[:,couls].groupby('City').count().sort_values(by='Restaurant ID', ascending=False).reset_index()
group_cidade = group_cidade.head(10)
group_cidade.columns = couls

fig = px.bar(group_cidade, x='Restaurant ID', y='City')
st.plotly_chart(fig, use_container_width=True)



#2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
cols1, cols2 = st.columns(2)
cols1.markdown("## Cidade com nota acima de 4")
df1 = df.copy()
linha  = df1['Aggregate rating'] > 4
df1 = df1.loc[linha,:]

couls_rating = ['City','Aggregate rating']
group_rating = df1.loc[:,couls_rating].groupby('City').mean().sort_values(by='Aggregate rating', ascending=False).reset_index()
group_rating.columns = couls_rating
group_rating =  group_rating.head(10)
fig = px.bar(group_rating, x='City', y='Aggregate rating')
cols1.plotly_chart(fig, use_container_width=True)


#3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?

cols2.markdown("## Cidade com nota abaixo de 2.5")
df2 = df.copy()
linha  = df2['Aggregate rating'] < 2.5
df2 = df2.loc[linha,:]
couls_rating = ['City','Aggregate rating']
group_rating = df2.loc[:,couls_rating].groupby('City').mean().sort_values(by='Aggregate rating', ascending=False).reset_index()
group_rating.columns = couls_rating
fig = px.bar(group_rating, x='City', y='Aggregate rating')
cols2.plotly_chart(fig, use_container_width=True)



#5. Qual o nome da cidade que possui restarente com a maior quantidade de tipos de culinária distintas?
st.markdown('## Quantidade de tipos de culinaria por Cidade')
couls_culinaria = ['City','Cuisines','Country']
group_culinaria = (
        df.loc[:, couls_culinaria]
        .groupby(["Country", "City"])
        .nunique()
        .sort_values(["Cuisines", "City"], ascending=[False, True])
        .reset_index()
    )
group_culinaria.columns = couls_culinaria
group_culinaria =  group_culinaria.head(10)
fig = px.bar(group_culinaria, x='City', y='Cuisines')
st.plotly_chart(fig, use_container_width=True)


