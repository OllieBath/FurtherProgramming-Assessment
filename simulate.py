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
        
class Animation:
    #class for animation
    def __init__(self):
        #set the size of the figure
        self.fig=plt.figure(figsize=(8,8))
        #this is a sub plot allowing two figure in one run, can be changed to add another plot
        self.axes_world = self.fig.add_subplot(1, 1, 1)
        self.world = world(self.axes_world)
       
    
class world:
    def __init__(self,axes):
        
        #hides the x, y axis of animation      
        self.axes=axes
        self.axes.set_xticks([])
        self.axes.set_yticks([])
'''
test to see whether the world works
x=Animation()
print(x)

'''

    

