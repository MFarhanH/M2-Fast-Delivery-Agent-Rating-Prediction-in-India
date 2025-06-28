import numpy as np
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# load model
with open('D:/Hacktiv8/Phase 1/Milestone 1/p1-ftds027-hck-m2-MFarhanH/randomforest_regression_grid_best.pkl', 'rb') as file:
    rf_grid = pickle.load(file)


def run():
    # pembuatan form
    with st.form(key='Milestone2'):
        # Membuat Title
        st.title('Aplikasi Prediksi Rating Agent dari data Fast Delivery Agent (India)')

        # Membuat Sub Header
        st.subheader(
            'Page ini mengenai Exploratory Data Analysis dari dataset Fast Delivery Agent (India)')
        st.write('\n')
        st.write('\n')

        # # Menambahkan Gambar
        image1 = Image.open(
            'D:\Hacktiv8\Phase 1\Milestone 1\p1-ftds027-hck-m2-MFarhanH\Deployment\Foto Delivery.png')
        st.image(
            image1, caption='Prediksi Rating Agent dari data Fast Delivery Agent (India)')

        # Menambahkan Teks
        st.write('# Page ini dibuat oleh: \n # Muhammad Farhan Hendriyanto')
        st.write('# HCK-027')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        Agent_Name = st.selectbox(
            'Agent Name', ('Zepto', 'JioMart', 'Blinkit', 'Swiggy Instamart'), index=0)
        Delivery_Time = st.number_input(
            'Delivery Time: ', min_value=1, max_value=999, value=30, step=1, help='Delivery Time (mnt)')
        Location = st.selectbox(
            'Location', ('Delhi', 'Lucknow', 'Ahmedabad', 'Chennai', 'Pune', 'Jaipur', 'Mumbai', 'Kolkata', 'Hyderabad', 'Bangalore'), index=0)
        st.markdown('---')
        Order_Type = st.selectbox(
            'Order Type', ('Essentials', 'Grocery', 'Pharmacy', 'Electronics', 'Food'), index=0)
        Customer_Feedback_Type = st.selectbox(
            'Customer Feedback Type', ('Neutral', 'Negative', 'Positive'), index=0)
        st.markdown('---')
        Price_Range = st.selectbox(
            'Price Range', ('High', 'Low', 'Medium'), index=0)
        Discount_Applied = st.selectbox(
            'Discount Applied', ('Yes', 'No'), index=0)
        st.markdown('---')
        Product_Availability = st.selectbox(
            'Product Availability', ('Out of Stock', 'In Stock'), index=0)
        Customer_Service_Rating = st.number_input(
            'Customer Service Rating: ', min_value=0, max_value=5, value=2, step=1, help='Delivery Time (mnt)')
        Order_Accuracy = st.selectbox(
            'Order Accuracy', ('Incorrect', 'Correct'), index=0)
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

    data_inf = {

        'Agent Name': Agent_Name,
        'Delivery Time': Delivery_Time,
        'Location': Location,
        'Order Type': Order_Type,
        'Customer Feedback Type': Customer_Feedback_Type,
        'Price Range': Price_Range,
        'Discount Applied': Discount_Applied,
        'Product Availability': Product_Availability,
        'Customer Service Rating': Customer_Service_Rating,
        'Order Accuracy': Order_Accuracy
    }

    data_inf = pd.DataFrame([data_inf])
    data_inf

    if submitted:

        y_pred_inf = rf_grid.predict(data_inf)
        st.write('# Rating : ', str(int(y_pred_inf)))


if __name__ == '__main__':
    run()
