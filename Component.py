# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:35:47 2022

@author: dillo
"""

class Component(object):
    
        
    #fluid implemented by days till fluid EOF  
    def __init__(self,name, age, maxAge,maintenancePeriod):
        
        if type(name) != str:
            raise TypeError("Name has to be a word, Check relevant component.csv in file name column")
        self.name = name
        
        if type(age) != int:
            raise TypeError("Age must to be a whole number, please check relevant " + str(self.name) + " component.csv")
        if age <= 0:
            raise ValueError("Age cannot be less than or equal to 0, please check relevant " + str(self.name) + "component.csv")
        self.age = age
        
        if type(maxAge) != int:
            raise TypeError("max age must to be a whole number, please check relevant " + str(self.name) + " component.csv")
        if maxAge <= 0:
            raise ValueError("max age cannot be less than or equal to 0, please check relevant " + str(self.name) + "component.csv")
        self.maxAge = maxAge;
        
        if type(maintenancePeriod) != int:
            raise TypeError("maintenace period must be a whole number in hours")
        if maintenancePeriod <= 0:
            raise ValueError("Maintenance period cannot be negative or zero hours, please check relevant " + str(self.name) + " component.csv")
        self.maintenancePeriod = maintenancePeriod
        
        
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
        
    def getMaintenancePeriod(self):
        return self.maintenancePeriod
    
    def setMaintenancePeriod(self, period):
        self.maintenancePeriod = period
        
    def toString(self):
        return 'Name:' + self.getName() +\
            '\nAge:' + str(self.getAge()) +\
                '\nmaxAge:' + str(self.getMaxAge()) +\
                    '\nMaintenance Period:' + str(self.getMaintenancePeriod()) +\
                        '\n---------------------------------------------------------\n\n'
    
#test values    
#asset1 = asset(True,10, True,60)
#asset2 = asset('lexus', 20, False,0)



