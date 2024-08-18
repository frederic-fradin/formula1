import streamlit as st
import pandas as pd
import plotly.express as px

from src import load_pitstop

st.subheader('Pit stop analysis')
st.write('Data before 2024-07-15')

tab1, tab2, tab3 = st.tabs(['World Champions', 'Team statistics', '...'])

pit, races = load_pitstop()


col1, col2, col3 = tab2.columns([0.2,0.4,0.2])
year = col1.selectbox('Season', options=races['year'].unique(), label_visibility='collapsed')
circuit = col2.selectbox('Circuit', options=races['name'].unique(), label_visibility='collapsed')
validate = col3.button('SHOW DATA', use_container_width=True)

with tab2:
    if validate:
        temp = pit[(pit['year'] == year) & (pit['name'] == circuit)].copy()
        temp['lap'] = temp['lap'].astype(int)

        pvt = pd.pivot_table(data=temp, index=['lap', 'name_c'],
                            values=['milliseconds'], aggfunc='mean').reset_index()

        fig = px.scatter(data_frame=pvt, x='lap', y='milliseconds', color='name_c')

        pvt2 = pd.pivot_table(data=temp, index=['name_c'],
                            values=['milliseconds', 'stop'],
                            aggfunc={'milliseconds':'sum', 'stop':'max'}).reset_index()
        
        pvt2['mean'] = pvt2.apply(lambda row: row['milliseconds'] / 1000 / row['stop'] if row['stop'] !=0 else 0, axis=1)
        pvt2['mean'] = pvt2['mean'].round(2)
        pvt2_min = pvt2['mean'].min()
        pvt2_max = pvt2['mean'].max()

        fig2 = px.bar(data_frame=pvt2.sort_values('mean'), x='name_c', y='mean', range_y=[pvt2_min-5, pvt2_max+5], text='mean')

        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
        st.dataframe(temp, use_container_width=True)