# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 10:48:28 2022

@author: subodh kumar
"""
#import os
#os.chdir('path-of-input-text-file')

#function to parse data via string manipulation
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
            mod.append(line[:3].strip())
            model.append(line[4:25].strip())
            status.append(line[26:].strip())
    
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