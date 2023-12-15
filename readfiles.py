# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:48:01 2023

@author: E.E. Aalbers
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('c:\\Users\\emmae\\OneDrive - HvA\\HvA\\04_Data_modellen\\WaterbergendeWeg\\Data\\')
filen = 'all_Zuidegge_id1933d4ec-d3fb-e911-b862-0003ff599e2a.csv'

data = pd.read_csv(filen, delimiter= ';')
var = list(data) # columnames

pr = data[var[2]] # 
tt = pd.to_datetime(data["datum"])


plt.plot(tt, pr)