import streamlit as st

def show(config):
    st.title(config["welcome_message"])
    
    if st.button(config["get_started_button_text"]):
        # Set a session state variable to track page navigation
        st.session_state.page = "user_info"
        st.rerun()
