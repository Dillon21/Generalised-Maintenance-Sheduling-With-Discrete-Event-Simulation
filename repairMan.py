# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 02:12:14 2022

@author: dillo
"""

from Component import Component

class RepairMan(object):
    
    def __init__(self, name,typee,skill,wage,available,asset):
        
        #Type check name
        if type(name) != str:
            raise TypeError("Name has to be a word, Check repairMan.csv in file name column")
        self.name = name
        
            
        #Type check typee
        if type(typee) != str:
            raise TypeError("Type field has to be a word")
        self.typee = typee
        
        #Type check and value check on skill
        if type(skill) != int:
            raise TypeError("Skill must be a whole number")
        if skill > 3 or skill <= 0:
            raise ValueError("Skill must be a number between 1 and 3")
        self.skill = skill
    
        #Type and Value Check wage
        if type(wage) != int and type(wage)!= float:
            raise TypeError(str(self.name) + "'s" + " Wage must be a number")        
        if wage > 0:
            self.wage = wage
        else:
            raise ValueError("Wage must be greater than 0, check repairMan.csv in wage column")   
            
        #Type check on available
        if type(available) != bool:
            raise TypeError("Available field has to equal TRUE or FALSE, check repairMan.csv in available column")
        self.available = available
        
        self.asset = asset
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getType(self):
        return self.typee
    
    def setType(self, typee):
        self.typee = typee
        
    def getSkill(self):
        return self.skill()
    
    def setSkill(self,skill):
        self.skill = skill
        
    def getWage(self):
        return self.wage()
    
    def setWage(self, wage):
        self.wage = wage
    
    def getAvail(self):
        return self.available
    
    def setAvail(self, status):
        self.available = status
        
    def getRepairMan(self, assetName):
        mech = 'engine'
        import pandas as pd
        df = pd.read_csv('base\\repair_man.csv')
        mech = df.loc[(df['Type'] == str(mech)) & (df['Available'] == True)]
        
        manList = []
        name = ''
        
        for index, row in mech.iterrows():
            manList.append(RepairMan(str(row['Name']), str(row['Type']), int(row['Skill']), int(row['Wage']), bool(row['Available']), str(row['Asset'])))
            
        #name = manList[0].getType()
        df.loc[df['Type'] == name, ['Available']] = 'FALSE'
        print(df)
        df.to_csv('base\\repair_man1.csv')
        manList[0].setAvail(False)
        return manList[0]
    
    
            
        
man = RepairMan('norman','engine',1,50,True,'Bmw')
man = man.getRepairMan('Bmw')

print(man.getAvail())   
        

#TEST EACH TYPE AND VALUE ERROR
# =============================================================================
# #get name type error        
# man = repairMan(23.3,'engine',1,50,True)
# 
# #get type type error
# man = repairMan('norman',True,1,50,True)
# 
# #get skill type and value error
# man = repairMan('norman','engine',"ice",50,True)
# man = repairMan('norman','engine',4,50,True)
# 
# #get wage type and value error
# man = repairMan('norman','engine',1,"hi",True)
# man = repairMan('norman','engine',1,0,True)
#         
# #get available type error
# man = repairMan('norman','engine',1,50,"banana")
# =============================================================================


