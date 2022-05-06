# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:28:24 2022

@author: dillo
"""

class assetSim():
    from Component import Component
    #from RepairMan import RepairMan
            
    def __init__(self, env, asset,machineName):
         
         self.env = env
         # Start the run process everytime an instance is created.
         self.action = env.process(self.run())
         self.name = asset.getName()
         self.age = asset.getAge()
         self.maxAge = asset.getMaxAge()
         self.break_Chance = self.calcInitCond() / 100
         self.broken = False
         self.repairTime = 0
         self.path = ''
         self.value = 0;
         self.maintainCount = 0
         self.workingHours = 0
         self.maintainPeriod = asset.getMaintenancePeriod()
         self.asset = asset
         self.machineName = machineName
         self.RepairMan = None
         #self.stoppedAssets = []
         #self.spareParts = self.getSpareParts()
         
        
        
        
    #while asset is broken remove it from environment
    
    def run(self):
        #initialse brake chance according to age
        #use maintain function as it does the same thing
        #self.maintain()
        import day
        Day = day.day(0)
        self.createCSV(self.machineName)
        
        
        
        while True:
            
            #pass a workday in environment
            #track hours through day process
            Day.workDay()
            # wait for working day to end
            print("asset has started operation at hour %d" % self.env.now)
            self.env.process(self.work())
        
            
            
            
            #pass a nighttime into environment                       
            Day.night()
            yield self.env.timeout(Day.getNightLength())
            print("asset has stopped operation at hour %d" % self.env.now)
            
    def work(self):
        # 8 hours working day
        hours = 8
        while hours > 0:
            
            
            #if asset is broken stop working to repair
            while self.broken == True:
                print(self.name ," ", self.age)
                if hours == 0:
                    break
                else:
                    yield self.env.timeout(1)
                    hours -= 1
                    self.setAge(self.age + 1)
                    self.repairTime -= 1
                    print(self.getName(), " repair hours = %d " % self.getRepairTime())
                    
                    if self.repairTime == 0:
                        self.repair()
                        #self.broken = False
                    else:
                        self.appendCSV()
                    break
                    
            
            while self.broken == False and hours > 0:
                print(self.name ," ", self.age)
                
#Attempt to make csv availabilty database                
# =============================================================================
#                 if self.machineName in self.stoppedAssets:
#                     yield self.env.timeout(1)
#                     self.appendCSV() 
# =============================================================================
                
               
                #normal operation
                self.workingHours += 1
                self.deteriorate(self) 
                self.appendCSV()   
                yield self.env.timeout(1)
                self.setAge(self.age + 1)
                
                if  self.maintainPeriod / self.workingHours == 1 and hours >=1:
                    self.maintain()
                
                print('workinghours = ' + str(self.workingHours))
                print('maintainPeriod = ' + str(self.maintainPeriod))
                print("working hours left = ", hours )
                hours -= 1
            
            
    
    
    @staticmethod    
    def deteriorate(self):
        counter = self.workingHours * 0.0003
        self.break_Chance = (0.0002 + self.break_Chance) + counter
        print("\n")
        print(self.getName(), " condition rating  = ", self.break_Chance)
        self.fail(self)
 
    #add code that will randomly break the asset    
    @staticmethod
    def fail(self):
        self.value = self.getRandom()
        print("value = ",self.value)

        #break if asset is over threshold    
        if self.value >= (1 - self.break_Chance):
            self.broken = True
            print("broken")
            #self.stoppedAssets.append(self.machineName)
            self.repairTime = 4
            
        elif self.value < (1-self.break_Chance) and self.broken == True:
            self.broken = False
            print("working")
            
    
    def maintain(self):
        #maintaining
        if self.broken == False:
            self.env.timeout(1)
            self.workingHours = 0
        
        
    def repair(self):
        if self.break_Chance > 0.5:
            self.workingHours = 0
            self.setAge(0)
            self.break_Chance = (self.calcInitCond())
            self.broken = False
            #self.stoppedAssets.remove(self.machineName)
            self.maintainCount = 0
                
        if self.broken == True:
            self.workingHours = 0
            self.maintainCount = (self.break_Chance * 1.02)
            self.break_Chance = (self.calcInitCond() /100) * self.maintainCount
            self.broken = False
            #self.stoppedAssets.remove(self.machineName)
                      
        
    def calcInitCond(self):
       out = 0
       out = (self.age/self.maxAge) * 100
       return out   
   
    def getRepairTime(self):
        return self.repairTime
    
    
    #get a random value for every cycle
    #each hour will present a different chance for failure
    def getRandom(self):
        from random import SystemRandom
        randfloat = SystemRandom()
        value = randfloat.random()      
        return value
    
    def appendCSV(self):
        import csv
        with open(self.path,'a',newline='') as file:
            if self.broken == True:
                writer = csv.writer(file)
                writer.writerow([self.break_Chance,self.value,'broken',self.env.now, self.repairTime])
            elif self.broken != True:
                writer = csv.writer(file)
                writer.writerow([self.break_Chance,self.value, 'working',self.env.now, self.repairTime])
    
    def createCSV(self,machine):
        import os
        folder_Path = 'base' + '\\' + machine
        if not os.path.exists(folder_Path):
            os.makedirs(folder_Path)
        
        path = folder_Path + '\\' + self.getName() + '_output' + '.csv'
        self.path = path
        import csv
        with open(path,'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Age wear','break chance', 'Status', 'Hour', 'RTime'])
            
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        Age = age
        self.age = Age
        self.asset.setAge(Age)
        
    def setRepairMan(self):
        self.RepairMan.setRepairMan(self.name)
        
    #def relieveRepairMan(self):
        
        
        
        
# =============================================================================
#     def getSpareParts(self):
#         from assetGetter import assetGetter
#         lst = assetGetter.getList('repairMan')
#         lst.reset_index()
#         
#         
#         return lst
# =============================================================================

# =============================================================================
# import simpy
# from asset import asset
# env = simpy.Environment()
# asset1 = asset('van', 100,200)
# sim = assetSim(env, asset1)
# 
# print(sim.getSpareParts())
# =============================================================================
