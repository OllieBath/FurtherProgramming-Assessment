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
               
        # inital condition
        chance = np.random.random()
        
        if chance < 0.95:
            self.condition="healthy"
        else:
            self.condition="infected"

        # chance of dying, if above 0.99 (1% chance) this person will die if they get covid
        self.chanceofdeath = np.random.random()
    #setting all possible conditions    
        
    def infect(self):
        self.condition="infected"


    def vaccinate(self):
        self.vaccinated="vaccinated"


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
    #set the possibilities of infected/recovered/dead    
    def chance_to_die(self):
        if self.condition == "infected":
            if self.chanceofdeath > 0.95:
                chance = np.random.random()
                # chance of death 10%
                if chance > 0.95:
                    self.change_speed([0,0])
                    self.condition = "dead"
            else:
                chance = np.random.random()
                if chance > 0.995:
                    self.condition = "recovered"
    
    def getvaccinated(self):
       
        if self.condition=="healthy":
           chance=np.random.random()
           if chance >0.5:
               self.condition== "vaccinated"
           else:
               self.condition== "healthy"
               
    def chance_to_infect(self, others):
        status = self.condition
        range = 0.5

        if status == "healthy":
            for person in others:
                if person.position[0] < (self.position[0] + range) and person.position[0] > (self.position[0] - range):
                    if person.position[1] < (self.position[1] + range) and person.position[1] > (self.position[1] - range):
                        if person.condition == "infected":
                            chance = np.random.random()
                            # chance of infection 30%
                            if chance > 0.985:
                                self.condition = "infected"

    def update_position(self):
        speed = self.speed

        

        
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
#delect the axis of the left simulation        
class world:
    def __init__(self,axis):
        self.axis=axis
        self.axis.set_xticks([])
        self.axis.set_yticks([])

class Simulation:
    
    def __init__(self, duration, population):
           
        self.duration = duration
        self.day = 0
        self.population = population

        self.everyone = []

        self.fig = plt.figure(figsize=(8,4))
        self.ax1 = self.fig.add_subplot(1,2,1)
        self.ax2 = self.fig.add_subplot(1,2,2)
        self.ax1.set_xlim(0,10)
        self.ax1.set_ylim(0,10)
        self.ax1.noaxis=world(self.ax1)
        self.ax2.set_xlim(0,10)
        self.ax2.set_ylim(0,10)
        
        self.framex, self.framey,self.framecolors, self.frameday, self.framehealthy, self.frameinfected, self.framerecovered, self.framedead = self.animate()
        self.x = []
        self.yHealthy = []
        self.yInfected = []
        self.yRecovered = []
        self.yDead = []
        
    
    def animate(self):
        # frames for animation, contains location of people
        self.frames = []

        # set up
        self.everyone = [Person() for i in range(self.population)]
        
        
        framex = []
        framey = []
        framecolors = []
        frameday = []
        framehealthy = []
        frameinfected = []
        framerecovered = []
        framedead = []
        

        for n in range(self.duration):
            list = []
            for x in range(n+1):
                list.append(x) 
            frameday.append(list)

            locations = []
            statuses = []
            healthycount = 0
            infectedcount = 0
            recoveredcount = 0
            deadcount = 0
            vaccinatedcount=0
            
            for person in self.everyone:
                # array of everyones location for specific point in time
                locations.append(person.position)
                # [[x,y],[x.y],[x,y]]  
                if person.condition=='healthy':
                    statuses.append('#00FF00')
                    healthycount += 1
                    
                elif person.condition=='infected':
                    statuses.append('#FF0000')
                    infectedcount += 1
                elif person.condition=='recovered':
                    statuses.append('#0000FF')
                    
                    recoveredcount += 1
                elif person.condition=='dead':
                    statuses.append('#000000')
                    deadcount += 1
                    
                #elif person.condition=='vaccinated':
                #    statuses.append('#FFFF00')
                    
                #    vaccinatedcount += 1
                #set the colour for every state    

            framehealthy.append(healthycount)
            frameinfected.append(infectedcount)
            framerecovered.append(recoveredcount)
            framedead.append(deadcount)

            # scatter plot of everyones location for specific point in time
            locationsx = []
            locationsy = []
            for n in range(len(locations)):
                locationsx.append(locations[n][0])
                locationsy.append(locations[n][1])

            #locationsscatter = [plt.scatter(locationsx, locationsy, c=statuses)]


            framex.append(locationsx)
            framey.append(locationsy)
            framecolors.append(statuses)

            

            
            # add to list of all frames
            
            #for person in self.everyone:
            #    person.getvaccinated()
            # move every person
            for person in self.everyone:
                person.chance_to_die()
            # spread disease
            for person in self.everyone:
                person.chance_to_infect(self.everyone)
            # move every person
            for person in self.everyone:
                person.update_position()
            
        return framex, framey, framecolors, frameday, framehealthy, frameinfected, framerecovered, framedead        
                  
    def init(self):
        #print(self.framecolors[0])
        #print(self.framex[0])
        #print(self.frameday)
        #print(len(self.framex))
        #print(self.framehealthy[:500+2])
        #print(self.framehealthy[:1])
        self.a1 = self.ax1.scatter(self.framex[0],self.framey[0],c=self.framecolors[0])
        
        #a2 = self.ax2.plot([],[])
        #a2 = self.ax2.scatter(self.framex[0],self.framey[0],c=self.framecolors[0])
        #self.a2 = self.ax2.scatter(self.framex[0],self.framey[0],c=self.framecolors[0])
        self.ax2.clear()
        return self.a1, self.ax2

    def animatescatter(self,i):
        #print(i)
        self.a1 = self.ax1.scatter(self.framex[i], self.framey[i], c=self.framecolors[i])

        return self.a1

    def animateline(self, i):
        if i == 0:
            self.x = []
            self.yHealthy = []
            self.yInfected = []
            self.yRecovered = []
            self.yDead = []
        
        ptHealthy = self.framehealthy[i]
        ptInfected = self.frameinfected[i]
        ptRecovered = self.framerecovered[i]
        ptDead = self.framedead[i]

        self.x.append(i)

        self.yHealthy.append(ptHealthy)
        self.yInfected.append(ptInfected)
        self.yRecovered.append(ptRecovered)
        self.yDead.append(ptDead)

        self.ax2.clear()

        self.ax2.plot(self.x, self.yHealthy, linewidth=2, label='Healthy')
        self.ax2.plot(self.x, self.yInfected, linewidth=2, label='Infected')
        self.ax2.plot(self.x, self.yRecovered, linewidth=2, label='recovered')
        self.ax2.plot(self.x, self.yDead, linewidth=2, label='dead')

        self.ax2.set_xlim([0,self.duration])
        self.ax2.set_ylim([0,self.population])

        self.ax2.legend(loc="upper right")

        return self.ax2

    def update(self, i):
        a1 = self.animatescatter(i)
        a2 = self.animateline(i)

        return a1, a2

    def showanimation(self):
        
        anim = animation.FuncAnimation(self.fig, self.update, init_func=self.init,frames=range(self.duration), blit=True, interval=2)

        plt.show()


#test


sim1 = Simulation(500,200)
sim1.animate
sim1.showanimation()

