import streamlit as st
import pandas as pd 
import csv
st.title('Municípios brasileiros')
st.caption('Nataly Abreu - Atividade 1')

df = pd.read_csv('brasil-win.csv', sep =',')
st.dataframe(df)
