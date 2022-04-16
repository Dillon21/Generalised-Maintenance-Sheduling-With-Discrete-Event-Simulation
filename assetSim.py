# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:28:24 2022

@author: dillo
"""

class assetSim(object):
    from asset import asset
            
    def __init__(self, env, asset):
         
         self.env = env
         # Start the run process everytime an instance is created.
         self.action = env.process(self.run())
         self.name = asset.getName()
         self.age = asset.getAge()
         self.break_Chance = self.age / 1000
         self.broken = False
         self.repairTime = 0
         self.path = ''
         self.value = 0;
         self.maintainCount = self.break_Chance
        
        
        
    #while asset is broken remove it from environment
    
    def run(self):
        #initialse brake chance according to age
        #use maintain function as it does the same thing
        #self.maintain()
        import day
        Day = day.day(0)
        self.createCSV()
        
        
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
                if hours == 0:
                    break

                yield self.env.timeout(1)
                hours -= 1
                self.repairTime -= 1
                print(self.getName(), " repair hours = %d " % self.getRepairTime())
                
                if self.repairTime == 0:
                    self.broken = False
                    self.maintain()
                self.appendCSV()
            
            #normal operation    
            yield self.env.timeout(1)
            self.deteriorate(self)
            self.appendCSV()
            print("working hours left = ", hours )
            hours -= 1
    
    
    @staticmethod    
    def deteriorate(self):
        self.break_Chance = (0.0003 + self.break_Chance)
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
            self.repairTime = 4
            
        elif self.value < (1-self.break_Chance) and self.broken == True:
            self.broken = False
            print("working")
            
    
    def maintain(self):
        self.maintainCount = self.maintainCount * 1.10
        self.break_Chance = (self.age / 1000) * self.maintainCount
        
        if self.break_Chance > 0.5:
            self.break_Chance = (self.age / 100)
        
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
                writer.writerow([self.break_Chance,self.value,'broken',self.env.now])
            elif self.broken != True:
                writer = csv.writer(file)
                writer.writerow([self.break_Chance,self.value, 'working',self.env.now])
    
    def createCSV(self):
        import os
        folder_Path = 'test'
        if not os.path.exists(folder_Path):
            os.makedirs(folder_Path)
        
        path = folder_Path + '\\' + self.getName() + '.csv'
        self.path = path
        import csv
        with open(path,'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Age wear','break chance', 'Status', 'Hour'])
    
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age
    
    



