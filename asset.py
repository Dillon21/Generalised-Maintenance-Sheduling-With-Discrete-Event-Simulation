# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:35:47 2022

@author: dillo
"""

class asset(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def setName(self,name):
        self.name = name
    
    def setAge(self,age):
        self.age = age
        
    def getName(self):
        return self.name
       
    def getAge(self):
        return self.age