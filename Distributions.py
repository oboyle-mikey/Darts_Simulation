# Version 2 - Distributions for each player

import pandas as pd
from fitter import Fitter

dtf_data = pd.read_csv("/Users/michaeloboyle/Documents/MSISS_Year_4/FYP/Distributions/dtf_by_player.csv")

unique_players = dtf_data['Player'].unique()

print (sorted(unique_players))

data_frame = pd.DataFrame()

Player = []
Distribution = []

for player in unique_players:
    
    data = dtf_data[dtf_data["Player"] == player]["DTF"]
    
    dist = Fitter(data)

    dist.fit()
    
    t = dist.get_best()
    
    a = list(t.keys())[0]
    
    Player.append(player)
    Distribution.append(a)
    
data_frame["Player"] = pd.Series(Player)
data_frame["Distribution"] = pd.Series(Distribution)

fileStr = str("/Users/michaeloboyle/Documents/MSISS_Year_4/FYP/player_distributions.csv")
data_frame.to_csv(fileStr, encoding='cp1252', index=False, header=False)


# Best distribution for all data 
data = dtf_data["DTF"]
    
dist = Fitter(data)

dist.fit()
    
t = dist.get_best()
    
a = list(t.keys())[0]



    
    