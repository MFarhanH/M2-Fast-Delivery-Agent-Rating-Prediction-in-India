import EDA
import Predict
import streamlit as st

page = st.sidebar.selectbox('Pilih Halaman', ('EDA', 'Predict'))

if page == 'EDA':
    EDA.run()

else:
    Predict.run()
