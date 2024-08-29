import streamlit as st
import requests

def get_items_by_item_type(config, item_type):
    api_url = config["backend_end_url"] + "/all-item-in-menu/" + item_type 
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()  # Assuming the API returns a JSON list of menu items
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch menu items: {e}")
        return []
    
def add_to_cart(item_name, item_cost, config):
    """Function to handle adding items to the cart."""
    api_url = config["backend_end_url"] + "item-to-cart" 
    
    data = {
        "user_name": "Jona",
        "number_of_items": 1,
        "item_name": item_name ,
        "item_cost": item_cost
    }
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()
        st.session_state.cart.append(item_name)
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to add item to cart: {e}")
        return False
    
def show_items(items, config):

    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.title(f"{st.session_state.selected_item_type}")

    with col2:
        if st.button("Back"):
            st.session_state.page = "menu_page"
            st.rerun()

    with col3:
        if st.button("Go to Cart"):
            st.session_state.page = "go_to_cart"
            st.rerun()

    if items:
        for item in items:
            col4, col5, col6 = st.columns([3,3,2])
            item_name = item.get("item_name", "Unnamed Item")
            item_cost = item.get("item_cost", "Unknown Cost")
            
            # Layout for each item
            with col4:
                st.write(f"**{item_name}**")

            with col5:
                st.write(f"Cost: ${item_cost}")

            with col6:
                if item_name in [cart_item for cart_item in st.session_state.cart]:
                    st.success("Added to cart!", icon="✅")
                else:

                    with col6:
                        if st.button("Add to Cart", key=item_name):
                            success = add_to_cart(item_name, item_cost, config)
                            if success:
                                st.rerun()
   
def show(config):
    item_type =  st.session_state.selected_item_type 
    items = get_items_by_item_type(config, item_type)
    items = items.get("items", [])
    if items:
        show_items(items, config)
    else:
        st.write(f"No item types are availale for {item_type}")