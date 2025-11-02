import streamlit as st
from pathlib import Path

from module.season import load_season_calendar
from module.races import load_race_result

# Get the current file's path and parent
current_file = Path(__file__)
current_folder = current_file.parent
parent_folder = current_file.parent.parent

st.subheader('Races', anchor=False)

races = load_season_calendar()
races = races.reset_index()

sel_race = st.selectbox('Races', options=races['Country'].unique())

tab1, tab2, tab3, tab4 = st.tabs(['Race Result', 'Qualifying', 'Practices', 'Pit Stop'])

with tab1:
    st.space("small")
    tab11, tab12, tab13 = st.columns([0.75, 0.05, 0.2])

    if sel_race:
        race_id = races[races['Country'] == sel_race].iloc[0, 0]
        race_result = load_race_result(gp_id=(race_id-1), session="R")
        
        tab13.image(f'{parent_folder}/assets/figures/race.jpg')

        col_data = ['HeadshotUrl', 'DriverNumber', 'FullName', 'Points',
                'Position', 'ClassifiedPosition', 'TeamName', 'Status', 'GridPosition']
        
        tab11.dataframe(race_result[col_data], width="stretch", hide_index=True,
                        column_config={
                            "HeadshotUrl": st.column_config.ImageColumn(),
                            "Points": st.column_config.ProgressColumn(format="plain", max_value=25)
                            }
                        )

with tab2:
    st.space("small")
    tab11, tab12, tab13 = st.columns([0.75, 0.05, 0.2])

    if sel_race:
        race_id = races[races['Country'] == sel_race].iloc[0, 0]
        race_result = load_race_result(gp_id=(race_id-1), session="Q")
        
        tab13.image(f'{parent_folder}/assets/figures/qualifying.jpg')

        col_data = ['HeadshotUrl', 'DriverNumber', 'FullName', 'Position',
                    'Q1', 'Q2', 'Q3', 'TeamName']
        
        tab11.dataframe(race_result[col_data], width="stretch", hide_index=True,
                        column_config={
                            "HeadshotUrl": st.column_config.ImageColumn(),
                            "Points": st.column_config.ProgressColumn(format="plain", max_value=25)
                            }
                        )

with tab3:
    st.space("small")
    tab11, tab12, tab13 = st.columns([0.75, 0.05, 0.2])

    if sel_race:
        race_id = races[races['Country'] == sel_race].iloc[0, 0]
        # race_result = load_race_result(gp_id=(race_id-1), session="P3")
        
        tab13.image(f'{parent_folder}/assets/figures/practice.jpg')

        # col_data = ['HeadshotUrl', 'DriverNumber', 'FullName', 'Position',
        #             'Q1', 'Q2', 'Q3', 'TeamName']
        
        # tab11.dataframe(race_result[col_data], width="stretch", hide_index=True,
        #                 column_config={
        #                     "HeadshotUrl": st.column_config.ImageColumn(),
        #                     "Points": st.column_config.ProgressColumn(format="plain", max_value=25)
        #                     }
        #                 )


with tab4:
    st.space("small")
    tab11, tab12, tab13 = st.columns([0.75, 0.05, 0.2])

    if sel_race:
        race_id = races[races['Country'] == sel_race].iloc[0, 0]
        # race_result = load_race_result(gp_id=(race_id-1), session="P3")
        
        tab13.image(f'{parent_folder}/assets/figures/pitstop.jpg')

        # col_data = ['HeadshotUrl', 'DriverNumber', 'FullName', 'Position',
        #             'Q1', 'Q2', 'Q3', 'TeamName']
        
        # tab11.dataframe(race_result[col_data], width="stretch", hide_index=True,
        #                 column_config={
        #                     "HeadshotUrl": st.column_config.ImageColumn(),
        #                     "Points": st.column_config.ProgressColumn(format="plain", max_value=25)
        #                     }
        #                 )