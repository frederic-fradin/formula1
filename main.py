import streamlit as st
import pandas as pd
from datetime import datetime

from src import load_races

today = datetime.today()
current_year = today.year

# Page configuration
st.set_page_config(
    page_title="Formula 1",
    page_icon="🏎️",
    layout = 'wide'
    )


# Page header
col1, col2, col3 = st.columns([0.55, 0.10, 0.35])
col1.title("Formula 1 World Championship (1950 - 2024)")
col3.image('./reports/figures/enzo_ferrari.jpg')
col1.write('"Races are won at the track. Championships are won at the factory." - Mercedes (2019)')

# Data
races = load_races()
races['status'] = races.apply(lambda row: '🏁' if row['date'] < today else '📆', axis=1)
races['date'] = pd.to_datetime(races['date']).dt.date

select_col = ['round', 'name', 'location', 'country', 'date', 'time',
              'quali_date', 'quali_time', 'fp2_date', 'fp2_time', 'fp1_date', 'fp1_time', 'url_c']

# Filter dataframe
total_df = races[(races['year'] == current_year)].copy()
upcoming_df = races[(races['year'] == current_year) & (races['status'] == '📆')].copy()
previous_df = races[(races['year'] == current_year) & (races['status'] == '🏁')].copy()

# Dataframe per status of race
st.subheader(f'Season {current_year}')
st.write('')
st.markdown("📆 Upcoming races")
st.dataframe(upcoming_df[select_col].sort_values('date', ascending=True),
                column_config={"url_c": st.column_config.LinkColumn("circuit", display_text="View")},
                hide_index=True,use_container_width=True)

st.write('')
st.markdown("🏁 Previous races")
st.dataframe(previous_df[select_col].sort_values('date', ascending=False),
                column_config={"url_c": st.column_config.LinkColumn("circuit", display_text="View")},
                hide_index=True,use_container_width=True)