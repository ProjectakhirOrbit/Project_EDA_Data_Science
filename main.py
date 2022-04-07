
#import Libraries yang diperlukan
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
visualization = st.sidebar.selectbox('Select Year ' , df['Year'].sort_values(ascending=True))

st.write(selected_state)
#bar_chart = px.bar(df , x='Death Numbers', y= selected_state)
#st.plotly_chart(bar_chart)

# st.title('Region Medical Cost Level analysis')

# def get_total_dataframe(df):
#    total_dataframe = pd.DataFrame({
  #      'Status':['age','sex','bmi','children','smoker','region','charges'],
 #       'Number of cases': (df.iloc[0]['age'],
    #                        df.iloc[0]['sex'],
     #                       df.iloc[0]['bmi'],
     #                       df.iloc[0]['children'],
      #                      df.iloc[0]['smoker'],
      #                      df.iloc[0]['region'],
       #                     df.iloc[0]['charges'],
       #                     )
  #  })
   # return total_dataframe

#state_total = get_total_dataframe(selected_state)