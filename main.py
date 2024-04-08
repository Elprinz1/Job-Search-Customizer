import streamlit as st
from PIL import Image
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from utils import *
from classes import *


st.set_page_config(page_title="Gen AI Projects", layout="wide")
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
        margin-bottom: 0.5em;
    }
    .python-code {
        background: #000;
        color: #eee;
        padding: 10px;
        border-radius: 10px;
        overflow-x: auto;
    }
    .button {
            border-radius: 10px;
            border: 1px solid #fff;
            padding: 0.5em;
            font: inherit;
            cursor: pointer;
            text-decoration: underline;
            color: black;
            width: 100%;
            text-decoration: none;

    }
    a {
            text-decoration: none;
    }
    img {
        border-radius: 50%;
    }
    .description {
            font-size: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# st.write('----')
# Custom layout with columns
col1, col2 = st.columns(2)

# First column for profile image and quick links
with col1:
    st.image(image, width=280)  # replace with the path to the image
    st.markdown('### Hi, I’m Princewill', unsafe_allow_html=True)
    st.markdown('<div class="info-text">Data Scientist | Process Engineer </div>',
                unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    col4.markdown(
        '<a href="mailto:princewill.egbujor@gmail.com"><button class="button">Email</button></a>', unsafe_allow_html=True)

    col5.markdown(
        '<a href="https://www.linkedin.com/in/princewillegbujor/"><button class="button">LinkedIn</button></a>', unsafe_allow_html=True)
    col6.markdown(
        '<a href="https://elprinz1.github.io/portfolio-website/"><button class="button">Portfolio</button></a>', unsafe_allow_html=True)

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

st.write('---')


# GEN AI - JOB SEARCH CUSTOMIZER
row2_1, row2_2, row2_3 = st.columns([1, 4, 1])

with row2_2:

    st.title("🔍 Gen AI Job Search Customizer & Analytics")
    st.markdown('<p class="description">Scrapes jobs from LinkedIn, Glassdoor, Indeed, and ZipRecruiter.</p>',
                unsafe_allow_html=True)

    site_name = ["indeed", "linkedin", "zip_recruiter", "glassdoor"]
    country = 'USA'
    date_posted = 24

    # Using a single column layout for a cleaner look, with spacers for better alignment
    st.write("---")  # Adding a horizontal line for visual separation

    col1, col2, col3 = st.columns(3)

    with col1:
        search_term = st.text_input(
            "Job Title", "", placeholder="Enter job title")

    with col2:
        location = st.text_input(
            "Location", "", placeholder="Enter job location")

    with col3:
        results_wanted = st.number_input("Results", min_value=1, value=20)

    st.write("---")

    if st.button("Scrape Jobs", help="Click to start scraping jobs based on your criteria"):
        if search_term:
            with st.spinner('Scraping job listings...'):
                st.session_state.jobs = get_jobs(
                    site_name, search_term, location, results_wanted, date_posted, country)
        else:
            st.warning("Please enter a job title to start scraping jobs.")

    columns = ['site', 'job_url', 'title', 'description', 'company',
               'location', 'date_posted', 'min_amount', 'max_amount', 'emails']

    with st.expander("DataFrame Preview"):
        if 'jobs' in st.session_state and not st.session_state.jobs.empty:
            st.dataframe(st.session_state.jobs[columns])
        else:
            st.info("No data available. Please scrape jobs first.")

    st.subheader(f"🔎 Let's Query the Job Search Dataframe")
    query = st.text_area("🗣️ Chat with Data, Example 'Show me a bar graph grouping jobs by location'",
                         placeholder="Ask something about the job data...")

    if query and 'jobs' in st.session_state:
        llm = OpenAI(api_token=os.environ.get('OPENAI_KEY'))
        query_engine = SmartDataframe(
            st.session_state.jobs,
            config={
                "llm": llm,
                "response_parser": StreamlitResponse,
            },
        )

        answer = query_engine.chat(query)
        st.write(answer)

st.write('----')
