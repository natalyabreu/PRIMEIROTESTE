import streamlit as st
import pandas as pd 
import csv
st.title('tarefa do josir')
st.caption('Nataly Abreu')

df = pd.read_csv("Fruit Prices 2020.csv")
st.dataframe(df)
