#import libraries

import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

#import data
st.title("Plotly and streamlit App")
df=px.data.gapminder()
st.write(df.head())
st.write(df.columns)

#summary stat
st.write(df.describe())

#data management
year_option =df['year'].unique().tolist()

year= st.selectbox("Select year which we plot", year_option, 0)
# df = df[df['year'] == year]

#plotting

fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent',
 hover_name='country', log_x=True, size_max=55, range_x=[100, 10000], range_y=[20,90]
 ,animation_frame='year', animation_group='country')
 

st.write(fig)

