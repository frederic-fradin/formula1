import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

pio.templates.default = "plotly_white"
color_pal1 = ['#59733F','#D99982','#F2B33D','#BF7B6B','#4A868C','#2C3740',
              '#BF544B','#A68877','#8C8B77','#F2B33D','#8C8C8C','#A3A651']
color_pal2 = ['#735439','#A7BF8F','#F2D5C4','#468AD8']

def constructor_chart(constructor_standing):
    temp = pd.pivot_table(data=constructor_standing, index=['year', 'name'], values=['points', 'round'], aggfunc='max').reset_index()
    temp['mean'] = temp.apply(lambda row: row['points'] / row['round'] if row['round'] !=0 else 0, axis=1)

    fig1 = px.line(data_frame=temp, x='year', y='points', color='name', title='Points per season', markers=True)
    fig2 = px.line(data_frame=temp, x='year', y='mean', color='name', title='Mean points per race', markers=True)
    
    return fig1, fig2, temp

def constructor_world_champion(constructor_standing):
    temp = pd.pivot_table(data=constructor_standing, index=['year', 'name'], values=['points'], aggfunc='max').reset_index()
    champion = temp.loc[temp.groupby('year')['points'].idxmax()]

    fig = px.bar(champion, x="year", y="points", color="name", title="World Champion")

    return fig, champion

def driver_chart(driver_standing):
    temp = pd.pivot_table(data=driver_standing, index=['year', 'surname'], values=['points', 'round'], aggfunc='max').reset_index()
    temp['mean'] = temp.apply(lambda row: row['points'] / row['round'] if row['round'] !=0 else 0, axis=1)

    fig1 = px.line(data_frame=temp, x='year', y='points', color='surname', title='Points per season', markers=True)
    fig2 = px.line(data_frame=temp, x='year', y='mean', color='surname', title='Mean points per race', markers=True)
    
    return fig1, fig2, temp

def driver_world_champion(driver_standing):
    temp = pd.pivot_table(data=driver_standing, index=['year', 'surname'], values=['points'], aggfunc='max').reset_index()
    champion = temp.loc[temp.groupby('year')['points'].idxmax()]

    fig1 = px.bar(champion, x="year", y="points", color="surname", title="Championship (after 2000)")

    temp2 = pd.pivot_table(data=temp, index=['surname'], values=['points'], aggfunc='sum').reset_index()
    temp2 = temp2[temp2['points'] > 100].sort_values('points', ascending=False)
    fig2 = px.bar(temp2, x="surname", y="points", text='points', title="Drivers with more than 100 points")

    return fig1, fig2, champion
