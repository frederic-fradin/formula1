import streamlit as st
from module.standings import load_drivers_standings

st.subheader('Drivers performance', anchor=False)

tab1, tab2, tab3 = st.tabs(['Standings', 'Statistics', 'Drivers'])

with tab1:
    fig = load_drivers_standings(st.session_state.my_season)
    st.plotly_chart(fig, width="stretch")