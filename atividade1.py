import streamlit as st
import pandas as pd 
import csv
st.title('Municípios brasileiros')
st.caption('Nataly Abreu - Atividade 1')

df = pd.read_csv('brasil-win.csv', encoding='ISO-8859-1')

st.dataframe(df)

st.bar_chart(chart_data.set_index)
