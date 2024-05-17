import hmac
import streamlit as st

password = "huutin0908200471"
check = st.text_input("Please enter your password:")
if check != password:
    st.write('False')
else:
    st.write('True')