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

st.subheader("🛒 Add to Cart")

if st.button("Add to Cart"):
    price = food_menu[selected_food]
    st.success(f"{selected_food} added to cart! ✅")
    st.write(f"Price: ₹{price}")

st.subheader("💰 Total Bill")

if st.button("Show Total Bill"):
    total = food_menu[selected_food]
    st.success(f"Your Total Bill is ₹{total}")

st.subheader("🔍 Search Food")

search = st.text_input("Enter food name")

if search:
    if search.title() in food_menu:
        st.success(f"{search.title()} is available! 🎉")
        st.write(f"Price: ₹{food_menu[search.title()]}")
    else:
        st.error("Food item not found.")
