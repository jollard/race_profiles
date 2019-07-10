import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.iplot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
})

"""from pandas.io.json import json_normalize
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly 
get_ipython().run_line_magic('matplotlib', 'inline')

race_dict = [{'race_id':'173054258','race_name':'Dublin City Marathon','race_year':2018,'race_country':'Ireland','race_type':'Marathon'},
            {'race_id':'2247306','race_name':'Cork City Marathon','race_year':2018,'race_country':'Ireland','race_type':'Marathon'},
            {'race_id':'12389632','race_name':'Limerick City Marathon','race_year':2018,'race_country':'Ireland','race_type':'Marathon'},
            {'race_id':'308430','race_name':'Galway City Marathon','race_year':2018,'race_country':'Ireland','race_type':'Marathon'}]
df = pd.DataFrame()
for race in race_dict:
    response = requests.get('https://www.mapmyrun.com/routes/view/elevation/'+race['race_id']+'/?datatype=json').json()
    df_temp = pd.DataFrame.from_dict(json_normalize(response), orient='columns')
    df_temp['race_id'] = race['race_id']
    df_temp['race_name'] = race['race_name']
    df_temp['race_year'] = race['race_year']
    df_temp['race_country'] = race['race_country']
    df = df.append(df_temp)

data = []
for race in race_dict:
    trace = go.Scatter(x=df.loc[df.race_id == race['race_id'],'distance'].values,
                       y=df.loc[df.race_id == race['race_id'],'elevation'].values,
                       name=race['race_name'])
    data.append(trace)
    
layout = go.Layout(
    title=go.layout.Title(
        text='Race Elevation [m]',
        xref='paper',
        x=0),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Distance [m]',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f')
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='Elevation [m]',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f')
        )
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='basic-area-no-bound')
"""



