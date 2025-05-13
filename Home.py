import streamlit as st

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Calorie Burn Predictor", page_icon="calories.ico", initial_sidebar_state="collapsed", layout="wide")

from views.login import Show_Login_Screen
from views.signup import Show_Sign_Up_Screen
from views.forgot_password import Show_Forgot_Password_Screen
from views.main_app import Show_Main_Screen
from utils.init import setup_session_state, initialize_database, Show_Splash_Screen
from utils.styles import sidebar_styles, hide_streamlit_style,text_outline_styles


setup_session_state()
initialize_database()

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
st.markdown(hide_streamlit_style(), unsafe_allow_html=True)
st.markdown(sidebar_styles(), unsafe_allow_html=True)

if not st.session_state.splash_shown:
    Show_Splash_Screen()
    st.session_state.splash_shown = True
    st.rerun()

if st.session_state.logged_in:
    with st.sidebar:
        st.markdown(
            f"""
            <div style="font-size: 25px; font-weight: 500; padding: 0.5rem 0; color: white;">
                Welcome, {st.session_state.username}
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("--------", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Refresh"):
            st.rerun()

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state.admin = False
            st.rerun()

    Show_Main_Screen()
else:
    if st.session_state.forgot_password:
        Show_Forgot_Password_Screen()
    elif st.session_state.show_signup:
        Show_Sign_Up_Screen()
    else:
        Show_Login_Screen()