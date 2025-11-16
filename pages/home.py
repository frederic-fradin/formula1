import fastf1
import streamlit as st
from datetime import datetime

from module.season import load_next_schedule

today = datetime.today()
current_year = today.year

st.subheader(f"Formula 1 - Season {current_year}", divider="red", anchor=False)
st.write('"Races are won at the track. Championships are won at the factory" Mercedes (2019)')
st.space("small")

list_season = [str(x) for x in range(2020, 2026, 1)]

season_selection = st.sidebar.selectbox(label="Season", options=list_season, index=None, key='default_season')

if season_selection:
    st.session_state.my_season = int(season_selection)

st.sidebar.write('')

if st.sidebar.button('Show cash', width='stretch'):
    cache_info = fastf1.Cache.get_cache_info()
    st.sidebar.write(cache_info)

if st.sidebar.button('Clear cache', width='stretch'):
    fastf1.Cache.clear_cache()

col11, col12, col13, col14 = st.columns([0.20, 0.40, 0.20, 0.20])

schedule_program = load_next_schedule(current_year)

col11.subheader(":grey[_Previous_]", anchor=False)
col11.image('./assets/figures/previous.jpg')
col11.caption(f'{schedule_program['previous_race']}')

col12.subheader(":red[**Next**]", anchor=False)
col12.image('./assets/figures/next.jpg')
col12.header(f"**:red[{schedule_program['next_race']}]**", anchor=False)
col12.badge(f'{schedule_program['next_date']}', color="red")
col12.caption(f'Round : {schedule_program['next_round']}')

col13.subheader(":grey[_Upcoming_]", anchor=False)
col13.image('./assets/figures/upcoming1.jpg')
col13.caption(f'{schedule_program['upcoming_1']}')

col14.subheader(":grey[_..._]", anchor=False)
col14.image('./assets/figures/upcoming2.jpg')
col14.caption(f'{schedule_program['upcoming_2']}')