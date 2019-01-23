# Simulation Version 4 - Simulate Set Match Best of 9 Sets Between MVG and GA
# Encorporate Moving Average

import scipy as sp
import pandas as pd
from scipy.stats import gamma
from scipy.stats import dweibull
from scipy.stats import dgamma
import numpy as np
import random


# ----- Fit Model -----
dtf_data = pd.read_csv("/Users/michaeloboyle/Documents/MSISS_Year_4/FYP/Distributions/dtf_by_player.csv")

data_x = dtf_data[dtf_data["Player"] == 'Suljovic, M.']["DTF"]
data_y = dtf_data[dtf_data["Player"] == 'Whitlock, S.']["DTF"]
  
params_x = np.array(sp.stats.gamma.fit(data_x))
params_y = np.array(sp.stats.gamma.fit(data_y))

i = 1
x_win = 0
y_win = 0

MA = []
Sim_Count = []
cum_sum = 0

while i < 1000:

    set_count_x = 0
    set_count_y = 0
    throw_first = '' 
    throw_second = ''

    first = random.uniform(0,1)
    if first <= 0.5:
        throw_first = 'x'
        throw_second = 'y'
    else:
        throw_first = 'y'
        throw_second = 'x'
        
    print(throw_first)

    while set_count_x <= 4 and set_count_y <= 4:
    
        # ----- Initialise Variables -----
        leg_count_x = 0
        leg_count_y = 0
        
        # ----- Loop legs -----
        
        while leg_count_x <= 2 and leg_count_y <= 2:
            
            # ----- Simulate Random Variables -----
            sim_x = gamma.rvs(params_x[0], loc = params_x[1], scale = params_x[2], size = 1)
            sim_y = gamma.rvs(params_y[0], loc = params_y[1], scale = params_y[2], size = 1)
            
            if throw_first == 'x':
                if (sim_x - 3) < sim_y:
                    leg_count_x += 1
                else:
                    leg_count_y += 1
            else:
                if (sim_y - 3) < sim_x:
                    leg_count_y += 1
                else:
                    leg_count_x += 1
            
            temp = throw_second
            throw_second = throw_first
            throw_first = temp
        
            print("LEGS: " + str(leg_count_x) + " - " + str(leg_count_y))

        if leg_count_x > leg_count_y:
            set_count_x += 1
        else:
            set_count_y += 1

        print("SETS: " + str(set_count_x) + " - " + str(set_count_y))

    if set_count_x > set_count_y:
        x_win += 1
    else:
        y_win += 1

        cum_sum = x_win
    mean = cum_sum/i
    MA.append(mean)
    Sim_Count.append(i)
            
    i += 1
    
    
plt.scatter(Sim_Count, MA)
plt.show()
            
            





