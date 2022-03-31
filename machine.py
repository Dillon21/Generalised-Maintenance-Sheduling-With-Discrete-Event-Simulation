# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:35:50 2022

@author: dillo
"""
import simpy
env = simpy.Environment()

class machine(object):
    
    
    def __init__(self, assetlist):
        self.assetlist = assetlist
        #self.simList = []
        

    def go(self):
        
        from assetSim import assetSim
        simList = []
        #self.simList.append(assetSim(env,self.assetlist[0]))
        for i in range(len(self.assetlist)):
            simList.append(assetSim(env,self.assetlist[i]))
        
        
        #for i in range(len(self.assetlist)):
            #print(self.assetlist[i].getName(), self.assetlist[i].getAge())
        

from assetGetter import assetGetter    
machine1 = machine(assetGetter.convertToAsset())
machine1.go()
env.run(until=8761)
