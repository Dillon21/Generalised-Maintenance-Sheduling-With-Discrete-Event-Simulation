# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:28:24 2022

@author: dillo
"""


class asset(object):
    def __init__(self, env, name, age):
         self.env = env
         # Start the run process everytime an instance is created.
         self.action = env.process(self.run())
         self.name = name
         self.age = age
         self.break_Chance = 0
         self.broken = False
         self.repairTime = 0
        
    def run(self):
        #initialse brake chance according to age
        #use maintain function as it does the same thing
        self.maintain()
        import day
        Day = day.day(0)
        
        
        while True:
            
            #pass a workday in environment
            #track hours through day process
            Day.workDay()
            # wait for working day to end
            
            yield self.env.process(self.work())
        
            print("asset is operating till hour %d" % self.env.now)
            
            
            #pass a nighttime into environment                       
            Day.night()
            yield self.env.timeout(Day.getNightLength())
            print("asset has stopped till hour %d" % self.env.now)
            
    def work(self):
        # 8 hours working day
        hours = 8
        while hours > 0:
            
            #if asset is broken stop working to repair
            while self.broken == True:
                yield self.env.timeout(1)
                hours -= 1
                self.repairTime -= 1
                print("repair hours = %d " % self.getRepairTime())
                if self.repairTime == 0:
                    self.broken = False
                    self.maintain()
            
            #normal operation    
            yield self.env.timeout(1)
            self.deteriorate(self)
            print(hours)
            hours -= 1
    
    
    @staticmethod    
    def deteriorate(self):
        self.break_Chance = (0.003 + self.break_Chance)
        print("\nchance1 = ", self.break_Chance)
        self.fail(self)
 
    #add code that will randomly break the asset    
    @staticmethod
    def fail(self):
        value = self.getRandom()
        print("value = ",value)

        #break if asset is over threshold    
        if value >= (1 - self.break_Chance):
            self.broken = True
            print("broken")
            self.repairTime = 4
            
        elif value < (1-self.break_Chance):
            self.broken = False
            print("working")
    
     
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age
    
    def maintain(self):
        self.break_Chance = (self.age / 100)
        
    def getRepairTime(self):
        return self.repairTime
    
    #get a random value for every cycle
    #each hour will present a different chance for failure
    def getRandom(self):
        import random
        import time
        time.sleep(1)
        random.seed(time.localtime())
        value = round(random.uniform(0,1), 4)
        return value
    
    
        
import simpy
env = simpy.Environment()
asset1 = asset(env,"ford", 5)

env.run(until=49)


