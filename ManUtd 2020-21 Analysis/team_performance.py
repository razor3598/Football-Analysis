# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:44:35 2021

@author: Amod
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from soccerplots.radar_chart import Radar

#Load the data
team_data = pd.read_csv("Data/team_performance_2020_21.csv")

#Assigning colors to the team
colors={}
for x in team_data['Squad'].unique():
    colors[x]='blue'
    if x=="Manchester Utd":
        colors[x]='red'
        
#Scatter plot for team goals
fig, ax = plt.subplots(figsize=(28, 20))
ax.scatter(team_data['Gls'],team_data['xG'],c=team_data['Squad'].map(colors))

for i, txt in enumerate(team_data.Squad):
    ax.annotate(txt,(team_data['Gls'].iloc[i]-0.5,team_data['xG'].iloc[i]+0.5))
    
ax.set_xlabel("Goals scored",fontsize=14) 
ax.set_ylabel("xG - expected goals",fontsize=14)
ax.set_title("Comparision of goals scored and expected goals",fontsize=25)
plt.savefig('team_goals')
plt.show()

#Loading up team performance data
#----------------------------------------------------------
team_data = pd.read_excel("Data/general_performance.xlsx")
# Top 6 of the premier league
team_data = team_data[(team_data['Squad']=='Manchester City') | (team_data['Squad']=='Manchester Utd') | (team_data['Squad']=='Leicester City') |(team_data['Squad']=='Liverpool')| (team_data['Squad']=='Chelsea') | (team_data['Squad']=='West Ham')]
team_data.set_index('Squad',inplace = True)

#Generating a parameter list for our radar chart
params = list(team_data.columns)
params

#Generating ranges
ranges = []
a_values = []
b_values = []

for x in params:
    a = min(team_data[params][x])
    a = a - (a*.25)
    
    b = max(team_data[params][x])
    b = b + (b*.25)
    
    ranges.append((a,b))

#Plotting the radar chart from soccerplots - radar_chart 
for x in range(len(team_data)):
    values=[team_data.loc['Manchester Utd'].values.tolist()]

    temp = team_data.iloc[x].values.tolist()
    values.append(temp)
    
    title = dict(
    title_name='Manchester United',
    title_color = 'red',
    title_name_2 = team_data.index[x],
    title_color_2 = 'blue',
    title_fontsize = 18
    )

    endnote = '@amod\ndata via FBREF / Statsbomb'
    
    radar = Radar()
    
    fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                             radar_color=['red','blue'],
                             alphas=[.5,.5],endnote=endnote,title=title,
                             compare=True)
    
    values=[]
    

#Loading up United's 2019-20 season stats
mufc_2019 = pd.read_excel("Data/mufc_2019_20.xlsx")
mufc_2019.set_index('Squad',inplace = True) 
values=[team_data.loc['Manchester Utd'].values.tolist()]
values.append(mufc_2019.iloc[0].values.tolist())

# Plotting radar chart for 2019-20 vs 2020-21 season
title = dict(
    title_name='MUFC 2020-21',
    title_color = 'red',
    title_name_2 = 'MUFC 2019-20',
    title_color_2 = 'black',
    title_fontsize = 18
    )

endnote = '@amod\ndata via FBREF / Statsbomb'
    
    
fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                             radar_color=['red','black'],
                             alphas=[.5,.7],endnote=endnote,title=title,
                             compare=True)