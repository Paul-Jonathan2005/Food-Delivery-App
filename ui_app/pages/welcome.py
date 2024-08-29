import streamlit as st

def show(config):
    st.title(config["welcome_message"])
    col1,col2,col3 = st.columns([1,1,1])
    
    with col1:
        pass
    with col3:
        pass
    with col2:
        if st.button(config["get_started_button_text"]):
            st.session_state.page = "user_info"
            st.rerun()
