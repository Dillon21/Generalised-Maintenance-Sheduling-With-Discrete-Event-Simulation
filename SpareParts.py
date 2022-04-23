# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:16:55 2022

@author: dillo
"""
import csv
import pandas as pd

class SpareParts(object):
    def __init__(self,):
        self.path = 'test' + '\\' + 'parts' + '.csv'
        self.df = pd.read_csv(self.path)
        
    def newParts(df):
        self.df = df
        self.df.to_csv(self.path)
            
    def getParts():
        return self.df
    
    
import time

for i in range (1000):
    print (round(time.time() * 1000))
    
    