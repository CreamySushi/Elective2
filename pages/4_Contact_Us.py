import streamlit as st
from utils.styles import sidebar_styles, text_outline_styles, hide_streamlit_style


st.markdown(sidebar_styles(), unsafe_allow_html=True)
st.markdown(hide_streamlit_style(), unsafe_allow_html=True)
st.markdown(text_outline_styles(), unsafe_allow_html=True)

st.title("Contact Us")
st.markdown("""
    <div style="color: white;text-align=justify">
        <h3>If you have any questions, suggestions, or feedback, feel free to reach out to us at:</h3>
        <h3><strong>Email:</strong>support@uphs-calories.com</h3>
        <h3><strong>Phone:</strong> +63 912 345 6789</h3>
        <h3><strong>Address:</strong> University of Perpetual Help System - Laguna, Biñan City, Laguna, Philippines</h3>

""", unsafe_allow_html=True)

st.markdown("""
<a href="https://www.facebook.com/profile.php?id=61576137483701" target="_blank">
    <button style='font-size:20px;padding:10px 20px;border-radius:10px;background-color:#3e93d2;color:white;border:none;cursor:pointer; font-family: 'Arial', sans-serif;'>
        Visit Facebook Page
    </button>
</a>
""", unsafe_allow_html=True)

background_style = """
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20240329/pngtree-rows-of-dumbbells-in-the-gym-image_15662386.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0.5);
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.45); /* Adjust the 0.45 for more/less dim */
        z-index: 0;
    }
</style>
"""
st.markdown(background_style, unsafe_allow_html=True)
