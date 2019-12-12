# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:16:41 2019

@author: suraj
"""

##Import packages
import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize

##Read the json file
filename = 'eb-response-page1.json'
with open(filename, 'r') as myfile:
    data=myfile.read()

datafile = json.loads(data)

#Convert to pandas df for easy analysis
Data = pd.DataFrame.from_dict(json_normalize(datafile['events']), orient='columns').drop_duplicates()  
n = Data.shape[1]

#Export to a file
#Data.drop_duplicates().to_csv('Cleaned_json.csv', index=False)  

#Read the activites file
Activities = pd.read_csv('Activities.csv')
myDict = Activities.set_index('Category')['Keywords'].to_dict()

#Create dummy vars for categories
for i in range(len(myDict.keys())):
    Data[list(myDict.keys())[i]] = np.where(Data['name.text'].str.contains(list(myDict.values())[i], case=False), 1, 0)
    
#Adding the category column
s = np.where(Data.iloc[:,n:], ['{}, '.format(x) for x in Data.iloc[:,61:].columns], '')
Data['Category'] = pd.Series([''.join(x).strip(', ') for x in s], index=Data.index) 

#Getting original data
cols = Data.iloc[:,:n].columns.tolist()
cols.append('Category')
Data = Data[cols]

#Export the final file
Data.to_csv('Output.csv', index=False)