# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:22:04 2022

@author: dillo
"""

from AssetGetter import AssetGetter    
from Fleet import Fleet
import simpy
import pandas as pd

class test():
    
    def createCSV(run, number):
        import os
        folder_Path = 'maintenance_tests' + '\\'+ 'test' + str(number) + '_output' + '.csv'
        run.to_csv(folder_Path)
    
    
    #def readCSV():
        


runs = []
periods = [4,8,12,16,20]
strPeriods = ['4','8','12','16','20']




for x in range(len(periods)):
    env = simpy.Environment()
    Runner1 = Fleet(AssetGetter.getList1())
    Runner1.run(env, periods[x])
    Runner1.editMachineMaintenance('Bmw', 'engine', periods[x])
    #print(type(Runner1.machineList[0]))
    env.run(until = 4381)
    run = AssetGetter.getList2('base', 'Bmw', 'engine_output')
    test.createCSV(run, x)
    
    runs.append(run['Status'].value_counts())
    

data = []

for x in range(len(runs)):
    data.append(runs[x].broken)

print(data)
from matplotlib import pyplot as plt
    
plt.bar(strPeriods, data)
plt.xlabel('working hours till maintained')
plt.ylabel('Failures')
plt.show()
    


    
