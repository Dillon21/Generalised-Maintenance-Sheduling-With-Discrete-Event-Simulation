# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:10:40 2022

@author: dillo
"""

class assetGetter():
    
    
    def getList(filename):
        import csv
        folder_Path = 'test' + '\\' + filename
        path = folder_Path + '\\' + filename + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
    
    def getList1():
        import csv
        folder_Path = 'test'
        path = folder_Path + '\\' + 'assets' + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
    
     
    def convertToAsset(name):
        lst = assetGetter.getList(name)
        lst.reset_index()
        assetList = []

        
        from asset import asset
        
        #needs optimisation not best way
        for index, row in lst.iterrows():
            name = row["Name"]
            age = row["Age"]
            maxAge = row["Maxage"]
            
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
                
            assetList.append(asset(str(row["Name"]), int(row["Age"]), int(row["Maxage"])))
            
        #for i in range(len(assetList)):
            #print(assetList[i].getName(), assetList[i].getAge())
        
        return assetList
    
    def convertToAsset1():
        lst = assetGetter.getList1()
        lst.reset_index()
        assetList = []

        
        from asset import asset
        
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
                
            assetList.append(asset(row["Name"], int(row["Age"]), int(row["Maxage"])))
            
        #for i in range(len(assetList)):
            #print(assetList[i].getName(), assetList[i].getAge())
        
        return assetList
    
#assetGetter.convertToAsset()




