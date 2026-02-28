import streamlit as st
from  PIL import Image


with st.expander("Start the camera"):
    #start the camera
    camera_image = st.camera_input("Take a picture")

if camera_image:
    #create a pillow image instance
    img = Image.open(camera_image)

    #convert the image to grayscale
    gray_img = img.convert("L")

    #display the image on web page
    st.image(gray_img)

