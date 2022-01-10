# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 11:18:28 2022

@author: subodh kumar
"""
import re
#import os
#os.chdir('path-of-input-text-file')

#function to parse data via regular expression and string manipulation
def parse_data(data):
    #empty lists 
    mod = []
    model=[]
    status=[]
    output_list = []
    
    #iterate over lines separated by \n
    for line in data.splitlines():
        #skip empty lines
        if line.strip() != "":
            line = re.sub("\s+", " ", line)
            mod.append(line.split()[0])
            model.append(line.split()[1])
            status.append(line.split()[2])
    
    #format output data        
    for i in range(2,len(mod)):
        element = f' "mod": {mod[i]}, "model": "{model[i]}", "status": "{status[i]}"'
        output_list.append( '{' + element + '}' )
    
    return output_list
    
#read text file in read mode
#assuming path of input text file is set correctly
with open('test.txt', 'r') as file:
    input_data = file.read()

output_data = parse_data(input_data)  
print(output_data)  