def sidebar_styles():
    return """
    <style>
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.5); 
        backdrop-filter: blur(10px);
    }
    </style>
    """

def hide_streamlit_style():
    return """
    <style>
    footer {
        visibility: hidden;
    }

    footer:after {
        content: "";
        visibility: hidden;
    }

    
    MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }
    </style>
    """


def text_outline_styles():
    return """
    <style>

    h1, h2, h3, h4, h5, h6,
    p, span, div, label {
        color: white !important;
        text-shadow:
            -1px -1px 0 #000,  
             1px -1px 0 #000,
            -1px  1px 0 #000,
             1px  1px 0 #000;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """

def side_bar_button_style():
    return """
    <style>
    section[data-testid="stSidebar"] div.stButton > button {
        background-color: transparent;
        text-weight: Bold;
        font-size: 30px;
        padding-right: 20px;
        border-radius: 10px;
        border: none !important;
        cursor: pointer;
        font-family: inherit !important;
        hover: {
            background-color: rgba(255, 255, 255, 0.2);
        }
    }
    """