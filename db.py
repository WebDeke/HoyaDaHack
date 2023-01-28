
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import streamlit as st
from gsheetsdb import connect

rowcount = 3
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "./studybuddy-376115-369daa1f5b57.json", scope)

client = gspread.authorize(credentials)


# Open the spreadhseet
sheet = client.open("Commilito Backend").worksheet("commilito_backend")

# Get a list of all records
data = sheet.get_all_records()
pprint(data)

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

def addUser(fname, lname):
    rowcount+=1
    sheet.insert_row([rowcount, fname, lname],rowcount)
def addCourses(rowcount, classes):
    record = sheet.row_values(rowcount)
    sheet.update_cell(rowcount, 4, classes)
def favoriteSpace(space):
    sheet.update_cell(rowcount, 5, space)
def phone(phone):
    sheet.update_cell(rowcount, 6, phone)

# Get a list of all records
def userList(): 
    data = sheet.get_all_records()
    pprint(data)


# def add_courses(course):
#     # Add a new user's course information to the database
#     conn = connect()
    
#     insertRow = [courses]
#     sheet_url.insert(insertRow,0)
#     conn.commit()
#     conn.close()

# def find_study_buddies(username):
#     # Find other users who are taking the same courses
#     conn = sqlite3.connect('study_buddies')
#     c = conn.cursor()
#     c.execute("SELECT * FROM courses WHERE username!=? AND courses IN (SELECT courses FROM courses WHERE username=?)", (username,username))
#     results = c.fetchall()
#     conn.close()
#     return results

# # Print results.
# for row in rows:
#     st.write(f"{row.name} is taking :{row.courses}:")
#     st.write(f"Email: {row.email}")

# def create_database():
#     # Create a new SQLite database and create a table to store course information
#     conn = sqlite3.connect('study_buddies')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS courses (username text, courses text)''')
#     conn.commit()
#     conn.close()
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