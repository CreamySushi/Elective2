import streamlit as st
from utils.styles import sidebar_styles, text_outline_styles, hide_streamlit_style
st.markdown(sidebar_styles(), unsafe_allow_html=True)
st.markdown(text_outline_styles(), unsafe_allow_html=True)
st.markdown(hide_streamlit_style(), unsafe_allow_html=True)


st.markdown("""
    <div style="color: white; text-align: justify; width: 90%; margin: auto; padding: 20px;font-size: 15px;">
        <br><br><br><br><br><br><br><br>
        <p>
        Welcome to <strong>CALORIE BURN PREDICTOR</strong> — where smart tech meets your fitness goals!
        We know that juggling classes, assignments, and social life can make staying healthy feel like an uphill battle. That’s why we’re here to make fitness easier, smarter, and way more personal.
        <br><br>
        Let’s face it — tracking calories and managing weight isn’t always straightforward. Most apps just toss out random estimates that don’t really fit you. That’s where we come in.
        Our platform uses powerful machine learning (don’t worry, we made it simple!) to give you accurate calorie burn predictions based on your unique stats — like age, height, weight, gender, and the type of activity you’re doing.
        <br><br>
        Behind the scenes, our tech runs on the XGBoost algorithm (basically, one of the smartest ways to crunch numbers fast), so you get real-time, precise info to help you manage your fitness and hit your goals — whether it’s getting stronger, staying in shape, or just feeling good.
        <br><br>
        This project was proudly developed by Third Year Students, Computer Engineering (CPE3A) from the University of Perpetual Help System, Laguna as a practical application to help users track their calorie burn.
        By simply entering a few key personal details, our app accurately calculates the calories you burn during activities. Using advanced machine learning — specifically the XGBoost algorithm — we provide precise, individualized results to help you manage your fitness more effectively.
        <br><br>
        <strong>Our mission?</strong> To give you a tool that actually works for you — no guesswork, no gimmicks — just clear insights so you can take control of your health with confidence.
        <br><br>
        Stay sharp. Stay fit. Let’s do this together at <strong>CALORIE BURN PREDICTOR</strong>.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="color: white; text-align: justify; width: 90%; margin: auto; padding: 20px;font-size: 20px;">
        <h2>Meet the Team</h2>
        <ul>
            <li><strong>Recto Sean Rainer</strong> - Project Manager</li>
            <li><strong>Morando Mark Christian, Dionisio Ianara Nicole</strong> - Backend Developer</li>
            <li><strong>Quirante John Aaron Flavien, Recto Sean Rainer</strong> - Frontend Developer</li>
            <li><strong>Cabrera Marinella Princess</strong> - Data Scientist</li>
            <li><strong>Adanza Whea</strong> - Designer</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


background_style = """
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://scontent.fmnl16-1.fna.fbcdn.net/v/t1.15752-9/494574100_482301831577913_2737380950047677051_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=9f807c&_nc_ohc=sdanFUA__dcQ7kNvwH5i_DW&_nc_oc=Adm9LpUj0JwLrwEcvEA8sDfDK6infrTbODnQtM9pkB8tdTzN0X5KH5CkjAB7AaqPzdQ&_nc_zt=23&_nc_ht=scontent.fmnl16-1.fna&oh=03_Q7cD2QHlyeIOZ3u9kwf4JN5pGu98DOhxH8O_AJtE5klVQSP-iQ&oe=684ACE8F");
        background-size: cover;
        background-position: top;
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
    .about-section, .team-section {
    color: white;
    text-align: justify;
    width: 90%;
    margin: auto;
    padding: 20px;
    font-size: 15px;
}

.team-section h2 {
    font-size: 22px;
    margin-top: 30px;
}

@media screen and (max-width: 768px) {
    .about-section, .team-section {
        font-size: 13px;
        padding: 10px;
    }
    .team-section h2 {
        font-size: 18px;
        text-align: center;
    }
    ul {
        padding-left: 20px;
    }
}
</style>
"""
st.markdown(background_style, unsafe_allow_html=True)
