# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:13:11 2021

@author: Amod
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from FCPython import createPitch

#Reading the csv file for shots across Europe
shots = pd.read_csv('shots_europe_2020_2021.csv')

#Collecting shots by Isak
shots = shots[shots['player']=='Alexander Isak']

#Shots that were goals scored by Isak
goals = shots[shots['result']=='Goal']

#Printing the assist provided to Isak
print(goals['player_assisted'].value_counts())
print(shots['player_assisted'].value_counts())

#----- Isak Shot Map-----

pitchLengthX = 120
pitchWidthY = 80

OldRange = 1.0 - 0.0 
NewRange_X = 120 - 0
NewRange_Y = 80 - 0

shots['X'] = shots['X'].apply(lambda x:(((x - 0.0) * NewRange_X) / OldRange) + 0.0)
shots['Y'] = shots['Y'].apply(lambda x:(((x - 0.0) * NewRange_Y) / OldRange) + 0.0)


#print(shots['result'].unique())
#Plotting two plots for goals scored and shots that were not goals
(plt1,fig1,ax1) = createPitch(pitchLengthX,pitchWidthY,'yards','black')
(plt2,fig2,ax2) = createPitch(pitchLengthX,pitchWidthY,'yards','black')

for i,shot in shots.iterrows():
    x = shot['X']
    y = shot['Y']
    #circleSize = 1.5
    circleSize=np.sqrt(shot['xG'])*2
    
    if shot['result']=='ShotOnPost':
        shotCircle=plt.Circle((x,y),circleSize,color="cyan")
        ax1.add_patch(shotCircle)
    
    if shot['result']=='Goal':
        if shot['shotType']=='Head':
            shotCircle=plt.Circle((x,y),circleSize,color="green")
            ax2.add_patch(shotCircle)
            
        elif shot['shotType']=='LeftFoot':
            shotCircle=plt.Circle((x,y),circleSize,color="cyan")
            ax2.add_patch(shotCircle)
            
        elif shot['shotType']=='RightFoot':
            shotCircle=plt.Circle((x,y),circleSize,color="red")
            ax2.add_patch(shotCircle)
    
    if shot['result']=='MissedShots':
        shotCircle=plt.Circle((x,y),circleSize,color="blue")
        ax1.add_patch(shotCircle)
        
    if shot['result']=='SavedShot':
        shotCircle=plt.Circle((x,y),circleSize,color="red")
        ax1.add_patch(shotCircle)

    if shot['result']=='BlockedShot':
        shotCircle=plt.Circle((x,y),circleSize,color="violet")
        ax1.add_patch(shotCircle)
        
#Adding a legend to the plot
red_patch = mpatches.Patch(color='red', label='Right Foot')
cyan_patch = mpatches.Patch(color='cyan', label='Left Foot')
green_patch = mpatches.Patch(color='green', label='Header')

cyan_patch1 = mpatches.Patch(color='cyan', label='Shot on Post')
blue_patch1= mpatches.Patch(color='blue', label='Missed shot')
red_patch1 = mpatches.Patch(color='red', label='Saved shot')
violet_patch1 = mpatches.Patch(color='violet', label='Blocked shot')

second_legend  = ax2.legend(handles=[red_patch,cyan_patch,green_patch])
ax2.add_artist(second_legend)
first_legend = ax1.legend(handles=[red_patch1,cyan_patch1,blue_patch1,violet_patch1])
ax2.add_artist(first_legend)