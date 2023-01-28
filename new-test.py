import streamlit as st
import pandas as pd
import numpy as np

st.title('Find a Study Buddy Near You!')

options = st.multiselect(
    'What classes are you taking',
    ['Green', 'Yellow', 'Red', 'Blue'],
    )

space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )
st.write('I am taking', options, 'and my favorite study space is', space)