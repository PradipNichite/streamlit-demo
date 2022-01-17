# from nbformat import read
import streamlit as st
import os
import csv
import tempfile


x = st.slider('Select a value')
uploaded_file = st.file_uploader("Choose a file",type="csv")



temp_dir = tempfile.TemporaryDirectory()

if uploaded_file:
    # st.write("Uploaded file name: ",uploaded_file.name)
    
    temp_csv_file_name = os.path.join(temp_dir.name,"sample.csv")
    temp_txt_file_name = os.path.join(temp_dir.name,"sample.txt")
    with open(temp_csv_file_name,"wb") as f: 
        f.write(uploaded_file.getbuffer()) 
    
    with open(temp_csv_file_name,'r') as f:
        with open(temp_txt_file_name,'w') as ft:
            reader = csv.reader(f)
            next(reader)
            for i,row in enumerate(reader):
                ft.write(row[0])
                ft.write("---")
    with open(temp_txt_file_name,'r') as ft:
        data = ft.read()
    file_name = uploaded_file.name.split(".csv")[0] + ".txt"
    st.download_button('Download Text File', data=data,file_name=file_name)  # Defaults to 'text/plain'

    temp_dir.cleanup()
