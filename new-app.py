import streamlit as st
import pandas as pd
import numpy as np

st.title('Commilito: Find your study partner in arms.')

classes = st.multiselect(
    'What classes are you taking',
    ['COSC 225', 'MATH 150', 'CHEM 228', 'PHYS 101', 'HIST 007', 'CULP 346', 'CLSS 141', 'CLSL 002'],
    )

space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )

st.button("Find a partner")
