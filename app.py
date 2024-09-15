import streamlit as st
import pickle

# Custom CSS to adjust font size and create a transparent footer
st.markdown(
    """
    <style>
    .big-font {
        font-size:40px !important;
    }
    .medium-font {
        font-size:24px !important;
        color: white;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 16px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Load the trained model
with open('model_pickle', 'rb') as f:
    model = pickle.load(f)

# Title of the web app
st.markdown('<p class="big-font">House Price Prediction App</p>', unsafe_allow_html=True)

# Input from the user
area = st.number_input('Enter the area of the house (in sqft):', min_value=500, max_value=10000, step=100)

# Predict the price when the user clicks the button
if st.button('Predict Price'):
    prediction = model.predict([[area]])[0]  # Predict the price
    st.markdown(f'<p class="medium-font">The predicted price for a house with {area} sqft area is: ${prediction:,.2f}</p>', unsafe_allow_html=True)

# Add transparent footer with author credit
st.markdown('<div class="footer">Author: Kanav Gupta</div>', unsafe_allow_html=True)
