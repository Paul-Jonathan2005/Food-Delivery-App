import streamlit as st
import requests

def delete_items_in_cart_by_user_name(config):
    api_url = config["backend_end_url"] + "delete-item-to-cart/Jona"
    
    try:
        response = requests.delete(api_url)
        response.raise_for_status()
        return response.json()  # Assuming the API returns a JSON list of menu items
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch menu items: {e}")
        return []

def show(config):
    st.title("Thank You For Ordering The Food")
    delete_items_in_cart_by_user_name(config)
    st.session_state.cart = []
    st.session_state.selected_item_type = None

    col1,col2,col3 = st.columns([1,1,1])
    
    with col1:
        pass
    with col3:
        pass
    with col2:
        if st.button("Go To Home"):
            st.session_state.page = "welcome"
            st.rerun()