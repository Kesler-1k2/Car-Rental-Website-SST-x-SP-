# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from helper_functions.utility import check_password

# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from datetime import datetime
current_datetime = datetime.now()
st.title("VB Transport Ltd")

st.write(':red[#1 Car Rental Company in Singapore]')

st.caption("R. VB Ltd")
if st.sidebar.button("Home"):
    page = "Home"
if st.sidebar.button("Car Rental"):
    page = "Car Rental"
if st.sidebar.button("List of Available Cars"):
    page = "List of Available Cars"



if page == 'Home':
    st.header('Welcome to the home page!')
elif page == 'Car Rental':
    st.header('Car Rental.')
    st.title('Forms Demo')
    with st.form('profile_form'):
        name = st.text_input('Name')
        email = st.text_input('Email')
        options = ["Toyota Sienta", "Toyota Prius", "Mazda CX-3", "Subaru e-Outback"]
        selection = st.pills("Directions", options, selection_mode="single")
        st.markdown(f"Your selected options: {selection}.")
        newsletter = st.checkbox('Subscribe to newsletter')
        submitted = st.form_submit_button('Submit')

    if submitted:
        st.success(f'''
        Car Rental
        {current_datetime}
        Selected Car: {selection}
        ''')

elif page == 'List of Available Cars':
  st.caption("Toyota Sienta")
  st.caption("Toyota Prius")
  st.caption("Mazda CX-3")
  st.caption("Subaru e-Outback")
# 1. Define the CSS for the background image
# We use Python f-strings to make it easy to swap the URL if needed.
  st.header("Cars Available")
image_url = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366"

background_css1 = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://s3-ap-southeast-1.amazonaws.com/motoristprod/editors%2Fimages%2F1640710025723-1640710025723.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Optional: This creates a semi-transparent overlay to make text readable */
[data-testid="stHeader"] {{
    background-color: rgba(0,0,0,0);
}}
</style>
"""


# 3. Your actual Python logic goes here


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)

# Do not continue if check_password is not True.
if not check_password():
    st.stop()

# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):

    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    st.write(response)
    print(response)

    st.divider()

    print(course_details)
    df = pd.DataFrame(course_details)
    df
