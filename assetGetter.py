# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:10:40 2022

@author: dillo
"""

class AssetGetter():
    
    
    def getList(filename,location):
        import csv
        folder_Path = location + '\\' + filename
        path = folder_Path + '\\' + filename + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
    
    def getList1():
        import csv
        folder_Path = 'base'
        path = folder_Path + '\\' + 'assets' + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
    
    def getList2(location,assetName,compName):
        import csv
        folder_Path = location + '\\' + assetName
        path = folder_Path + '\\' + compName + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
    
     
    def convertToAsset(name,location):
        lst = AssetGetter.getList(name,location)
        lst.reset_index()
        assetList = []

        
        from Component import Component
        
        #needs optimisation not best way
        for index, row in lst.iterrows():
            name = row["Name"]
            age = row["Age"]
            maxAge = row["Maxage"]
            mPeriod = row["Mperiod"]
            
            if type(name) not in [str]:
                raise TypeError("Name cannot be a number on its own")
            
            if type(age) not in [int]:
                raise TypeError("Age must be an integer in hours")
            if age < 0:
                raise ValueError("Age cannot be negative")
            
            if type(maxAge) not in [int]:
                raise TypeError("Max age must be an integer in hours")
            if maxAge < 0:
                raise ValueError("Max age cannot be negative")
                
            if type(mPeriod) not in [int]:
                raise TypeError("Maintenance period must be an integer in hours")
            if mPeriod < 0:
                raise ValueError("Maintenance period cannot be negative")    
                
            assetList.append(Component(str(row["Name"]), int(row["Age"]), int(row["Maxage"]), int(row["Mperiod"])))
            
        #for i in range(len(assetList)):
            #print(assetList[i].getName(), assetList[i].getAge())
        
        return assetList
    
    def convertToAssets(name,location,period):
        lst = AssetGetter.getList(name,location)
        lst.reset_index()
        assetList = []

        
        from Component import Component
        
        #needs optimisation not best way
        for index, row in lst.iterrows():
            name = row["Name"]
            age = row["Age"]
            maxAge = row["Maxage"]
            mPeriod = row["Mperiod"]
            
            if type(name) not in [str]:
                raise TypeError("Name cannot be a number on its own")
            
            if type(age) not in [int]:
                raise TypeError("Age must be an integer in hours")
            if age < 0:
                raise ValueError("Age cannot be negative")
            
            if type(maxAge) not in [int]:
                raise TypeError("Max age must be an integer in hours")
            if maxAge < 0:
                raise ValueError("Max age cannot be negative")
                
            if type(mPeriod) not in [int]:
                raise TypeError("Maintenance period must be an integer in hours")
            if mPeriod < 0:
                raise ValueError("Maintenance period cannot be negative")    
            print('MPERIODS = ' + str(period))
                
            assetList.append(Component(str(row["Name"]), int(row["Age"]), int(row["Maxage"]), period))
            
        #for i in range(len(assetList)):
            #print(assetList[i].getName(), assetList[i].getAge())
        
        return assetList
    
    def convertToAsset1():
        lst = AssetGetter.getList1()
        lst.reset_index()
        assetList = []

        
        from Component import Component
        
        #needs optimisation not best way
        for index, row in lst.iterrows():
            name = row["Name"]
            age = row["Age"]
            maxAge = row["Maxage"]
            
            if type(name) not in [str]:
                raise ValueError("Name cannot be a number on its own")
            if type(age) not in [int]:
                raise ValueError("Age must be an integer in hours")
            if type(maxAge)not in [int]:
                raise ValueError("max age must be an integer in hours")
                
            assetList.append(Component(row["Name"], int(row["Age"]), int(row["Maxage"])))
            
        #for i in range(len(assetList)):
            #print(assetList[i].getName(), assetList[i].getAge())
        
        return assetList
    

        
 
    
#assetGetter.convertToAsset()




