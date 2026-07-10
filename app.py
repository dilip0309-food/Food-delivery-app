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
if "cart" not in st.session_state:
    st.session_state.cart = []

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
    st.session_state.cart.append(selected_food)
    st.success(f"{selected_food} added to cart! ✅")

st.subheader("🛒 Your Cart")

if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"• {item}")
else:
    st.write("Your cart is empty.")
    
st.subheader("💰 Total Bill")

if st.button("Show Total Bill"):
    total = sum(food_menu[item] for item in st.session_state.cart)
    st.success(f"Your Total Bill is ₹{total}")
    
st.subheader("🔍 Search Food")

search = st.text_input("Enter food name")

if search:
    if search.title() in food_menu:
        st.success(f"{search.title()} is available! 🎉")
        st.write(f"Price: ₹{food_menu[search.title()]}")
    else:
        st.error("Food item not found.")

st.subheader("❌ Remove from Cart")

if st.session_state.cart:
    remove_item = st.selectbox(
        "Select item to remove",
        st.session_state.cart,
        key="remove_item"
    )

    if st.button("Remove Item"):
        st.session_state.cart.remove(remove_item)
        st.success(f"{remove_item} removed from cart! 🗑️")
        st.rerun()
else:
    st.info("Cart is empty.")
