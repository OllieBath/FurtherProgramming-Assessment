#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:06:55 2022

@author: kareemelsabbagh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

table=pd.read_csv('./corona_records.csv',sep=',')
tf=pd.DataFrame(table)
# print(tf)

slices={"Day":pd.Series(data=range(1,782),index=range(1,782)),
        "New Cases":pd.Series(data=tf["newCasesBySpecimenDate"],index=range(1,782)),
        "Cumulative Cases":pd.Series(data=tf["cumCasesBySpecimenDate"],index=(range(1,782))),
        "Cum Deaths":pd.Series(data=tf["cumDeaths"],index=range(1,782)),
        "New deaths":pd.Series(data=tf["newDeaths"],index=range(1,782)),
        "vaccinated":pd.Series(data=tf["Vac"],index=range(1,782))}
slicef=pd.DataFrame(slices)
# print(slicef.head())

days=slicef["Day"]
newcases=slicef["New Cases"]
cumcases=slicef["Cumulative Cases"]
cumDeaths=slicef["Cum Deaths"]
newdeaths=slicef["New deaths"]
vaccinated=slicef["vaccinated"]

# print(vaccinated)
def dplot(x,y1,y2,x_label,y1_label,y2_label,title):
    fig1,new=plt.subplots(figsize=(10,12))
    new.plot(x,y1,'r-')
    new.set_xlabel(x_label)
    # ax1.xticks(np.arange(10,800),50)
    new.set_ylabel(y1_label,fontsize=12)
    new.set_xlim(0,800)
    # new.set_ylim(0,300000)
    cum=new.twinx()
    cum.plot(x,y2,'-b',)
    # cum.set_ylim(0,22000000)
    cum.set_yscale("linear")
    cum.set_ylabel(y2_label,fontsize=12)
    
    cum.set_title(title)
    red_patch = mpatches.Patch(color='red', label=y1_label)
    blue_patch = mpatches.Patch(color='blue', label=y2_label)
    plt.legend(handles=[red_patch]+[blue_patch],loc=("upper left"))
    plt.savefig(title)

dplot(days,newcases,newdeaths,"Dayssssss","New casess","New Deaths","title")
dplot(days,vaccinated,newdeaths,"Dayssssss","vaccinated","Newdeaths","title2")



