# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:35:50 2022

@author: dillo
"""


class machine(object):
    
    
    def __init__(self, assetlist):
        self.assetlist = assetlist
        #self.simList = []
        

    def go(self,env):
        
        from assetSim import assetSim
        simList = []
        #self.simList.append(assetSim(env,self.assetlist[0]))
        print(len(self.assetlist))
        for i in range(len(self.assetlist)):
            simList.append(assetSim(env,self.assetlist[i]))
            
        
        #for i in range(len(self.assetlist)):
            #print(self.assetlist[i].getName(), self.assetlist[i].getAge())
        
        
import simpy
env = simpy.Environment()
from assetGetter import assetGetter
machine1 = machine(assetGetter.convertToAsset1())
machine1.go(env)
#env.run(until=8761)

import matplotlib.pyplot as plt

import csv
folder_Path = 'test'
path = folder_Path + '\\' + 'Bmw' + '.csv'
import pandas as pd
df = pd.read_csv(path)
df = df.iloc[500:1500]
print(df)


plt.plot(df['Hour'], df['Age wear'])
plt.title('Machine')
plt.xlabel('Time(hours)')
plt.ylabel('Level of wear')
plt.grid(True)
plt.show()

#df = pd.DataFrame({'Maintenance?':['yes', 'no'], 'Hours Broken':[184,236]})
#ax = df.plot.bar(x='Maintenance?', y='Hours Broken', rot=0)


