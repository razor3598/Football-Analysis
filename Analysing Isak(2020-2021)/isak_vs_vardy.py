# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:03:29 2021

@author: Amod
"""

import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
player_data = pd.read_excel("isak_vs_vardy.xlsx")
player_data.set_index('Player',inplace = True)
params = list(player_data.columns)
 
#Getting the ranges to plot the radar chart
ranges = []
a_values = []
b_values = []

for x in params:
    a = min(player_data[params][x])
    a = a - (a*1.0)
    
    b = max(player_data[params][x])
    b = b + (b*1.0)
    
    ranges.append((a,b))
    
#Getting player stats- values
values=[]
for idx,_ in player_data.iterrows():
        values.append(player_data.loc[idx].values.tolist())

#Assigning title to the plot
title = dict(
    title_name='Jamie Vardy',
    title_color = 'blue',
    title_name_2 = 'Alexander Isak',
    title_color_2 = 'Red',
    title_fontsize = 18
    )
endnote = '@amod\ndata via FBREF / Statsbomb'

#Potting the radar chart
radar = Radar()
fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                             radar_color=['blue','red'],
                             alphas=[.5,.7],endnote=endnote,title=title,
                             compare=True)

