# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 17:16:08 2022

@author: dillo
"""
import asset

car1 = asset.asset("ford",5,0)
Break = False


for x in range(10):
    print(car1.deteriorate(car1))
    