# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:28:24 2022

@author: dillo
"""


class asset(object):
    def __init__(self, env, name, age, break_Chance):
         self.env = env
         # Start the run process everytime an instance is created.
         self.action = env.process(self.run())
         self.name = name
         self.age = age
         self.break_Chance = break_Chance
         self.broken = False
        
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
        import random
        import time
        random.seed(time.process_time())
        value = round(random.uniform(0,1), 4)
        print("value = ",value)
        print("chance = ", self.break_Chance)
        #check if asset is broken
        if self.broken == True:
            print("repair time")
        #break if asset is over threshold    
        elif value >= (1 - self.break_Chance):
            self.broken = True
            print("broken")
        elif value < (1-self.break_Chance):
            self.broken = False
            print("working")
    
     
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age
    
    def maintain(self):
        self.break_Chance = (self.age / 100)
        
        
        
import simpy
env = simpy.Environment()
asset1 = asset(env,"ford", 5, 0)
env.run(until=49)


