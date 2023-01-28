import streamlit as st
import pandas as pd
import numpy as np

st.title('Commilito: Find your study partner in arms.')
col1, col2 = st.columns([3, 1])

col1.subheader("A wide column with a chart")
classes = st.multiselect(
    'What classes are you taking',
    ['COSC 225', 'MATH 150', 'CHEM 228', 'PHYS 101', 'HIST 007', 'CULP 346', 'CLSS 141', 'CLSL 002'],
    )

space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )
col2.subheader("A narrow column with the data")
col2.fname = st.text_input('First name')
col2.lname = st.text_input('Last name')
col2.phone = st.text_input("Phone number")

st.button("Find a partner")