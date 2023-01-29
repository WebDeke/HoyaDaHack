import streamlit as st
import pandas as pd
import numpy as np
# from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import streamlit as st
from urllib import requests 
import http.client

# import sys, subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread'])
# scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# credentials = ServiceAccountCredentials.from_json_keyfile_name(
#     "./studybuddy-376115-369daa1f5b57.json", scope)

# client = gspread.authorize(credentials)

httpConn = http.client.HTTPSConnection("localhost", 5003)


# Open the spreadhseet
# sheet = client.open("Commilito Backend").worksheet("commilito_backend")

# # Get a list of all records
# data = sheet.get_all_records()
# pprint(data)

# public_gsheets_url = "https://docs.google.com/spreadsheets/d/1tYPHXibwW4lMQBH8iaXOXqZHg5P7-lVQ7JZ8EGmki5w/edit#gid=0"
# Create a connection object.

rowcount = 4
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows

# sheet_url = st.secrets["public_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows
# def addUser(fname, lname):
#     global rowcount
#     rowcount += 1
#     sheet.insert_row([str(rowcount-1), fname, lname], rowcount)


# def addCourses(classes):
#     global rowcount
#     record = sheet.row_values(rowcount)
#     sheet.update_cell(rowcount, 4, classes)


# def favoriteSpace(space):
#     global rowcount
#     sheet.update_cell(rowcount, 5, space)


# def phone(phone):
#     global rowcount
#     sheet.update_cell(rowcount, 6, phone)



#START OF STREAMLIT CODE..................

st.title('Commilito')
st.subheader("Combine academic weapons.")
fname = st.text_input("first name")
lname = st.text_input("last name")

classes = st.multiselect(
    'What classes are you taking',
    ['COSC 225', 'MATH 150', 'CHEM 228', 'PHYS 101',
        'HIST 007', 'CULP 346', 'CLSS 141', 'CLSL 002'],
)

space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )

phone = st.text_input("Phone number")


st.button("Find a partner")


object = {"fname":fname, "lname":lname, "classes":classes, "studySpace":space, "phone":phone}
r = requests.post("localhost:5003/users",data=object)
print(r.text)

#............................................


# #TEST CODE, not part of codebase
# # Create a connection object.
# print("Hello World!")
# addUser("Hanz", "Zimmer")
# # addUser()
# classitems = "Calc1,Calc2"
# addCourses(classitems)

# sheet.col_values

# st.write(sheet.get_all_records())

