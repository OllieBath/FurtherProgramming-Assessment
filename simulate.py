# Template

import numpy as np
from matplotlib import pyplot as plt

class Simulation:
    
    def __init__(self,duration):
           
        self.duration = duration
        self.day = 0 

           # just template probabilites, will change
        self.recovery_probability = 0.7
        self.infection_probability = 0.1
        self.death_probability = 0.05
class world:
    def __init__(self,width,height,xlim,ylim):
        self.width=width
        self.height=height
        self.xlim=xlim
        self.ylim=ylim
    def model(self):
        self.fig = plt.figure(figsize=(self.width,self.height))
        self.plt.xlim(0,self.xlim)
        self.plt.ylim(0,self.ylim)





    
