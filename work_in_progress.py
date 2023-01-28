import streamlit as st
from gsheetsdb import connect
from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

street = st.sidebar.text_input("Street", "75 Bay Street")
city = st.sidebar.text_input("City", "Toronto")
province = st.sidebar.text_input("Province", "Ontario")
country = st.sidebar.text_input("Country", "Canada")

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+province+", "+country)

lat = location.latitude
lon = location.longitude

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

st.map(map_data) 


def main():
    st.set_page_config(page_title="Study Buddy Finder", page_icon=":guardsman:", layout="wide")
    st.title("Study Buddy Finder")

    options = st.multiselect(
    'What classes are you taking?', ,
    )

    space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )
    st.write('I am taking', options, 'and my favorite study space is', space)

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
