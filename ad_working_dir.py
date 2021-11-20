#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:14:33 2021

@author: chaitanyakunapareddi
"""

import xlrd
#package to read excel files in python
 
# Give the location of the file
loc = ("/Users/chaitanyakunapareddi/Desktop/iconsult/ad/master_db.xlsx")
#location where the excel file is located.
#must be changed when run in local.
 
# To open Workbook
wb = xlrd.open_workbook(loc)
#to create an object of workbook.
#this will help access the objects/functions for sheet.
sheet_ab = wb.sheet_by_name('ableist')
sheet_sg = wb.sheet_by_name('suggestions')
#reading the two sheets.


ableist_dictionary=[]
#creating an array to store ableist words.
for i in range(sheet_ab.nrows):
    ableist_dictionary.append(sheet_ab.cell_value(i, 0))
#iterate over the sheet to read all words.  

 
suggestions_dictionary=[]
#creating an array to store suggestion words.
for i in range(sheet_sg.nrows):
    suggestions_dictionary.append(sheet_sg.cell_value(i, 0))
#iterate over the sheet to read all words.  

















