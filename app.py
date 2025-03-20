import streamlit as st
import pandas as pd
import pickle
import time
import numpy as np

# Load the trained model
with open("xgboost_model.pkl", "rb") as file:
    model = pickle.load(file)

# Unique values mapping based on dataset
exterior_colors = ["Black", "White", "Gray", "Blue", "Red", "Silver"]
interior_colors = ["Black", "Beige", "Gray", "Brown", "White"]
drivetrains = ["FWD", "RWD", "AWD", "4WD"]
fuel_types = ["Gasoline", "Diesel", "Electric", "Hybrid"]
transmissions = ["Automatic", "Manual"]
engines = ["1.5L", "2.0L", "2.5L", "3.0L", "3.5L", "4.0L"]

# Streamlit App Title
st.set_page_config(page_title="Car Price Predictor", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .stButton>button {
        color: white;
        background-color: #ff4b4b;
        border-radius: 10px;
        width: 100%;
        height: 50px;
        font-size: 18px;
    }
    .stSelectbox, .stNumberInput {
        background-color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Image
st.image("https://cdn.pixabay.com/photo/2017/07/05/16/56/car-2474785_960_720.jpg", use_container_width=True)

st.title("🚗 Car Price Prediction")
st.write("### Enter the details below to predict the price of your car.")

# Create input fields
exterior_color = st.selectbox("Exterior Color", exterior_colors)
interior_color = st.selectbox("Interior Color", interior_colors)
drivetrain = st.selectbox("Drivetrain", drivetrains)
mpg = st.number_input("Miles Per Gallon (MPG)", min_value=10, max_value=50, step=1)
fuel_type = st.selectbox("Fuel Type", fuel_types)
transmission = st.selectbox("Transmission", transmissions)
engine = st.selectbox("Engine Size", engines)
mileage = st.number_input("Mileage (miles)", min_value=0, max_value=300000, step=5000)

# Convert inputs to numerical format (assuming correct mapping)
exterior_color_num = exterior_colors.index(exterior_color)
interior_color_num = interior_colors.index(interior_color)
drivetrain_num = drivetrains.index(drivetrain)
fuel_type_num = fuel_types.index(fuel_type)
transmission_num = transmissions.index(transmission)
engine_num = engines.index(engine)

# Prediction button
if st.button("Predict Price"):
    with st.spinner("Predicting... 🚀"):
        time.sleep(2)  # Simulate processing time
        
        # Create input dataframe
        input_data = pd.DataFrame([[exterior_color_num, interior_color_num, drivetrain_num, mpg, 
                                    fuel_type_num, transmission_num, engine_num, mileage]], 
                                  columns=['Exterior color', 'Interior color', 'Drivetrain', 'MPG', 
                                           'Fuel type', 'Transmission', 'Engine', 'Mileage'])

        # Make prediction
        predicted_price = model.predict(input_data)

        # Display result
        st.success(f"💰 Estimated Price: **${predicted_price[0]:,.2f}**")

