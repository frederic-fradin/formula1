import streamlit as st
import pandas as pd
from datetime import timedelta

from module.fastf1 import f1_get_session

st.cache_data(ttl=timedelta(days=1))
def load_race_result(gp_id:int, session:str="R"):
    # Initialisation de la course
    session = f1_get_session(st.session_state.my_season, int(gp_id) + 1, session)
   
    session.load()
    result = session.results

    for col in ['Q1', 'Q2', 'Q3']:
        result[col] = result[col].apply(
                lambda x: f"{int(x.total_seconds() // 60):02d}:{x.total_seconds() % 60:06.3f}"
                    if pd.notna(x) else None
            )

    return result