
import streamlit as st
from gsheetsdb import connect

public_gsheets_url = "https://docs.google.com/spreadsheets/d/1tYPHXibwW4lMQBH8iaXOXqZHg5P7-lVQ7JZ8EGmki5w/edit#gid=0"
# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")

# #db.py
# import streamlit as st
# from pymongo import MongoClient

# # Initialize connection.
# # Uses st.experimental_singleton to only run once.
# @st.experimental_singleton(suppress_st_warning=True)
# def init_connection():
#     return MongoClient("mongodb+srv://asundar:5zGDjohcbP4TApTH@studyusers.b1bzofp.mongodb.net/?retryWrites=true&w=majority")

# # client = init_connection("mongodb+srv://studyusers.b1bzofp.mongodb.net/StudyUsers")
# client = init_connection()

# # Pull data from the collection.
# # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def get_data():
#     db = client.Users
#     items = db.mycollection.find()
#     items = list(items)  # make hashable for st.experimental_memo
#     return items

# items = get_data()

# # Print results.
# for item in items:
#     st.write(f"{item['name']} has a :{item['pet']}:")