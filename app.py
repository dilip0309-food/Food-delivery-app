import streamlit as st
import pandas as pd

st.title("🍔 Food Delivery App")

st.write("Welcome to the Food Delivery App!")
st.write("Select your favorite food items.")

food_menu = {
    "Pizza": 250,
    "Burger": 150,
    "Biryani": 200,
    "Fried Rice": 180,
    "Sandwich": 120
}

st.subheader("📋 Food Menu")

for item, price in food_menu.items():
    st.write(f"{item} - ₹{price}")

st.subheader("🍽️ Select Your Food")

selected_food = st.selectbox(
    "Choose a food item",
    list(food_menu.keys())
)

st.write("You selected:", selected_food)
