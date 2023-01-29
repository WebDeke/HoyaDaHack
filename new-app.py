import streamlit as st
import pandas as pd
import numpy as np
# from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import requests 
from requests.adapters import HTTPAdapter, Retry
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


if st.button("Find a partner"):
    data = [
    {"Rank": 1, "Name": "John", "Score": 5, "Courses": "CLSL 002, COSC 225, MATH 150", "Study Place": "C", "Phone": 1234356},
    {"Rank": 2, "Name": "Lauren", "Score": 4.5, "Courses": "COSC 225, MATH 150", "Study Place": "B", "Phone": 6543213},
    {"Rank": 3, "Name": "Geno", "Score": 4.0, "Courses": "MATH 150, CLSL 002", "Study Place": E, "Phone": 1111311"},
    ]

    st.write("### Your Best Matches")

    st.table(data)



# if st.button("Submit"):
#    urllib request to api
#    object = {"fname":fname, "lname":lname, "classes":classes, "studySpace":space, "phone":phone}
#   session = requests.Session()
#    retry = Retry(connect=3, backoff_factor=0.5)
#    adapter = HTTPAdapter(max_retries=retry)
#    session.mount('http://', adapter)
#    session.mount('https://', adapter)
#    req = session.post("http://127.0.0.1:5005/api/users",data=object)

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

