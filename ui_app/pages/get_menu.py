import requests
import streamlit as st


# Function to fetch menu items from an API
def fetch_menu_items(config):
    # Replace with your actual API endpoint
    api_url = config["backend_end_url"] + "/all-item-in-menu"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()  # Assuming the API returns a JSON list of menu items
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch menu items: {e}")
        return []

# Function to handle menu item selection and navigation
def select_item_type(item_type):
    st.session_state.selected_item_type = item_type
    st.session_state.page = "food_items"
    st.rerun()

# Get Menu Page content
def show(config):
    if st.session_state.page == "menu_page":
        st.title(config["item_type_title"])
        
        # Fetch menu items
        menu_items = fetch_menu_items(config)
        all_items_types = menu_items.get("item_types", [])
        
        # Display each menu item as a clickable button
        if all_items_types:
            for item in all_items_types:
                
                if st.button(item):
                    select_item_type(item)
        else:
            st.write("No menu items available.")