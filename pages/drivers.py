import streamlit as st

from src import load_drivers_perf, driver_world_champion, driver_chart

st.subheader('Drivers performance')
st.write('Data before 2024-07-15')

tab1, tab2, tab3 = st.tabs(['World Champions', 'Driver statistics', 'Drivers'])

driver_standing, drivers = load_drivers_perf()
fig1, fig2, champion = driver_world_champion(driver_standing)

tab1.plotly_chart(fig1)
tab1.plotly_chart(fig2)
tab1.dataframe(champion, hide_index=True,use_container_width=True)

col1, col2 = tab2.columns([0.8,0.2])
driver = col1.multiselect('Drivers', options=drivers['surname'].unique(), label_visibility='collapsed')
validate = col2.button('SHOW DATA', use_container_width=True)

if validate:
    driver_standing2, drivers2 = load_drivers_perf(selection=driver)
    fig1a, fig2a, selection = driver_chart(driver_standing2)
    tab2.plotly_chart(fig1a)
    tab2.plotly_chart(fig2a)
    tab2.dataframe(selection, hide_index=True,use_container_width=True)

tab3.dataframe(drivers, hide_index=True,use_container_width=True,
               column_config={"url": st.column_config.LinkColumn("driver", display_text="View")},)