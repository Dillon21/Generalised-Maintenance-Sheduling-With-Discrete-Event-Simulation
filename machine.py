# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:35:50 2022

@author: dillo
"""

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



#df = pd.DataFrame({'Maintenance?':['yes', 'no'], 'Hours Broken':[184,236]})
#ax = df.plot.bar(x='Maintenance?', y='Hours Broken', rot=0)


