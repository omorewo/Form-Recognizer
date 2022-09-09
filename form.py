import streamlit as st     #streamlit run form.py
import os
import pandas as pd
from PIL import Image
#import pdf2image #converts pdf to image
#import PyPDF2  #converts pdf to text
import easyocr
import cv2
import pdfplumber

# try image to pdf
@st.cache
def load_image(image_file):
    # convert pdf to image
    if image_file.type != 'application/pdf':   
        img = Image.open(image_file)
    return img


# add a function to save uploaded files to a directory

def main():
    st.title("CONVERT YOUR RECEIPTS INTO A SINGLE SPREADSHEET")
    # Load file (image and pdf)
    st.subheader("Upload your Image or PDF receipt")

    receipt_file = st.file_uploader("Upload your receipt", type = ['pdf', 'png', 'jpeg', 'jpg'])

    if receipt_file is not None:
        file_details = {'File Name': receipt_file.name, "File Type": receipt_file.type}
        st.write(file_details)
        
        if receipt_file.type == 'application/pdf':
            with pdfplumber.open(receipt_file) as pdf:
                page = pdf.pages[0]
                text = page.extract_text()
            
            st.write(text)

        else:
            receipt = load_image(receipt_file)
        
            # Extract Info from file to txt
            reader = easyocr.Reader(['en'], gpu = False)
            result = reader.readtext(receipt)
            st.write(result)
            print(result)
            


    # Append To Excel

if __name__ == "__main__":
    main()
