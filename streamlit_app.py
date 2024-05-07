import streamlit as streamlit
import pandas as pd
st.write("""
        #Weed detection App
        This app detects the common weed found in the Wheat field
        """)

st.selectbox('Select Your Province', ["Punjab","Sindh","Balochistan", "KPK", "Azad Jammu and Kashmir", "Gilgit-Baltistan"])
st.camera_input("Please take the image of the field.")
st.write("or")
st.file_uploader('Upload the image of the field', type=['jpg','png','jpeg'])
