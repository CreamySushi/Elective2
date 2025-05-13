def sidebar_styles():
    return """
    <style>
    div.stButton > button {
        font-size: 14px;
        font-weight: 400;
        color: white;
        background-color: transparent;
        border: none;
        padding: 0;
        text-align: left;
    }
    }
    </style>
    """
def hide_streamlit_style():
    return """
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

def background_main():
    return """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://t3.ftcdn.net/jpg/04/29/35/62/360_F_429356296_CVQ5LkC6Pl55kUNLqLisVKgTw9vjyif1.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0.5);
    }
    </style>
    """