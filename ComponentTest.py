# -*- coding: utf-8 -*-
"""
Created on Fri May  6 02:09:05 2022

@author: dillo
"""
from Component import Component

class ComponentTest():
    
    #Input Boolean instead of string
    def testName(self):
        try:
            comp = Component(True,100,600,24)
        except Exception as e:
            print("\nTest name type error:")
            print(e)
            pass
        
    #Input boolean instead of integer
    def testAgeType(self):
        try:
            comp = Component('engine',True,600,24)
        except Exception as e:
            print("\nTest Age type error:")
            print(e)
            pass
        
    #input negative integer instead of positive integer    
    def testAgeValue(self):
        try:
            comp = Component('engine',-2,600,24)
        except Exception as e:
            print("\nTest Age type error:")
            print(e)
            pass
    
    #input boolean instead of integer     
    def testMaxAgeType(self):
        try:
            comp = Component('engine',True,600,24)
        except Exception as e:
            print("\nTest max age type error:")
            print(e)
            pass
    
    #input negative integer instead of positive integer
    def testMaxAgeValue(self):
        try:
            comp = Component('engine',-2,600,24)
        except Exception as e:
            print("\nTest max age type error:")
            print(e)
            pass
        
    #input boolean instead of integer   
    def testMaintnenaceType(self):
        try:
            comp = Component('engine',100,600,True)
        except Exception as e:
            print("\nTest name type error:")
            print(e)
            pass
    
    #input 0 instead of normal integer
    def testMaintenanceValue(self):
        try:
            comp = Component(True,100,600,0)
        except Exception as e:
            print("\nTest name type error:")
            print(e)
            pass
        

compTest = ComponentTest()
compTest.testName()
compTest.testAgeType()
compTest.testAgeValue()
compTest.testMaxAgeType()
compTest.testMaxAgeValue()
compTest.testMaintnenaceType()
compTest.testMaintenanceValue()