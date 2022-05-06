# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:49:01 2022

@author: dillo
"""


from AssetGetter import AssetGetter
from machine import machine
import simpy
import time


#env = simpy.Environment()

class Fleet(object):
    
    def __init__(self, machineList):
        self.machineList = machineList
        self.machines = []
        self.location = 'base'
        
    def run(self,env, period):
            for index, row in self.machineList.iterrows():
                name = (row["Name"])
                self.machines.append(machine(name, AssetGetter.getList(name, self.location)))
            
            self.machineList = []
            for i in range(len(self.machines)):
                #print(self.machines[i].getName())
                if period == None:
                    self.machineList.append(self.getList(self.machines[i].getName(), self.location, None))
                    self.machines[i].setList(self.machineList[i])
                    #print(self.machines[i].compList)
                    self.machines[i].go(env)
                    #print(self.machineList[i])
                else:
                    self.machineList.append(self.getList(self.machines[i].getName(), self.location, period))
                    self.machines[i].setList(self.machineList[i])
                    #print(self.machines[i].compList)
                    self.machines[i].go(env)
                    #print(self.machineList[i])
                
    def getList(self, name, location, period):
        if period == None:
            return AssetGetter.convertToAsset(name,self.location)
        else:
            return AssetGetter.convertToAssets(name,self.location, period)
                
    
    def editMachineMaintenance(self,name,compName,newPeriod):
        for x in range(len(self.machines)):
            if self.machines[x].getName() == name:
                self.machines[x].changeMaintenance(compName, newPeriod)
                self.machines[x].printAssetComponents()
                
        
    #def printMachine(self):
        #for x in range(len(self.machines)):
        
                
    def printAllAssets(self):
        for x in self.machines:
            x.printAssetComponents()
            
    def setLocation(self, location):
        self.location = location
        
    def copyBase(self,location):
        from distutils.dir_util import copy_tree
        fromDirectory = 'base'
        toDirectory = 'tests\\' + location
        
        copy_tree(fromDirectory,toDirectory)
        
    def clearTestFolder(self):
        import os, shutil
        folder = 'maintenance_tests'
        for filename in os.listdir(folder):
            path = os.path.join(folder, filename)
            
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                    
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                    
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (path, e))
        

# =============================================================================
# Runner1 = Fleet(AssetGetter.getList1())
# Runner1.run()
# Runner1.editMachineMaintenance('Bmw', 'gearbox', 48)
# 
# Runner1.printAllAssets()
# env.run(until = 721)
# =============================================================================

#Runner1.clearTestFolder()
#Runner1.copyBase()
#print(Runner1.machineList)
#print(Runner1.machines)

  

#8760

total = 0
times = []

# =============================================================================
# runs = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
# for x in range(len(runs)):
#     from assetGetter import assetGetter    
#     Runner1 = Runner(assetGetter.getList1())
#     Runner1.run()
#     start = time.time()
#     env.run(until=runs[x])
#     end = time.time()    
#     total = end - start
#     times.append(total)
# 
# import matplotlib.pyplot as plt
# =============================================================================



# =============================================================================
# import pandas as pd
# df = pd.DataFrame(runs, columns=['hours'])
# df = df.assign(times = times)
# 
# print(df)
# 
# 
# plt.plot(df['hours'], df['times'])
# plt.title('Running times')
# plt.xlabel('Sim Time(hours)')
# plt.ylabel('Time to run')
# plt.grid(True)
# plt.show()
# =============================================================================

# =============================================================================
# import matplotlib.pyplot as plt
# 
# import csv
# folder_Path = 'test'
# path = folder_Path + '\\' + 'Bmw' + '\\' + 'gearbox_output' + '.csv'
# 
# path = folder_Path + '\\' + 'Toyota' + '.csv'
# import pandas as pd
# df = pd.read_csv(path)
# #df = df.iloc[500:1500]
# print(df)
# 
# 
# plt.plot(df['Hour'], df['Age wear'])
# plt.title('Toyota')
# plt.xlabel('Time(hours)')
# plt.ylabel('Level of wear')
# plt.grid(True)
# plt.show()
# =============================================================================

