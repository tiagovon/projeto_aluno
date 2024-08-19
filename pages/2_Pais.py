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

st.header('Visão pais')


#Pais



#Qual o nome do país que possui mais restaurantes registrados?


st.markdown('## Quantidade de Restaurantes por pais ')
couls_id = ['Country','Restaurant ID']
group_restaurante = df.loc[:,couls_id].groupby('Country').count().sort_values(by='Restaurant ID', ascending=False).reset_index()
group_restaurante.columns = couls_id
fig = px.bar(group_restaurante, x='Country', y='Restaurant ID')
st.plotly_chart(fig, use_container_width=True)


#cidade por pais 

st.markdown('## Quantidade de cidade por pais')
couls_city = ['Country','City']
group_city = df.loc[:,couls_city].groupby('Country').nunique().sort_values(by='City', ascending=False).reset_index()
group_city.columns = couls_city
fig = px.bar(group_city, x='Country', y='City')
st.plotly_chart(fig, use_container_width=True)





couls1 , couls2 = st.columns(2)
#9. Qual o nome do país que possui, na média, a maior nota média registrada?

coulss_votos_maior = ['Country','Aggregate rating']
group_votos_maior = df.loc[:,coulss_votos_maior].groupby('Country').mean().sort_values(by='Aggregate rating', ascending=False).reset_index()
group_votos_maior.columns = coulss_votos_maior
fig = px.bar(group_votos_maior, x='Country', y='Aggregate rating')
couls1.markdown('##  Media de notas por pais')
couls1.plotly_chart(fig, use_container_width=True)


#11. Qual a média de preço de um prato para dois por país?

couls_perco = ['Country','Average Cost for two']
group_perco = df.loc[:,couls_perco].groupby('Country').mean().sort_values(by='Average Cost for two', ascending=False).reset_index()
group_perco.columns = couls_perco
fig = px.bar(group_perco, x='Country', y='Average Cost for two')
couls2.markdown('## Media de preco por pais')
couls2.plotly_chart(fig, use_container_width=True)

