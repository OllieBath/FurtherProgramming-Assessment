

import random
from random import randint

class Person():
    defaultspeed=[0,0]
    gridsize=[100,100]
    
    def __init__(self):
        

        #Initial settings (0 speed for random speed)


   
 

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


            
                





        

##TEST
    
def main():
    person1= Person()
    person2= Person()

    print(person1.status())

    person1.kill()

    print(person1.status())





    
    


main()
 
       
        
        
        


    
