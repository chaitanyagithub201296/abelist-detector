#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:05:36 2022

@author: chaitanyakunapareddi
"""

''' importing packages '''

from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS,cross_origin
import json

'''reading job descriptions'''

prk_file ='/Users/chaitanyakunapareddi/Desktop/iconsult/AD-Local/oadbjobs.parquet'
db=pd.read_parquet(prk_file, engine='pyarrow')
db1=db[['SourceGUID','Company','Description','Title']]
db1 = db1.dropna(subset=['Description'])
db1=db1.head(5000)

''' reading master DB '''
file_name = ("master_db.xlsx")
global wordsData
wordsData = pd.read_excel(file_name)



''' setting up API '''

app = Flask(__name__)
'''
app_cors_config = {
  "methods": ["OPTIONS", "GET", "POST","PUT","DELETE"],
}
'''

api_cors_config = {
  "origins": "*",
  "allow_headers": 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers'
}

#CORS(app)
cors = CORS(app,resources={"/*": api_cors_config})
#app.config['CORS_HEADERS'] = 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers'
api = Api(app)

''' APIs '''

@app.route('/jobdesc',methods=['GET'])
def get():
    data = db1  
    dblength={'dblength':db1.shape[0]}
    data = data.to_dict()  # convert dataframe to dictionary
    return {'data': data,'dblength':dblength}, 200  # return data and 200 OK code
# methods go here
pass

@app.route('/worbotdetails',methods=['GET'])
def get_worddata():
    details=wordsData.shape[0]+1
    return {'details': details}, 200  # return data and 200 OK code
# methods go here
pass

@app.route('/locations',methods=['POST'])
def post():
    new_data=request.get_json()
    j_data = json.dumps(new_data)
    json_data=json.loads(j_data)
    df_json=pd.DataFrame(json_data,columns=json_data[0].keys())
    #print(df_json)
    df_json.columns=['ablesit words','suggestion words']
    #df_json.rename(columns={'abelistwords': 'ablesit words', 'alternatewords': 'suggestion words'}, inplace=True)
    print(df_json)
    new_data=wordsData.append(df_json,ignore_index=True)
    new_data.to_csv('wordsData.csv',index=False)

    return 'success', 200 # return data with 200 OK
pass
  

''' main function '''


if __name__ == '__main__':
    #app.run() 
    app.run(host='localhost',port=4300)








