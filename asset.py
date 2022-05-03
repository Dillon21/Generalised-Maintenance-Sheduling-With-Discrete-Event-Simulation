# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:35:47 2022

@author: dillo
"""

class asset(object):
    
        
    #fluid implemented by days till fluid EOF  
    def __init__(self,name, age, maxAge):
        self.name = name
        self.age = age
        self.maxAge = maxAge;
        self.repairTime = 0
        self.replaceTime = 0
        #self.fluid = fluid
        #self.fluidEOF = fluidEOF
        
    def setName(self,name):
        self.name = name
    
    def setMaxAge(self,maxAge):
        self.maxAge = maxAge
        
    def setFluid(self,fluid):
        self.fluid = fluid
        
    def setFluidEOF(self,fluidEOF):
        self.fluidEOF = fluidEOF
    
    def getFluid(self):
        return self.fluid
        
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age
       
    def getMaxAge(self):
        return self.maxAge
    
    def setAge(self,age):
        self.age = age
    
#test values    
#asset1 = asset('ford',10, True,60)
#asset2 = asset('lexus', 20, False,0)



