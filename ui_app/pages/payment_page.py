import streamlit as st
import requests
from PIL import Image



def show(config):
    total_price = st.session_state.total_price
    st.title(f"Total Amount: Rs {total_price}")
    st.write("You can complete your payment using PhonePe.")

    st.header("PhonePe Payment Details")
    st.write("PhonePe Number: +91-9676103385")  
    st.write("Please scan the QR code below to make the payment.")

    
    qr_code_image = Image.open(r"C:/Users/Kakani Nageswara Rao/OneDrive/Documents/Food-Delivery-App/ui_app/assets/QR Code.png")  
    st.image(qr_code_image, caption="Scan to Pay via PhonePe", use_column_width=True)

    if st.button("Continue"):
        st.session_state.page = "thank_you_page"
        st.rerun()