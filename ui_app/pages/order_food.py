import streamlit as st

def show(config):
    st.title(config["user_data_saved"])
    
    if st.button(config["order_food_button_text"]):
        # Set a session state variable to track page navigation
        st.session_state.page = "menu_page"
        st.rerun()
