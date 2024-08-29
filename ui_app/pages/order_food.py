import streamlit as st

def show(config):
    st.title(config["user_data_saved"])
    col1,col2,col3 = st.columns([1,1,1])
    
    with col1:
        pass
    with col3:
        pass
    with col2: 
        if st.button(config["order_food_button_text"]):
            # Set a session state variable to track page navigation
            st.session_state.page = "menu_page"
            st.rerun()
