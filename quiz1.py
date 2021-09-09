# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:16:28 2021

@author: c_ken
"""

import numpy as np
from pylab import *

#importing data 
CO2_ppm_MaunaLoa = np.load("Mauna.npy")
#print(CO2_ppm_MaunaLoa)

#Now to create an array of timepoints in years for each data point
#Every year will have ~26 data points - 230 total 
#print(len(CO2_ppm_MaunaLoa))

x = np.linspace(0, 230/26.0714 , 230)
#print(x)

#Plotting CO2 concentration per year from 1981
plot(x, CO2_ppm_MaunaLoa)
title("CO2 Concentrations in Mauna Hawaii")
ylabel("CO2 Concentration (ppm)")
xlabel('Years after 1981')

#Plotting the bestfit and printing slope
m, b = np.polyfit(x, CO2_ppm_MaunaLoa, 1)
plt.plot(x, m*x + b)
print(m)
# slope = 1.54 ppm CO2 / year increase 

plt.text(.5, 350, "1.54 ppm CO2 increase per year")
