#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:57:53 2022

@author: kareemelsabbagh
"""

from Graph_Plot import dplot 
import pandas as pd


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

dplot(days,newcases,newdeaths,"days","new cases","New deaths","Coronavirus " )
dplot(days, vaccinated, cumDeaths, "Days", "Number of people vaccinated", "Cumulative number of deaths", "Vaccination effect ")
