import streamlit as st
# import pandas as pd
# import numpy as np
# from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import requests 
# import http.client

# httpConn = http.client.HTTPSConnection("localhost", 5003)


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


if st.button("Submit"):
    #urllib request to api
    object = {"fname":fname, "lname":lname, "classes":classes, "studySpace":space, "phone":phone}
    r = requests.post("http://127.0.0.1:5003/api/users",data=object)

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

