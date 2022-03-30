# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:10:40 2022

@author: dillo
"""

class assetGetter():
    
    
    def getList():
        import csv
        folder_Path = 'test'
        path = folder_Path + '\\' + 'assets' + '.csv'
        
        import pandas as pd
        df = pd.read_csv(path)
        
        return df
     
    def convertToAsset():
        lst = assetGetter.getList()
        lst.reset_index()
        print(lst)
        assetList = []
        
        from asset import asset
        
        #needs optimisation not best way
        for index, row in df.iterrows():
            print(row["c1"], row["c2"])
        
        for i in range(len(assetList)):
            print(assetList[i].getName(), assetList[i].getA)
        

assetGetter.convertToAsset()




