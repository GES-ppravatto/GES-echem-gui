import streamlit as st

def set_production_page_style():

    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """

    st.markdown(hide_st_style, unsafe_allow_html=True)