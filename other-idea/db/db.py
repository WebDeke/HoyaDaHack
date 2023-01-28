#db.py
import streamlit as st
from pymongo import MongoClient

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton(suppress_st_warning=True)
def init_connection():
    return MongoClient("mongodb+srv://asundar:5zGDjohcbP4TApTH@studyusers.b1bzofp.mongodb.net/?retryWrites=true&w=majority")

# client = init_connection("mongodb+srv://studyusers.b1bzofp.mongodb.net/StudyUsers")
client = init_connection()

# Pull data from the collection.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def get_data():
    db = client.Users
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.experimental_memo
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")