import streamlit as st
from utils import detect_plagiarism, efficiency_matrix

st.title('Plagiarism Detection System')

text = st.text_area('Enter the text:')
pattern = st.text_area('Enter the pattern to search:')

if st.button('Detect Plagiarism'):
    result = detect_plagiarism(text, pattern)
    st.write('Plagiarism Detected' if result else 'No Plagiarism Detected')
    
    efficiency = efficiency_matrix(text, pattern)
    st.write('Efficiency Matrix:')
    st.write(efficiency)

