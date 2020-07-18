# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:09:37 2020

@author: JOTA
"""
import csv
filename="chamba"
with open(filename) as f:
    reader=csv.reader(f)
    header=next(reader)

    print(header)
    

