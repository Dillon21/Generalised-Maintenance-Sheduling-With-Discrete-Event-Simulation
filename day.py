# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:59:23 2022

@author: dillo
"""

class day(object):
    workdayLength = 8
    nightLength = 16
    def __init__(self, hour):
        self.hour = hour
        #False = not working
        self.state = False
        
    def workDay(self):
        self.hour += 8
        
    
    def night(self):
        self.hour += 16
        
    def getHour(self):
        return self.hour
    
    def getNightLength(self):
        return self.nightLength
    
    def getDayLength(self):
        return self.workdayLength