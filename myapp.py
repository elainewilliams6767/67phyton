import streamlit as st

st.title("My first streamlit app")

st.write ("welcome to my first streamlet app!")

name = st.text_input("Enter your name")

st.success("hello " + name + "!Welcome to the app.")



feeling = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Disapointed", "angery"])


