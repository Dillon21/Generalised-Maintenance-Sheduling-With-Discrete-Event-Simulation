# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:35:50 2022

@author: dillo
"""
from Component import Component

class machine(object):
    
    
    def __init__(self,name, compList):
        self.compList = compList
        self.name = name
        #self.simList = []
        

    def go(self, env):
        
        from assetSim import assetSim
        simList = []
        
        #self.simList.append(assetSim(env,self.assetlist[0]))
        
        #add each 
        for i in range(len(self.compList)):
            simList.append(assetSim(env,self.compList[i], self.name))
            
        
        #for i in range(len(self.assetlist)):
            #print(self.assetlist[i].getName(), self.assetlist[i].getAge())
        
    def getName(self):
        return self.name
    
    def setList(self, lst):
        self.compList = lst
        
    def changeMaintenance(self, name, period):
        for x in range(len(self.compList)):
            
            if self.compList[x].getName() == name:
                self.compList[x].setMaintenancePeriod(period)
                
    def printAssetComponents(self):
        for x in range(len(self.compList)):
            print('Asset:' + self.name + '\n' + self.compList[x].toString())
            



#df = pd.DataFrame({'Maintenance?':['yes', 'no'], 'Hours Broken':[184,236]})
#ax = df.plot.bar(x='Maintenance?', y='Hours Broken', rot=0)


# =============================================================================
# #test changeMaintenance method
# import pandas as pd
# lst = []
# 
# lst.append(asset('engine', 800, 2000, 24))
# lst.append(asset('gearbox', 800, 2000, 24))
# lst.append(asset('ac', 800, 2000, 24))
# lst.append(asset('lights', 800, 2000, 24))
# 
# 
# machine1 = machine('Bmw', lst)
# machine1.printAssetComponents()
# machine1.changeMaintenance('engine', 48)
# machine1.changeMaintenance('lights', 8)
# 
# machine1.printAssetComponents()
# 
# =============================================================================
