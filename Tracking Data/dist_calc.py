# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:28:21 2021

@author: Amod
"""

import Metrica_IO as mio
import numpy as np
import matplotlib.pyplot as plt

# set up initial path to data
DATADIR = 'D:/Football Analysis/sample-data-master/sample-data-master/data'
game_id = 2 # let's look at sample match 2

tracking_home = mio.tracking_data(DATADIR,game_id,'Home')
tracking_away = mio.tracking_data(DATADIR,game_id,'Away')

tracking_home = mio.to_metric_coordinates(tracking_home)
tracking_away = mio.to_metric_coordinates(tracking_away)

#Calculating distance ran by players
print("HOME TEAM")
print("***Distance run by the player(in km)***")
print("Number     Distance")
home_distances=[]
home_kit = []
for i in range(1,15):
    tracking_home['v_x_{}'.format(i)] = (tracking_home[['Home_{}_x'.format(i)]] - tracking_home[['Home_{}_x'.format(i)]].shift(1))**2 
    tracking_home['v_y_{}'.format(i)] = (tracking_home[['Home_{}_y'.format(i)]] - tracking_home[['Home_{}_y'.format(i)]].shift(1))**2 
    
    
    tracking_home['Distance_{}'.format(i)] = np.sqrt(tracking_home['v_x_{}'.format(i)] + tracking_home['v_y_{}'.format(i)])
    tracking_home.drop(['v_x_{}'.format(i), 'v_y_{}'.format(i)], axis=1)
    dist = tracking_home['Distance_{}'.format(i)].dropna().sum()/1000
    print(i,"       ",dist)
    home_kit.append(i)
    home_distances.append(dist)
    
#Calculating distance ran by players
print("AWAY TEAM")
print("***Distance run by the player(in km)***")
print("Number     Distance")
away_distances=[]
away_kit = []
for i in range(15,26):
    tracking_away['v_x_{}'.format(i)] = (tracking_away[['Away_{}_x'.format(i)]] - tracking_away[['Away_{}_x'.format(i)]].shift(1))**2 
    tracking_away['v_y_{}'.format(i)] = (tracking_away[['Away_{}_y'.format(i)]] - tracking_away[['Away_{}_y'.format(i)]].shift(1))**2 
    
    
    tracking_away['Distance_{}'.format(i)] = np.sqrt(tracking_away['v_x_{}'.format(i)] + tracking_away['v_y_{}'.format(i)])
    tracking_away.drop(['v_x_{}'.format(i), 'v_y_{}'.format(i)], axis=1)
    dist = tracking_away['Distance_{}'.format(i)].dropna().sum()/1000
    print(i,"       ",dist)
    away_kit.append(i)
    away_distances.append(dist)

#Plotting bar charts    
fig,(ax) = plt.subplots()
ax.bar(home_kit,home_distances,width=0.5)
ax.set_ylabel("Distance in km")
ax.set_xlabel("Player")
ax.set_title("Distance ran by each player - HOME")
plt.show()

fig,(ax) = plt.subplots()
ax.bar(away_kit,away_distances,width=0.5)
ax.set_ylabel("Distance in km")
ax.set_xlabel("Player")
ax.set_title("Distance ran by each player - AWAY")
plt.show()