#import Libraries yang diperlukan
from matplotlib.pyplot import text
import streamlit as st
import pandas as pd
import numpy as np
from turtle import width
from PIL import Image
import plotly.express as px

# Membangun aplikasi dashboard
# image = Image.open("Health.jpeg")
#st.image(image, width=500)
st.markdown('<style>body{background-color: lightblue}</style>', unsafe_allow_html=True)
st.header("""
Analisis Dashboard Penyebab Kematian Di Dunia ☠️
""")

# Import Dataset
@st.cache
def load_data():
    df = pd.read_csv("Death_causes.csv")
    return df

df = load_data()

state_select = st.sidebar.selectbox('Select a Country', df['Entity'].unique())
selected_state = df[df['Entity'] == state_select]


column_names = ["Entity","Code","Year","Causes name","Causes Full Description","Death Numbers"]

selected_state = selected_state.reindex(columns=column_names)

st.title('analisis Penyebab Kematian di dunia')
st.write(selected_state)
col1, col2 , col3 = st.columns(3)

with col1:
    st.write(selected_state['Entity'])

with col2:
    st.write(selected_state['Causes Full Description'])
with col3:
    st.write(selected_state['Year'])

bar_graph_Cause = px.bar(selected_state, x='Causes name', y='Death Numbers'.format(int),color='Causes name', width=1000, height=600)
st.plotly_chart(bar_graph_Cause)

def test_asc():
    visualization1 = df['Year'].sort_values(ascending=True)
    visualization2 = list(set(visualization1))
    visualization3 = st.selectbox('Select Year ' , visualization2)
    return visualization3

visualization3 = test_asc()
selected_year = df[df['Year'] == visualization3]
st.markdown('Scatter plot Jumlah Kematian yang disebabkan oleh penyakit berdasarkan tahun ke tahun')
st.markdown(visualization3)
scatter_graph_year = px.scatter(selected_year,x='Causes name', y='Death Numbers' , color='Causes name', width=1000, height=600)

scatter_graph_year.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
st.plotly_chart(scatter_graph_year)




