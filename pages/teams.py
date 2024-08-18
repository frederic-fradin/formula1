import streamlit as st

from src import load_constructors_perf, constructor_chart, constructor_world_champion

st.subheader('Teams performance')
st.write('Data before 2024-07-15')

tab1, tab2, tab3 = st.tabs(['World Champions', 'Team statistics', 'Teams'])

constructor_standing, constructors = load_constructors_perf()
fig, champion = constructor_world_champion(constructor_standing)

tab1.plotly_chart(fig)
tab1.dataframe(champion, hide_index=True,use_container_width=True)


col1, col2 = tab2.columns([0.8,0.2])
constructor = col1.multiselect('Constructors', options=constructors['name'].unique(), label_visibility='collapsed')
validate = col2.button('SHOW DATA', use_container_width=True)

if validate:
    constructor_standing2, constructors2 = load_constructors_perf(selection=constructor)
    fig1, fig2, selection = constructor_chart(constructor_standing2)
    tab2.plotly_chart(fig1)
    tab2.plotly_chart(fig2)
    tab2.dataframe(selection, hide_index=True,use_container_width=True)

tab3.dataframe(constructors, hide_index=True,use_container_width=True,
               column_config={"url": st.column_config.LinkColumn("constrcutor", display_text="View")},)

