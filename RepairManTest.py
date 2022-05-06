# -*- coding: utf-8 -*-
"""
Created on Fri May  6 01:29:16 2022

@author: dillo
"""



from RepairMan import RepairMan

class TestRepairMan(object):
    
    def testName(self):
        try:
            man = RepairMan(23.3,'engine',1,50,True)
        except Exception as e:
            print("\nTest name type error:")
            print(e)
            pass
        
    def testTypee(self):
        try:
            man = RepairMan('norman',True,1,50,True)
        except Exception as e:
            print("\nTest type error:")
            print(e)
            pass
        
    def testSkillType(self):
        try:
            man = RepairMan('norman','engine',"ice",50,True)
        except Exception as e:
            print("\nTest type error:")
            print(e)
            pass
    
    def testSkillValue(self):
        try:
            man = RepairMan('norman','engine',4,50,True)
        except Exception as e:
            print("\nTest skill value error:")
            print(e)
            pass
    
    def testWageType(self):
        try:
            man = RepairMan('norman','engine',1,"hi",True)
        except Exception as e:
            print("\nTest wage type error:")
            print(e)
            pass
        
    def testWageValue(self):
        try:
            man = RepairMan('norman','engine',1,0,True)
        except Exception as e:
            print("\nTest wage value error:")
            print(e)
            pass
    
    def testAvailable(self):
        try:
            man = RepairMan('norman','engine',1,50,"banana")
        except Exception as e:
            print("\nTest type error:")
            print(e)
            pass
        
Test = TestRepairMan
Test.testName(Test)
Test.testTypee(Test)
Test.testSkillType(Test)
Test.testSkillValue(Test)
Test.testWageType(Test)
Test.testWageValue(Test)
Test.testAvailable(Test)


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