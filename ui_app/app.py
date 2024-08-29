import streamlit as st
from pages import welcome, user_info, order_food, get_menu, food_items, go_to_cart, payment_page, thank_you
from utils.config_loader import load_config

# Load configuration
config = load_config('config.json')

# Check if the session state variable is set
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.cart = []

# Page navigation logic
if st.session_state.page == "welcome":
    welcome.show(config)
elif st.session_state.page == "user_info":
    user_info.show(config)
elif st.session_state.page == "order_food":
    order_food.show(config)
elif st.session_state.page == "menu_page":
    get_menu.show(config)
elif st.session_state.page == "food_items":
    food_items.show(config)
elif st.session_state.page == "go_to_cart":
    go_to_cart.show(config)
elif st.session_state.page == "payment_page":
    payment_page.show(config)
elif st.session_state.page == "thank_you_page":
    thank_you.show(config)