# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:49:01 2022

@author: dillo
"""


from assetGetter import assetGetter
from machine import machine
import simpy
import time

env = simpy.Environment()
global machList 
machList = ['hello', 'its me']

class Runner(object):
    
    def __init__(self, machineList):
        self.machineList = machineList
        self.machines = []
    
    def run(self):
          
        for index, row in self.machineList.iterrows():
            name = (row["Name"])
            self.machines.append(machine(name, assetGetter.getList(name)))
            
             
        #self.machines.append(machine(self.machineList[i]))    
        self.machineList = []
        for i in range(len(self.machines)):
            #print(self.machines[i].getName())
            self.machineList.append(assetGetter.convertToAsset(self.machines[i].getName()))
            self.machines[i].setList(self.machineList[i])
            print(self.machines[i].compList)
            self.machines[i].go(env)
            print(self.machineList[i])
            
    def getList(self, name):
        return assetGetter.convertToAsset(name)

    
from assetGetter import assetGetter    
Runner1 = Runner(assetGetter.getList1())
Runner1.run()    
#8760

total = 0
times = []

runs = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
for x in range(len(runs)):
    from assetGetter import assetGetter    
    Runner1 = Runner(assetGetter.getList1())
    Runner1.run()
    start = time.time()
    env.run(until=runs[x])
    end = time.time()    
    total = end - start
    times.append(total)

import matplotlib.pyplot as plt

# =============================================================================
# import csv
# folder_Path = 'test'
# path = folder_Path + '\\' + 'Bmw' + '\\' + 'gearbox_output' + '.csv'
# =============================================================================
import pandas as pd
ndf = pd.DataFrame(runs, columns=['hours'])
df = ndf.assign(times = times)

print(df)


plt.plot(df['hours'], df['times'])
plt.title('Running times')
plt.xlabel('Sim Time(hours)')
plt.ylabel('Time to run')
plt.grid(True)
plt.show()

# =============================================================================
# import matplotlib.pyplot as plt
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
