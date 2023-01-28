import streamlit as st
import sqlite3

def create_database():
    # Create a new SQLite database and create a table to store course information
    conn = sqlite3.connect('study_buddies.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE courses
                 (username text, courses text)''')
    conn.commit()
    conn.close()

def add_courses(username, courses):
    # Add a new user's course information to the database
    conn = sqlite3.connect('study_buddies.db')
    c = conn.cursor()
    c.execute("INSERT INTO courses VALUES (?,?)", (username, courses))
    conn.commit()
    conn.close()

def find_study_buddies(username):
    # Find other users who are taking the same courses
    conn = sqlite3.connect('study_buddies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM courses WHERE username!=? AND courses IN (SELECT courses FROM courses WHERE username=?)", (username,username))
    results = c.fetchall()
    conn.close()
    return results

def main():
    st.set_page_config(page_title="Study Buddy Finder", page_icon=":guardsman:", layout="wide")
    st.title("Study Buddy Finder")

    # create the database if it doesn't exist
    create_database()
    # get the username and courses from the user
    username = st.text_input("Enter your username:")
    courses = st.text_input("Enter the courses you are taking (separated by commas):")

    if st.button('Submit'):
        # add the user's courses to the database
        add_courses(username, courses)
        # find other users who are taking the same courses
        results = find_study_buddies(username)
        # display the results
        if results:
            st.success("Here are your study buddies:")
            st.table(results)
        else:
            st.warning("Sorry, no study buddies found.")

if __name__== "__main__":
    main()
