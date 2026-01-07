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
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

def navigate_to(page):
    st.session_state.current_page = page

# Sidebar Navigation Buttons
if st.sidebar.button("Home"):
    navigate_to("Home")
if st.sidebar.button("Car Rental"):
    navigate_to("Car Rental")
if st.sidebar.button("List of Available Cars"):
    navigate_to("List of Available Cars")
if st.sidebar.button("Help"):
    navigate_to("Help")

# --- PAGE LOGIC ---

# 1. HOME PAGE
if st.session_state.current_page == 'Home':
    st.header('Welcome to the home page!')

# 2. CAR RENTAL PAGE (Receipt Logic Here)
elif st.session_state.current_page == 'Car Rental':
    st.header('Car Rental Form')
    
    with st.form('profile_form'):
        name = st.text_input('Name')
        email = st.text_input('Email')
        option = st.selectbox(
            "Which car would you like to rent?",
            ("Toyota Sienta", "Toyota Prius", "Mazda CX-3", "Subaru e-Outback"),
        )
        newsletter = st.checkbox('Subscribe to newsletter')
        submitted = st.form_submit_button('Submit')

    if submitted:
        # A. Save to CSV
        csv_file = 'rental_bookings.csv'
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        booking_data = [current_time, name, email, option, newsletter]
        
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Date', 'Name', 'Email', 'Car Selected', 'Newsletter'])
            writer.writerow(booking_data)
        
        # B. THE RECEIPT DISPLAY
        # We use st.container with a border to look like a physical receipt
        st.divider()
        with st.container(border=True):
            st.markdown("### ✅ Booking Receipt")
            st.caption(f"Transaction ID: {hash(current_time)}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Customer:**")
                st.write(name)
                st.write(email)
            with col2:
                st.write("**Vehicle:**")
                st.write(option)
                st.write(f"_{current_time}_")
            
            st.divider()
            st.write("Please present this receipt at the counter.")
        
        st.toast("Booking saved successfully!")

# 3. AVAILABLE CARS
elif st.session_state.current_page == 'List of Available Cars':
    st.header("Cars Available")
    cars = ["Toyota Sienta", "Toyota Prius", "Mazda CX-3", "Subaru e-Outback"]
    for car in cars:
        st.caption(f"• {car}")

# 4. HELP PAGE
elif st.session_state.current_page == 'Help':
    st.title("AI Chatbot")
    with st.form(key="ai_form"):
        st.subheader("Prompt")
        user_prompt = st.text_area("Enter your prompt here", height=200)
        submit_ai = st.form_submit_button("Submit")

        if submit_ai:
            response, course_details = process_user_message(user_prompt)
            st.write(response)
            if course_details:
                st.dataframe(pd.DataFrame(course_details))
st.caption("2026 VB Ltd®")
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


# endregion <--------- Streamlit App Configuration --------->

