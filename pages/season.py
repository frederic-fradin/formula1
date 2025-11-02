import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import datetime as dt

from module.season import load_season_calendar, load_gp_detail

list_season = [str(x) for x in range(2020, 2026, 1)]

# Page header
st.header('Season calendar', divider="red")

sel_season = st.segmented_control(label="Select a season",
                options=list_season,
                default=None,
                key='sel_season',
                selection_mode="single",
                label_visibility="hidden",
                width="stretch"
                )

st.space("small")

col21, col22, col23 = st.columns([0.55, 0.05, 0.40])

if sel_season is not None:
    overview = load_season_calendar(int(sel_season))
    
    col21.caption('_Select a GP for more details_')
    overview['EventDate'] = pd.to_datetime(overview['EventDate']).dt.date
    sel_gp = col21.dataframe(overview,
                    height="auto",
                    selection_mode="single-row",
                    on_select="rerun")

    if len(sel_gp['selection']["rows"]) !=0:
        id_gp = sel_gp['selection']["rows"][0]
        
        try:
            gp_detail = load_gp_detail(id_gp)
        except Exception as e:
            gp_detail = {}
        
        try:
            col23.write(f'**{gp_detail["Location"]}**')
            col23.image(f'./assets/figures/circuit_{gp_detail['Location']}.png')
        except Exception as e:
            col23.write("Circuit overview not available")
        
        col23.write("")
        with col23.expander("See details"):
            st.write(gp_detail)