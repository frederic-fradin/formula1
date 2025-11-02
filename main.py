import streamlit as st

# Page configuration
st.set_page_config(page_title="Formula 1", page_icon="🏎️", layout="wide")

# Adjust top padding
st.markdown(
    """
            <style>
                    .block-container {
                        padding-top: 4rem;
                        padding-bottom: 4rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
            </style>
            """,
    unsafe_allow_html=True,
)

if 'my_season' not in st.session_state:
    st.session_state.my_season = 0

if 'last_round' not in st.session_state:
    st.session_state.last_round = 0

pages = {
    "Home": [
        st.Page("./pages/home.py", title="Home"),
        st.Page("./pages/season.py", title="Calendar"),
    ],
    "Results": [
        st.Page("./pages/races.py", title="Race results"),
        st.Page("./pages/drivers.py", title="Driver standings"),
        st.Page("./pages/teams.py", title="Team standings"),
    ],
    "Analysis": [
        st.Page("./pages/stand.py", title="Stand analysis"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()