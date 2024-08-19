import streamlit as st
from pages import welcome, user_info, order_food, get_menu
from utils.config_loader import load_config

# Load configuration
config = load_config('config.json')

# Check if the session state variable is set
if 'page' not in st.session_state:
    st.session_state.page = "welcome"

# Page navigation logic
if st.session_state.page == "welcome":
    welcome.show(config)
elif st.session_state.page == "user_info":
    user_info.show(config)
elif st.session_state.page == "order_food":
    order_food.show(config)
elif st.session_state.page == "menu_page":
    get_menu.show(config)
