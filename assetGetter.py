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
        for row in lst.itertuples(index=True, name='Pandas'):
            print(row.Name, row.Age)
        
        for i in range(len(assetList)):
            print(assetList[i].getName())
        

assetGetter.convertToAsset()




