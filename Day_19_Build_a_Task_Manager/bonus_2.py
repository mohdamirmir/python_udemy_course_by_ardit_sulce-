import streamlit as st
from  PIL import Image


with st.expander("Upload Image"):
    #upload the image
    uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    #create a pillow image instance
    img = Image.open(uploaded_image)

    #convert the image to grayscale
    gray_img = img.convert("L")

    #display the image on web page
    st.image(gray_img)

