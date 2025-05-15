import streamlit as st
import importlib

# Import pages dynamically
def load_page(page_name):
    page = importlib.import_module(page_name)
    # print(111111111111111,page)
    page.run()

# Ensure login status is initialized if not already set
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Page Navigation based on login status
if st.session_state.logged_in:
    # If the user is logged in, automatically redirect to the prediction page
    page = "Prediction"
else:
    # If not logged in, show the login page and other options
    page = st.sidebar.radio("Select a page", ["Home", "About", "Register", "Login"])

# Render the selected page based on the page selected
if page == "Home":
    load_page("home")  # Replace with your actual home page module
elif page == "About":
    load_page("about")  # Replace with your actual about page module
elif page == "Register":
    load_page("register")  # Registration page
elif page == "Login":
    load_page("login")  # Login page
elif page == "Prediction":
    load_page("prediction")  # Prediction page, accessible only after login
    # run()

