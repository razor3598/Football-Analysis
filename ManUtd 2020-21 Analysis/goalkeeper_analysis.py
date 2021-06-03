# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:36:50 2021

@author: Amod
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
goalkeeper_data = pd.read_csv('Data/goalkeeping.csv')
matches_played = goalkeeper_data['MP']
goalkeeper_data = pd.read_csv("Data/adv_goalkeeping.csv")
goalkeeper_data['MP'] = matches_played

### Clean the data ###
for i,x in enumerate(goalkeeper_data['Player']):
    temp = x.split('\\')[1].split("-")
    goalkeeper_data['Player'].iloc[i] = temp[len(temp)-1]

        
# Filter goalkeepers who have played more than 10 matches
goalkeeper_data = goalkeeper_data[goalkeeper_data['MP']>=10]


# Plotting xG against/90 and goals conceded/90
colors={}
for x in goalkeeper_data['Squad'].unique():
    colors[x]='blue'
    if x=="Manchester Utd":
        colors[x]='red'

fig, ax = plt.subplots(figsize=(28,20))
ax.scatter( goalkeeper_data['Expected_PSxG'],goalkeeper_data['GA'],c=goalkeeper_data['Squad'].map(colors),s=15)
    
for i, txt in enumerate(goalkeeper_data.Player):
    ax.annotate(txt,(goalkeeper_data.Expected_PSxG.iloc[i],goalkeeper_data.GA.iloc[i]+0.005))

ax.set_xlabel("xG against per 90",fontsize=14) 
ax.set_ylabel("Goals against per 90",fontsize=14)
ax.set_title("Comparision of xG against/90 and goals conceded/90",fontsize=25)
plt.savefig('premier_league_keepers')
plt.show()


###########################################################

# Load the data for Passing metric
passing_data = pd.read_csv('Data/passing_stats.csv')
passing_data = passing_data[(passing_data['Pos']=='GK') & (passing_data['90s']>=10.0)]

#Clean the data
for i,x in enumerate(passing_data['Player']):
    temp = x.split('\\')[1].split("-")
    passing_data['Player'].iloc[i] = temp[len(temp)-1]


#Calculate pass rating
passing_data['pass_rating'] = (passing_data['Short_Cmp'] - ((passing_data['Short_Att']-passing_data['Short_Cmp'])*2) + ((passing_data['Medium_Cmp']+passing_data['Long_Cmp'])*2) - ((passing_data['Medium_Att']+passing_data['Long_Att']) - (passing_data['Medium_Cmp']+passing_data['Long_Cmp']))) / ((passing_data['Short_Att']) + ((passing_data['Medium_Att']+passing_data['Long_Att'])*2))

#Print the table sorted by pass_rating
print(passing_data[['Player','pass_rating']].sort_values("pass_rating",ascending=False).head(10))