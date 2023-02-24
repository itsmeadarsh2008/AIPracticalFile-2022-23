import streamlit as st

st.write('''
# Artificial Intelligence Practical File 2022-23 `(Adarsh Gourab Mahalik)`

''')
with open('./AI Practical File.md','r') as f:
    st.write(f.read())