import fastf1
import streamlit as st
from datetime import timedelta

fastf1.Cache.enable_cache('./data/cache')

# st.cache_data(ttl=timedelta(days=1))
def f1_get_session(season, racenumber, session):

    session = fastf1.get_session(season, racenumber, session)
    st.toast(f'{session} initialized', icon=":material/sports_motorsports:")

    return session

# st.cache_data(ttl=timedelta(days=1))
def f1_get_event_schedule(season, testing):

    schedule = fastf1.get_event_schedule(season, include_testing=testing)
    st.toast(f'Season {season} events initialized', icon=":material/sports_motorsports:")

    return schedule