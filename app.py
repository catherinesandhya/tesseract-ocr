import streamlit as st
import cv2
import pytesseract
from PIL import Image #PIL or python imaging library is used to open images in streamlit as streamlit does not display images directly
pytesseract.pytesseract.tesseract_cmd='/app/.apt/usr/bin/tesseract'  #for heroku  setup
st.set_option('deprecation.showfileUploaderEncoding',False) #Ignores the warning
st.title("OCR - Optical Character Recognition")
st.text('Upload the image')  #like write
uploaded_file=st.sidebar.file_uploader('Choose an image',type=["jpg","jpeg","png"])  #create a file uploader and can upload the image with 3 extensions given
if uploaded_file is not None:   #Only if a file is uploaded, perform the below
  img=Image.open(uploaded_file)  #opens uploaded file
  st.image(img,caption='Uploaded Image',use_column_width=True)  #display the uploaded image with original width and height
  st.write('')

  if st.button('PREDICT'):  #if predict button is pressed
    st.write("Result...")
    info=pytesseract.image_to_string(img)   #perform ocr - open CV not used, uploaded image is fetched using PIL as streamlit cannot open the image
    st.title(info)   #display the text extracted from image
