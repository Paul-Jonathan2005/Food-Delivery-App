import requests
import streamlit as st

def fetch_menu_items(config):
  
    api_url = config["backend_end_url"] + "/all-item-in-menu"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()  
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch menu items: {e}")
        return []

def select_item_type(item_type):
    st.session_state.selected_item_type = item_type
    st.session_state.page = "food_items"
    st.rerun()

def show(config):
    if st.session_state.page == "menu_page":
        st.title(config["item_type_title"])
        
        
        menu_items = fetch_menu_items(config)
        all_items_types = menu_items.get("item_types", [])
    
        if all_items_types:
            for item in all_items_types:
                
                if st.button(item):
                    select_item_type(item)
        else:
            st.write("No menu items available.")