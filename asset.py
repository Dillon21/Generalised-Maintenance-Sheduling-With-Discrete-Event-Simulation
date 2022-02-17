# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 17:03:54 2022

@author: dillo
"""

# generate random floating point values
from random import seed
from random import random

name = ""
age = 0


class asset:
    def __init__(self, name, age, break_Chance):
        self.name = name
        self.age = age
        self.break_Chance = break_Chance
        
    @staticmethod    
    def deteriorate(self):
        self.break_Chance = (age / 100) + (0.003 + self.break_Chance)
        print("chance1 = ", self.break_Chance)
        self.fail(self)
    @staticmethod
    def fail(self):
        self.break_Chance = 1 - self.break_Chance
        value = random()
        print("value = ",value)
        print("chance = ", self.break_Chance)
        if value >= self.break_Chance:
            broken = True
            print("broken")
        elif value < self.break_Chance:
            broken = False
            print("working")
    
     
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age
        

car1 = asset("ford",5,0)
Break = False


for x in range(10):
    car1.deteriorate(car1)
    