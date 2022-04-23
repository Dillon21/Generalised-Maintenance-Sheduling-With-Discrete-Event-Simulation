# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 02:12:14 2022

@author: dillo
"""

from asset import asset

class repairMan(object):
    def __init__(self,skill,wage):
        if skill > 3 or 0:
            
        self.skill = skill
        self.wage = wage
        
    def getWage():
        return self.wage()
    
    def setWage(wage):
        self.wage = wage
    
    def getSkill():
        return self.skill()
    
    def setSkill(skill):
        self.skill = skill
    
    def calcRepairTime(asset):
        
        