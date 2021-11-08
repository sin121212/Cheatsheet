# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:00:36 2021

@author: ITDSCK
"""


import turbodbc

import pyodbc
from sqlalchemy import create_engine
import urllib

#%%

class Class_DB_Engine():
    
    def __init__(self):
        
        pass

    def AS400(self, driver, system, uid, pwd):
    
        # https://stackoverflow.com/questions/35461388/connecting-to-ibm-as400-server-for-database-operations-hangs        
        print('Create Database engine for AS400:')
        
        # {iSeries Access ODBC Driver}
        
        con = turbodbc.connect(
            driver=driver,
            system=system,
            uid=uid,
            pwd=pwd)
                    
        # set autocommit here -> for make change in database
        con.autocommit = True
        print(f'autocommit mode: {con.autocommit}')
        
        return con
    
    def SQL_Server(self, driver, server, port, db_name, uid, pwd):
        
        print('Create Database engine for SQL Server:')
        
        # {ODBC Driver 17 for SQL Server}
        
        params = urllib.parse.quote_plus(f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={db_name};UID={uid};PWD={pwd}')
        
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, fast_executemany=True)
    
        return engine
    
    