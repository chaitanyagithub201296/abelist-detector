#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:15:17 2021

@author: chaitanyakunapareddi
"""


import pandas as pd

prk_file ='/Users/chaitanyakunapareddi/Desktop/iconsult/AD-Local/oadbjobs.parquet'
db=pd.read_parquet(prk_file, engine='pyarrow')
db.head(10)

db1=db.head(10)


db1=db1[['SourceGUID','Company','Description','Title']]

#remove  nulls