import streamlit as st
import pandas as pd
import numpy as np

st.title('Commilito: Find your study partner in arms.')

classes = st.multiselect(
    'What classes are you taking',
    ['COSC 225 - Computer Networks', 'MATH 150 – Linear Algebra', 'CHEM 228 - Synthetic Methods', 'PHYS 101 - Physics', 'HIST 007 – Introduction to Early History', 'CULP 346 - Crit Geography: Theory and Practice', 'CLSS 141 - Roman History', 'CLSL 002 - Latin II'],
    )

space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )
st.write('I am taking', classes, 'and my favorite study space is', space)