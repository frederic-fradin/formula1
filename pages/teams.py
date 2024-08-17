import streamlit as st

from src import load_constructors_perf, constructor_chart, constructor_world_champion

st.subheader('Teams performance')
st.write('Data before 2024-07-15')

tab1, tab2, tab3 = st.tabs(['World Champions', 'Team statistics', '...'])

constructor_standing, constructors = load_constructors_perf()

fig1, champion = constructor_world_champion(constructor_standing)
fig2, selection = constructor_chart(constructor_standing)

tab1.plotly_chart(fig1)
tab1.dataframe(champion, hide_index=True,use_container_width=True)

tab2.plotly_chart(fig2)
tab2.dataframe(selection, hide_index=True,use_container_width=True)

