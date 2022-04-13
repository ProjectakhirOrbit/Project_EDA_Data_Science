#import Libraries yang diperlukan
from tokenize import String
from matplotlib.pyplot import text
import streamlit as st
import pandas as pd
import numpy as np
from turtle import width
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns


# Membangun aplikasi dashboard
# image = Image.open("Health.jpeg")
#st.image(image, width=500)

# Import Dataset
@st.cache
def load_data():
    df = pd.read_csv("cd.csv")
    return df

df = load_data()

#VARIABEL

visualization = st.sidebar.selectbox('Select visualization',('Home_Navigation','Model_1', 'Model_2', 'Model_3', 'Model_4'))

if visualization =='Home_Navigation':
    st.header("Analisis Dashboard Penyebab Kematian Di Dunia ☠️")
    
elif visualization == 'Model_1':
    column_names = ["Entity","Code","Year","Causes name","Causes Full Description","Death Numbers"]
    selected_state = df.reindex(columns=column_names)
    state_select = st.sidebar.selectbox('Select a Country', df['Entity'].unique())
    selected_state = df[df['Entity'] == state_select]
    fig1 = px.bar(selected_state, x='Year', y='Death Numbers',
    hover_data=['Code', 'Causes Full Description'], color='Causes name',
    labels={'Death Numbers':'Total Death'}, height=400 , width=1200)
    st.title(f'Total Death by diseases & accidents in {state_select} From 1990 - 2019')
    st.plotly_chart(fig1)
elif visualization == 'Model_2':
    column_names = ["Entity","Code","Year","Causes name","Causes Full Description","Death Numbers"]
    selected_state = df.reindex(columns=column_names)
    state_select = st.sidebar.selectbox('Select a Country', df['Entity'].unique())
    selected_state = df[df['Entity'] == state_select]
    Cause_select = st.sidebar.selectbox('Pilih Penyebab' , selected_state['Causes name'].sort_values(ascending=True).unique())
    selected_cause = selected_state[selected_state['Causes name'] == Cause_select]
    st.title(f'Country : {state_select}')
    df1 = selected_cause.sort_values(by=['Year'])
    df2 = df1.replace(np.nan,0)
    df3=df2.pivot_table(index=['Causes name'],values=['Death Numbers'],aggfunc=sum).iloc[[0],[0]].values
    fig2 = px.bar(df2, x='Causes name', y='Death Numbers',
    hover_data=['Code', 'Death Numbers','Year'],color='Causes name',
    labels={'Death Numbers':'Total Death'}, height=400 , width=400)
    st.header(f"Total deaths Caused by {Cause_select} From 1990 - 2019 : {str(int(df3))}")
    st.plotly_chart(fig2)
elif visualization == 'Model_3':
    column_names = ["Entity","Code","Year","Causes name","Causes Full Description","Death Numbers"]
    selected_state = df.reindex(columns=column_names)
    state_select = st.sidebar.selectbox('Select a Country', df['Entity'].unique())
    selected_state = df[df['Entity'] == state_select]
    year_select = st.sidebar.selectbox('Select Year' , df['Year'].sort_values(ascending=True).unique())
    selected_year = selected_state[selected_state['Year'] == year_select]
    df4=selected_year.pivot_table(index=['Year'],values=['Death Numbers'],aggfunc=sum).iloc[[0],[0]].values
    fig3 = px.bar(selected_year, x='Year', y='Death Numbers',
    hover_data=['Code', 'Death Numbers'],color='Causes name',
    labels={'Death Numbers':'Total Death by diseases & accidents'}, height=400, width=650)
    st.title(f'Total Deaths by diseases & accidents in {state_select} in {year_select} : {str(int(df4))}')
    st.plotly_chart(fig3)
   
elif visualization == 'Model_4':
    column_names = ["Entity","Code","Year","Causes name","Causes Full Description","Death Numbers"]
    selected_state = df.reindex(columns=column_names)
    state_select = st.sidebar.selectbox('Select a Country', df['Entity'].unique())
    selected_state = df[df['Entity'] == state_select]
    Cause_select = st.sidebar.selectbox('Pilih Penyebab' , selected_state['Causes name'].sort_values(ascending=True).unique())
    selected_cause = selected_state[selected_state['Causes name'] == Cause_select]
    df1 = selected_cause.sort_values(by=['Year'])
    df2 = df1.replace(np.nan,0)
    df3=df2.pivot_table(index=['Causes name'],values=['Death Numbers'],aggfunc=sum).iloc[[0],[0]].values
    fig4 = px.line(df2,x='Year' , y='Death Numbers'
    ,hover_data=['Code', 'Causes name']
    )
    st.title(f'Total deaths Caused by {Cause_select} in {state_select} From 1990 - 2019 : {str(int(df3))}')
    st.plotly_chart(fig4)
