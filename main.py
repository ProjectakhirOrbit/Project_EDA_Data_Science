#import Libraries yang diperlukan
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

fig = px.bar(selected_state, x='Year', y='Death Numbers',
             hover_data=['Code', 'Causes Full Description'], color='Causes name',
             labels={'Death Numbers':'Total Death'}, height=400 , width=1200)
st.plotly_chart(fig)

Cause_select = st.selectbox('Pilih Penyebab' , selected_state['Causes name'].sort_values(ascending=True).unique())
selected_cause = selected_state[selected_state['Causes name'] == Cause_select]

fig2 = px.bar(selected_cause, x='Causes name', y='Death Numbers',
             hover_data=['Code', 'Death Numbers'],color='Causes name',
             labels={'Death Numbers':'Total Death'}, height=400 , width=400)
st.plotly_chart(fig2)


year_select = st.selectbox('Select Year' , selected_cause['Year'].sort_values(ascending=True).unique())
selected_year = selected_state[selected_state['Year'] == year_select]

fig3 = px.bar(selected_year, x='Year', y='Death Numbers',
             hover_data=['Code', 'Death Numbers'],color='Causes name',
             labels={'Death Numbers':'Total Death by diseases & accidents'}, height=400, width=650)
st.plotly_chart(fig3)

df3 = selected_cause.replace(np.nan,0)

fig4 = px.line(df3,x='Year' , y='Death Numbers')
st.plotly_chart(fig4)











