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
    fig = make_subplots(rows=2, cols=1, subplot_titles=("total points per season", "mean points per race"),
                        row_heights=[0.6,0.4], shared_xaxes=True, vertical_spacing = 0.10)

    temp = pd.pivot_table(data=constructor_standing, index=['year', 'name'], values=['points', 'round'], aggfunc='max').reset_index()
    temp['mean'] = temp.apply(lambda row: row['points'] / row['round'] if row['round'] !=0 else 0, axis=1)

    col1 = 0
    for ser1 in temp['name'].unique():
        selection = temp[temp['name'] == ser1].copy()
        
        fig.add_trace(go.Scatter(x=selection['year'], y=selection['points'],
                                 name=ser1), row=1, col=1)
    
        fig.add_trace(go.Scatter(x=selection['year'], y=selection['mean'],
                                showlegend = False), row=2, col=1)
    
    fig.update_layout(height=740, width=1300, title_text="Constructors (after 2010)")
    
    return fig, temp

def constructor_world_champion(constructor_standing):
    temp = pd.pivot_table(data=constructor_standing, index=['year', 'name'], values=['points'], aggfunc='max').reset_index()
    
    champion = temp.loc[temp.groupby('year')['points'].idxmax()]

    fig = px.bar(champion, x="year", y="points", color="name", title="Long-Form Input")
    
    fig.update_layout(height=740, width=1300, title_text="Constructors (after 2010)")

    return fig, champion
