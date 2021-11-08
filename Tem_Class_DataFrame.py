# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:05:33 2021

@author: ITDSCK
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:56:35 2021

@author: ITDSCK
"""

import pandas as pd
pd.set_option('display.max_columns', None)

from pandas.api.types import CategoricalDtype

import numpy as np

from time import time

import datetime

#%%

class Class_xxx():
    

    def __init__(self, df):
        
        self.df = df
        
        # call self function
        self.dp_df = self.Data_Processing()
    
    def Show_Columns_Name(self):
        print(f'df columns: {self.df.columns}')
    
    def Get_Processed_DataFrame(self):
        
        return self.dp_df
    
    def Data_Processing(self):
        
        # rename col
        
        # Data_Processing output
        return df
    
    def Stat(self):

        
        df = self.dp_df.copy()
        
        stat_df = df.groupby(['xxx']).agg({'col_1': ['size','count'], 'col_2': ['size','nunique']})
        print(stat_df, '\n')    
        print('-' * 20)
        return
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    

