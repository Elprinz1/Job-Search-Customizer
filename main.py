import streamlit as st
from PIL import Image


st.set_page_config(page_title="Project Solomon Gets a Job", layout="wide")

image = Image.open('./images/profile_pix.jpg')


# Use local CSS to manipulate Streamlit default styles
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: 550;
    }
    .info-text {
        font-size:20px !important;
    }
    .python-code {
        background: #000;
        color: #eee;
        padding: 10px;
        border-radius: 10px;
        overflow-x: auto;
    }
    img {
        border-radius: 50%;
    }
    </style>
    """, unsafe_allow_html=True)

# Custom layout with columns
col1, col2 = st.columns(2)

# First column for profile image and quick links
with col1:
    st.image(image, width=280)  # replace with the path to the image
    st.markdown('### Hi, I’m Princewill', unsafe_allow_html=True)
    st.markdown('<div class="info-text">Data Scientist | Process Engineer </div>',
                unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    col4.button("Email", use_container_width=True)
    col5.button("Resume", use_container_width=True)
    col6.button("LinkedIn", use_container_width=True)

# Second column for python code display
with col2:
    st.markdown("""
    ```python
    class AboutPrincewill:
        def __init__(self):
            self.occupation = 'Data Scientist | Process Engineer'
            self.skills = (
                'Python',
                'Machine Learning',
                'A/B testing',
                'Generative AI',
                'Project Management'
            )
            self.hobbies = (
                '⚽️ Playing Soccer',
                '🛫 Travelling'
            )
            self.current_favorite_music_artists = (
                'Dierk Bentley',
                'Eric Church',
                'Maroon 5',
            )
            self.fun_fact = 'Arsenal FC Fan'
    ```
    """, unsafe_allow_html=True)

    # Add more Streamlit components or custom HTML/CSS as needed for your content
