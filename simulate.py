# Template

import numpy as np
from matplotlib import pyplot as plt


import random
from random import randint

class Person():
    #Initial settings (0 speed for random speed)

    defaultspeed=[0,0]
    gridsize=[100,100]
    
    def __init__(self):
        



   
 

        #Choosing random direction, speed, position

        
        xposition=randint(0,Person.gridsize[0])
        yposition=randint(0,Person.gridsize[1])

        #Set random speed
        speedlist=[-5,-4,-3,-2,-1,1,2,3,4,5]
        speed=Person.defaultspeed

        for i in range(2):
            if speed[i]==0:
                speed[i]=random.choice(speedlist)

        
        

        #Add initial settings to self

        self.width=1
        self.height=1
        self.speed=speed
        self.position=[xposition,yposition]
        self.vaccinated=0
        
        self.condition="healthy"



    def infect(self):
        self.condition="infected"

    def vaccinate(self):
        self.vaccinated=1

    def kill(self):
        self.speed=[0,0]
        self.condition="dead"

    def recover(self):
        self.condition="recovered"


    def status(self):
        status={"position":self.position,"speed":self.speed,"vaccinated":self.vaccinated,"condition":self.condition}

        return status

    def position(self,position):
        self.position=position
        
    def speed(self,speed):
        self.speed=position

    def updateposition(self):
        #Update position

        for i in range(2):
            newpos=self.position[i]+self.speed[i]

            if newpos>self.gridsize[i] or newpos<0:
                newpos=self.position[i]
                self.speed[i]=self.speed[i]*-1

            self.position[i]=newpos


            
                




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

    

