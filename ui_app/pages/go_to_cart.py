import streamlit as st
import requests


def get_cart_items( config):
    api_url = config["backend_end_url"] + "all-item-in-menu/user/Jona"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()  # Assuming the API returns a JSON list of menu items
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to get cart items: {e}")
        return []

def remove_item(item_name, config):
    api_url =  config["backend_end_url"] + "/item-to-cart/Jona/" + item_name

    try:
        response = requests.delete(api_url)
        response.raise_for_status()
        st.session_state.cart.remove(item_name)
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to add item to cart: {e}")
        return False

def increase_item_count(item_name, config):
    api_url =  config["backend_end_url"] + "/increase-item-count"

    data = {
        "user_name": "Jona",
        "item_name": item_name 
    }
    try:
        response = requests.put(api_url, json=data)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to add item to cart: {e}")
        return False
    
def decrease_item_count(item_name, config):
    api_url =  config["backend_end_url"] + "/decrease-item-count"

    data = {
        "user_name": "Jona",
        "item_name": item_name 
    }
    try:
        response = requests.put(api_url, json=data)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to add item to cart: {e}")
        return False

def show(config):

    col1, col2= st.columns([3, 1])
    
    with col1:
        st.title("Your Cart")

    with col2:
        if st.button("Back"):
            st.session_state.page = "food_items"
            st.rerun()

    cart_items = get_cart_items(config)
    cart_items = cart_items['cart_items']

    if cart_items:
        total_price = 0
        for cart_item in cart_items:
            item_name = cart_item['item_name']
            item_cost = cart_item['item_cost']
            no_of_items = cart_item['no_of_items']
            item_price = int(item_cost)*int(no_of_items)
            total_price+=item_price 

            col1, col2, col3, col4, col5, col6 = st.columns([2.5, 1, 1, 1, 1.5, 1])

            with col1:
                st.write(f"**{item_name}** - ${item_cost}")
            
            with col2:
                if st.button("Minus", key=f"minus-{item_name}"):
                    decrease_item_count(item_name, config)
                    st.rerun()

            
            with col3:
                st.write(f"{no_of_items}")
            
            with col4:
                if st.button("Plus", key=f"plus-{item_name}"):
                    increase_item_count(item_name, config)
                    st.rerun()

            with col5:
                if st.button("Remove", key=f"remove-{item_name}"):
                    remove_item(item_name, config)
                    st.rerun()
            
            with col6:
                st.write(f"Rs {item_price}")

        col7,col8,col9 = st.columns([1,1,1])
    
        with col7:
            pass
        with col9:
            pass
        with col8:
        
            st.write(f"Total Amount:  Rs {total_price}")

            if st.button("Pay The Bill"):
                st.session_state.total_price = total_price
                st.session_state.page = "payment_page"
                st.rerun()

    else:
        st.write("Empty")