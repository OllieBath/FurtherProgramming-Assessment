#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:06:55 2022

@author: kareemelsabbagh
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from itertools import count
import pandas as pd
import matplotlib.patches as mpatches
table=pd.read_csv('./corona_records.csv',sep=',')
tf=pd.DataFrame(table)
slices={"Day":pd.Series(data=range(1,782),index=range(1,782)),
        "New Cases":pd.Series(data=tf["newCasesBySpecimenDate"],index=range(1,782)),
        "Cumulative Cases":pd.Series(data=tf["cumCasesBySpecimenDate"],index=(range(1,782))),
        "Cum Deaths":pd.Series(data=tf["cumDeaths"],index=range(1,782)),
        "New deaths":pd.Series(data=tf["newDeaths"],index=range(1,782)),
        "vaccinated":pd.Series(data=tf["Vac"],index=range(1,782))}
slicef=pd.DataFrame(slices)

x_days=list (slicef["Day"])
y1_newcases=list (slicef["New Cases"])
y2_cumcases=list(slicef["Cumulative Cases"])
y3_cumdeaths=list(slicef["Cum Deaths"])
y4_newdeaths=list(slicef["New deaths"])
y5_vaccinated=list(slicef["vaccinated"])


x,y1,y2,y3 = [], [],[],[]

fig = plt.figure(figsize=(5,2))
fst = fig.add_subplot(1,1,1)
# fst.set_ylim(0, 8*10**7,10**6)
fst.set_xlim(0, 800)
fst.set_ylabel("Number of infected and vaccinated cases",fontsize=12)
fst.set_xlabel("Days")
plt.style.use("seaborn")
sec=fst.twinx()
sec.set_ylabel("Number of death cases")
# sec.set_ylim(0, 160000)

red_patch = mpatches.Patch(color='red', label="Cumulative infected cases")
blue_patch = mpatches.Patch(color='blue', label="Cumulative death cases")
green_patch = mpatches.Patch(color='green', label="Vaccinated")
plt.legend(handles=[red_patch]+[blue_patch]+[green_patch],loc=("upper left"))



def animate(i):
    x.append(x_days[i])
    y1.append((y2_cumcases[i]))
    y2.append((y3_cumdeaths[i]))
    y3.append((y5_vaccinated[i]))
    fst.plot(x,y1, scaley=True, scalex=True, color="blue")
    sec.plot(x,y2, scaley=True, scalex=True, color="red")
    fst.plot(x,y3, scaley=True, scalex=True, color="green") 

ani = FuncAnimation(fig=fig, func=animate,frames=800, interval=0.0001, repeat=True)
ani.save("vid.mp4")    

