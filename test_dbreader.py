#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:14:05 2021

@author: chaitanyakunapareddi
"""

import pyodbc
 
server = 'localhost' 
database = 'demo' 
username = 'sa' 
password = 'SU2orange!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=myserver;Database=mydatabase;Port=myport;User ID=myuserid;Password=mypassword')
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row:
    print(row[0])
    row = cursor.fetchone()