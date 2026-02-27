import streamlit as st

st.set_page_config(page_title="Sum Calculator", page_icon="➕")

st.title("➕ Sum Calculator App")

st.write("Enter two numbers and get their sum")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Button
if st.button("Calculate Sum"):
    result = num1 + num2
    st.success(f"Sum = {result}")