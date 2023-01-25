import pickle
import numpy as np
import streamlit as st
def main():

    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")
    st.title(' trying something new with streamlit')
    text1 = st.text_input('Enter your first text here')
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'cube will be', x * x * x)

if __name__ == '__main__':
    main()