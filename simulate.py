import numpy as np
from matplotlib import pyplot as plt, animation
import random
from random import randint

class Person():
    #Initial settings (0 speed for random speed)

    defaultspeed=[0,0]
    gridsize=[10,10]
    
    def __init__(self):
        #Choosing random direction, speed, position
        xposition= 10 * np.random.random()
        yposition= 10 * np.random.random()

        speed = [ ((np.random.random() / 10)*random.choice([-1,1])), ((np.random.random() / 10)*random.choice([-1,1]))]

        #Add initial settings to self
        self.radius=1
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


    def change_position(self,position):
        self.position=position


    def change_speed(self,speed):
        self.speed=speed


    def update_position(self):
        speed = self.speed
        print(speed)
        
        # if x touching boundaries 
        if self.position[0] + self.speed[0] < 0:
            x = -self.speed[0] - self.position[0]
            self.speed[0] = -self.speed[0]
        elif self.position[0] + self.speed[0] > self.gridsize[0]:
            x =2*self.gridsize[0]-self.speed[0]-self.position[0]
            self.speed[0] = -self.speed[0]
        else:
            x = self.position[0] = self.position[0] + self.speed[0]

        # if y touching boundaries
        if self.position[1] + self.speed[1] < 0:
            y = -self.speed[1] - self.position[1]
            self.speed[1] = -self.speed[1]
        elif self.position[1] + self.speed[1] > self.gridsize[1]:
            y =2*self.gridsize[1]-self.speed[1]-self.position[1]
            self.speed[1] = -self.speed[1]
        else:
            y = self.position[1] = self.position[1] + self.speed[1]

        # update position
        self.position = [x, y]


class Simulation:
    
    def __init__(self, duration, population):
           
        self.duration = duration
        self.day = 0
        self.population = population

        # just template probabilites, will change
        self.recovery_probability = 0.7
        self.infection_probability = 0.1
        self.death_probability = 0.05

        self.everyone = []


    def animate(self):
        # frames for animation, contains location of people
        self.frames = []

        # set up
        self.everyone = [Person() for i in range(self.population)]
        self.fig = plt.figure(figsize=(10, 10))
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        self.axs = plt.axes()

        for n in range(self.duration):
            locations = []
            status=[]
            for person in self.everyone:
                # array of everyones location for specific point in time
                locations.append(person.position)
                # [[x,y],[x.y],[x,y]]  
                if person.condition=='healthy':
                    status.append('#00FF00')
                elif person.condition=='infected':
                    status.append('#FF0000')
                elif person.condition=='recovered':
                    status.append('#0000FF')
                elif person.condition=='dead':
                    status.append('#000000')
            # scatter plot of everyones location for specific point in time
            locationsx = []
            locationsy = []
            for n in range(len(locations)):
                locationsx.append(locations[n][0])
                locationsy.append(locations[n][1])
            locationsscatter = [self.axs.scatter(locationsx, locationsy, c=status)]
            
            # add to list of all frames
            self.frames.append(locationsscatter)
            
            # move every person
            for person in self.everyone:
                person.update_position()
            
                    
                  
        simulate = animation.ArtistAnimation(self.fig, self.frames, interval=20)
        plt.pause(0.05)
        plt.show()        
       
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

#test
sim1 = Simulation(100,10)
sim1.animate()

