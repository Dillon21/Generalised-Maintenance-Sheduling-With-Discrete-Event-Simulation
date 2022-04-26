# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:10:40 2022

@author: dillo
"""

class assetGetter():
    
    
    def getList(filename):
        import csv
        folder_Path = 'test'
        path = folder_Path + '\\' + filename + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
     
    def convertToAsset():
        lst = assetGetter.getList('assets')
        lst.reset_index()
        assetList = []
        
        from asset import asset
        
        #needs optimisation not best way
        for index, row in lst.iterrows():
            
            assetList.append(asset(row["Name"], int(row["Age"]), int(row["Maxage"])))
        
        #for i in range(len(assetList)):
            #print(assetList[i].getName(), assetList[i].getAge())
        
        return assetList
    
assetGetter.convertToAsset()




