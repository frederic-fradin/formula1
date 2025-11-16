import os
import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import timedelta, date

from module.fastf1 import f1_get_event_schedule, f1_get_session

# Get the current file's path and parent
current_file = Path(__file__)
current_folder = current_file.parent
parent_folder = current_file.parent.parent

st.cache_data(ttl=timedelta(days=1))
def load_next_schedule(season:int=2025):
   schedule = f1_get_event_schedule(2025, False)

   schedule['EventDate'] = pd.to_datetime(schedule['EventDate']).dt.date
   next_races = schedule[schedule['EventDate'] >= date.today()].copy()
   previous_races = schedule[schedule['EventDate'] < date.today()].copy()

   dict_schedule = {
      'previous_race' : str(previous_races.iloc[-1, 2]) + " - " + str(previous_races.iloc[-1, 1]),
      'previous_round' : previous_races.iloc[-1, 0],
      'next_round' : next_races.iloc[0, 0],
      'next_race' : str(next_races.iloc[0, 2]) + " - " + str(next_races.iloc[0, 1]),
      'next_date' : next_races.iloc[0, 4],
      'upcoming_1' : str(next_races.iloc[1, 2]) + " - " + str(next_races.iloc[1, 1]),
      'upcoming_2' : str(next_races.iloc[2, 2]) + " - " + str(next_races.iloc[2, 1]),
   }

   return dict_schedule

st.cache_data(ttl=timedelta(days=1))
def load_season_calendar(season:int=2025):

   if os.path.exists(f"{parent_folder}/data/season_{season}.parquet"):
      schedule = pd.read_parquet(f"{parent_folder}/data/season_{season}.parquet")
      # st.toast("Season loaded with success", icon=":material/done_outline:")
   else:
      schedule = f1_get_event_schedule(season, False)
      schedule = schedule[schedule['EventName'] != 'Pre-Season Testing']
      schedule.to_parquet(f"{parent_folder}/data/season_{season}.parquet")

   st.session_state['my_season'] = season

   season_overview = schedule[schedule['F1ApiSupport']][['RoundNumber', 'Country', 'Location', 'EventDate',
      'EventName']].set_index('RoundNumber')
   
   return season_overview

def load_gp_detail(gp_id:int):
   # Initialisation de la course
   race = f1_get_session(st.session_state.my_season, int(gp_id) + 1, 'R')
   
   race_info = ['RoundNumber', 'Location', 'EventDate', 'EventFormat',
            'Session1', 'Session1DateUtc', 'Session2', 'Session2DateUtc', 'Session3', 'Session3DateUtc',
            'Session4', 'Session4DateUtc', 'Session5', 'Session5DateUtc']

   dict_info = {}
   for info in race_info:
      dict_info[info] = race.event[info]
   
   return dict_info