import streamlit as st
import streamlit.components.v1 as components

# Page configuration ko set karein taaki layout wide aur clean dikhe
st.set_page_config(page_title="Sync Routine Analysis", layout="wide")

# CSS se default Streamlit ke paddings, headers aur footers ko poori tarah hide kar dein
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

# Aapki poori index.html file ko Streamlit ke andar render karna
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# HTML content ko poore screen par embed karna
components.html(html_content, height=1500, scrolling=True)