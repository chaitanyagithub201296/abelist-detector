#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:05:36 2022

@author: chaitanyakunapareddi
"""


#while



from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS,cross_origin
import json



prk_file ='/Users/chaitanyakunapareddi/Desktop/iconsult/AD-Local/oadbjobs.parquet'
db=pd.read_parquet(prk_file, engine='pyarrow')
db.head(10)

db1=db.head(10)
db1=db1[['SourceGUID','Company','Description','Title']]


file_name = ("/Users/chaitanyakunapareddi/Desktop/iconsult/AD-Local/master_db.xlsx")
wordsData = pd.read_excel(file_name)


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



@app.route('/jobdesc',methods=['GET'])
def get():
    data = db1  # read CSV
    data = data.to_dict()  # convert dataframe to dictionary
    return {'data': data}, 200  # return data and 200 OK code
# methods go here
pass


somelist=[]
@app.route('/locations',methods=['POST'])
def post():
    new_data=request.get_json()
    j_data = json.dumps(new_data)
    json_data=json.loads(j_data)
    df_json=pd.DataFrame(json_data,columns=json_data[0].keys())
    print(df_json)
    # add the newly provided values
    wordsData.append(df_json,ignore_index=True)
    # save back to CSV
    wordsData.to_excel('/Users/chaitanyakunapareddi/Desktop/iconsult/AD-Local/master_db.xlsx')
    #somelist.append(df_json)
        

    return 'success', 200 # return data with 200 OK
pass
  

'''
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        print('Received from client: {}'.format(request.get_json() ))
        data = request.get_json()  # Get data posted as a json
        j_data = json.dumps(data)
        json_data=json.loads(j_data)
        df_json=pd.DataFrame(json_data,columns=json_data[0].keys())
        df_json=data_preprocess(df_json)
        y_pred=pickle_file['model'].predict(df_json)
        pred=[]
        for i in range(len(y_pred)):
                pred.append(str(pickle_file['label'][y_pred[i]]))
        print(pred)
    return str(pred)

'''




if __name__ == '__main__':
    #app.run() 
    app.run(host='localhost',port=4300)








