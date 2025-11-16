import streamlit as st
from pathlib import Path

from module.standings import load_drivers_standings, load_teams_standings

# Get the current file's path and parent
current_file = Path(__file__)
current_folder = current_file.parent
parent_folder = current_file.parent.parent

st.subheader(f'Season {st.session_state.my_season}', anchor=False)

tab1, tab2, tab3 = st.tabs(['Driver standings', 'Team standings', '...'])

with tab1:
    tab11, tab12, tab13 = st.columns([0.75, 0.05, 0.2])

    fig = load_drivers_standings(st.session_state.my_season)
    st.toast('Driver standings loaded', icon=":material/sports_score:")
    tab11.plotly_chart(fig, width="stretch")
    tab13.space("large")
    tab13.image(f'{parent_folder}/assets/figures/pilote.jpg')

with tab2:
    tab21, tab22, tab23 = st.columns([0.75, 0.05, 0.2])
    
    fig = load_teams_standings(st.session_state.my_season)
    st.toast('Team standing loaded', icon=":material/sports_score:")
    tab21.plotly_chart(fig, width="stretch")
    tab23.space("large")
    tab23.image(f'{parent_folder}/assets/figures/team.jpg')