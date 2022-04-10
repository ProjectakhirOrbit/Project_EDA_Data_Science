# Kita akan mulai dengan mengimpor beberapa library penting yang akan kita gunakan
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# Membangun aplikasi dashboard
st.title("Medical Cost Personal Datasets")
st.write("Biaya Medical berdasarkan beberapa faktor")
image = Image.open("Health.jpeg")
st.image(image, width=500)
st.markdown("Analisi Dataset ini menampilkan biaya medical berdasarkan faktor age dan region")
st.markdown('<style>body{background-color: lightblue}</style>', unsafe_allow_html=True)

# Import Dataset
@st.cache
def load_data():
    df = pd.read_csv("insurance.csv")
    return df

df = load_data()

visualization = st.sidebar.selectbox('Select a Chart type',('Bar Chart', 'Pie Chart', 'Line Chart'))
state_select = st.sidebar.selectbox('Select a region', df['region'].unique())
selected_state = df[df['region'] == state_select]
st.title('Region Medical Cost Level analysis')
def get_total_dataframe(df):
    total_dataframe = pd.DataFrame({
        'Status':['age','sex','bmi','children','smoker','region','charges'],
        'Number of cases': (df.iloc[0]['age'],
                            df.iloc[0]['sex'],
                            df.iloc[0]['bmi'],
                            df.iloc[0]['children'],
                            df.iloc[0]['smoker'],
                            df.iloc[0]['region'],
                            df.iloc[0]['charges'],
                            )
    })
    return total_dataframe

state_total = get_total_dataframe(selected_state)
if visualization == 'Bar Chart':
    bar_graph_age = px.bar(df, x='age', y='charges',
                               labels={'charges': 'Medical Cost in %s' % (state_select)}, color='age')
    st.plotly_chart(bar_graph_age)
    bar_graph_sex = px.bar(df, x='region', y='charges',
                               labels={'charges':'Medical Cost in%s' % (state_select)}, color='region')
    st.plotly_chart(bar_graph_sex)


elif visualization == 'Pie Chart':
    status_select = st.sidebar.radio('Medical Cost status', df['region'].unique())
    if status_select == 'southeast':
        st.markdown('## **Medical Cost southeast**')
        fig = px.pie(df, values=df['charges'][:1339], names=df['region'][:1339])
        st.plotly_chart(fig)
    elif status_select == 'southwest':
        st.markdown('## **Medical Cost southwest**')
        fig = px.pie(df, values=df['charges'][:1339], names=df['region'][:1339])
        st.plotly_chart(fig)
    elif status_select == 'northeast':
        st.markdown('## **Medical Cost northeast**')
        fig = px.pie(df, values=df['charges'][:1339], names=df['region'][:1339])
        st.plotly_chart(fig)
    else:
        st.markdown('## **Medical Cost northwest**')
        fig = px.pie(df, values=df['charges'][:1339], names=df['region'][:1339])
        st.plotly_chart(fig)
elif visualization == 'Line Chart':
    status_select = st.sidebar.radio('Medical Cost status', df['region'].unique())
    if status_select == 'southeast':
        st.markdown('## **Medical Cost southeast Charges**')
        fig = px.line(df, x='age', y='charges' , color='age'
        )
        st.plotly_chart(fig)
    elif status_select == 'southwest':
        st.markdown('## **Medical Cost southwest Charges**')
        fig = px.line(df, x='age', y='charges' , color='age')
        st.plotly_chart(fig)
    elif status_select == 'northeast':
        st.markdown('## **Medical Cost northeast Charges **')
        fig = px.line(df, x='age', y='charges', color='age')
        st.plotly_chart(fig)
    else:
        st.markdown('## **Medical Cost northwest Charges**')
        fig = px.line(df, x='age', y='charges' , color='age')
        st.plotly_chart(fig)

def get_table():
    datatable = df[['age','sex','bmi','children','smoker','region','charges']].sort_values(by=['region'],
                ascending=False)
    return datatable

datatable = get_table()
st.dataframe(datatable)