# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 11:23:23 2022

@author: subodh kumar
"""

import pandas as pd
#import os
#os.chdir('path-of-input-text-file')

#read input file with fixed width
#Note: we can also use either of "colspecs" or "widths" specifically
#inspite of depending on function to infer automatically like below
#assuming path of input text file is set correctly
df = pd.read_fwf('test.txt', skiprows=3, names=['mod', 'model', 'status'],
                 colspecs='infer', widths=None, infer_nrows=100)

#remove those rows, which has NA for all columns present in dataframe df
df = df.dropna(axis = 0, how = 'all')

#reset index
df.reset_index(drop=True, inplace=True)

#while reading text file using read_fwf function, mod column is converted to float
#below line converts float to int
df["mod"] = df["mod"].astype('int')

#display dataframe rows as list, containing dictionary as elements
print(df.to_dict('records'))
#print(str(df.to_dict('records')).replace("'",'"'))