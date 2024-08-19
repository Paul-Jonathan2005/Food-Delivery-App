import streamlit as st
import requests
import re

def validate_phone_number(phone_number):
    """Validate phone number (basic check)."""
    if phone_number.isdigit() and len(phone_number) in [10, 11]:  # Example: 10 or 11 digit phone numbers
        return True
    return False

def validate_email(email):
    """Validate email address using a regex pattern."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    return False

def send_data_to_api(backend_end_url, user_data):
    """Send user data to the backend API."""
    try:
        response = requests.post(backend_end_url, json=user_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response  # Return JSON response from the API
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

def show(config):
    st.title(config["user_info_title"])
    
    with st.form(key='user_info_form'):
        username = st.text_input(config["form_labels"]["username"])
        password = st.text_input(config["form_labels"]["password"], type='password')
        phone_number = st.text_input(config["form_labels"]["phone_number"])
        email = st.text_input(config["form_labels"]["email"])
        
        submit_button = st.form_submit_button(config["submit_button_text"])
        
        if submit_button:
            # Validation checks
            phone_valid = validate_phone_number(phone_number)
            email_valid = validate_email(email)
            
            if not phone_valid:
                st.error("Invalid phone number. Please enter a 10 or 11 digit phone number.")
            if not email_valid:
                st.error("Invalid email address. Please enter a valid email address.")
            
            if phone_valid and email_valid:
                backend_end_url = config["backend_end_url"]  # Replace with your API URL
                backend_end_url = backend_end_url + "user"
    
                # Prepare data to send
                user_data = {
                    "customer_name": username,
                    "passcode": password,  # Ensure you handle passwords securely
                    "phone_number": phone_number,
                    "email": email
                }
                
                # Send data to the backend API
                response = send_data_to_api(backend_end_url, user_data)
                
                if response and response.status_code == 200:
                    # Navigate to another page on successful submission
                    st.session_state.page = "order_food"
                    st.rerun()
                    
                else:
                    st.write("Failed to submit data.")

           
