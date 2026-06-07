import streamlit as st
import base64
import os

st.set_page_config(page_title="Sync Routine Analysis", layout="wide")

# Static components se padding aur menus ko hide karna
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

def get_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

try:
    html_content = get_file_content("index.html")
    
    # Folder ki sabhi files (images aur mp3) ko Streamlit internal routing mein bypass karna
    for file_name in os.listdir("."):
        if file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp3")):
            with open(file_name, "rb") as media_file:
                encoded_string = base64.b64encode(media_file.read()).decode()
                
            # HTML code ke andar relative paths ko base64 data URIs se replace karna
            if file_name.endswith(".mp3"):
                mime_type = "audio/mp3"
            else:
                mime_type = f"image/{file_name.split('.')[-1]}"
                
            old_path = f'src="{file_name}"'
            new_path = f'src="data:{mime_type};base64,{encoded_string}"'
            html_content = html_content.replace(file_name, f"data:{mime_type};base64,{encoded_string}")

    # Pure module ko Chrome security bypass ke sath render karna
    st.components.v1.html(html_content, height=1500, scrolling=True)

except Exception as e:
    st.error(f"Error executing frame render: {e}")