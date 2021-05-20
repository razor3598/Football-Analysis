# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:19:43 2021

@author: Amod
"""

import matplotlib.pyplot as plt
import numpy as np
from FCPython import createPitch
import matplotlib.patches as mpatches

#Size of the pitch in yards
pitchLengthX=120
pitchWidthY=80

match_id_required = 7576
home_team_required ="Portugal"
away_team_required ="Spain"

file_name=str(match_id_required)+'.json'

#Load in all match events 
import json
with open('D:/Football Analysis/SoccermaticsForPython-master/Statsbomb/data/data/events/'+file_name) as data_file:
    data = json.load(data_file)

#get the nested structure into a dataframe 
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

shots = df.loc[df['type_name']=='Shot'].set_index('id')
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

player = 'Cristiano Ronaldo dos Santos Aveiro'

for i,shot in shots.iterrows():
    if shot['player_name']==player:
        x = shot['location'][0]
        y = shot['location'][1]
    
        circleSize = np.sqrt(shot['shot_statsbomb_xg'])*3
        if shot['shot_type_name']=='Penalty':
            shotCircle = plt.Circle((x,pitchWidthY - y),circleSize,color="blue")
        else:
            shotCircle = plt.Circle((x,pitchWidthY - y),circleSize,color="red")
        if shot['shot_outcome_name']!='Goal':
            shotCircle.set_alpha(0.4)

        ax.add_patch(shotCircle)
non_p = mpatches.Patch(color='red', label='Non-penalty shot')
penalty = mpatches.Patch(color='blue', label='Penalty')
plt.legend(handles=[non_p,penalty],loc="lower left")
plt.text(5,81,player+"'s shots")     
fig.set_size_inches(10, 7)
fig.savefig('Output/tweet_shots.pdf', dpi=100) 
plt.show()
        
passes = df.loc[df['type_name']=='Pass'].set_index('id')
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
for i,pass1 in passes.iterrows():
    if pass1['player_name']==player:
        x = pass1['location'][0]
        y = pass1['location'][1]
        x_pass_received = pass1['pass_end_location'][0]
        y_pass_received = pass1['pass_end_location'][1]
        
        if pass1['pass_outcome_name']=='Incomplete':
            passArrow = plt.arrow(x,pitchWidthY-y,x_pass_received-x,y_pass_received-y,color="red",head_width=1)
        else:
            if pass1['pass_height_name']=="Ground Pass":
                passArrow = plt.arrow(x,pitchWidthY-y,x_pass_received-x,-y_pass_received+y,color="blue",head_width=1)
            elif pass1['pass_height_name']=="High Pass":
                passArrow = plt.arrow(x,pitchWidthY-y,x_pass_received-x,-y_pass_received+y,color="green",head_width=1)
            else:
                passArrow = plt.arrow(x,pitchWidthY-y,x_pass_received-x,-y_pass_received+y,color="orange",head_width=1)
        ax.add_patch(passArrow)
 
pop_a = mpatches.Patch(color='red', label='Incomplete Pass')
pop_b = mpatches.Patch(color='blue', label='Ground Pass')
pop_c = mpatches.Patch(color='green', label='High Pass')
pop_d = mpatches.Patch(color='orange', label='Low Pass')
plt.legend(handles=[pop_a,pop_b,pop_c,pop_d],loc="lower left")
plt.text(5,81,player+"'s passes")     
fig.set_size_inches(10, 7)
fig.savefig('Output/tweet_passes.pdf', dpi=100) 
plt.show()
