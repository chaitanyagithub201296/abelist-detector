#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:14:33 2021

@author: chaitanyakunapareddi
"""

import pandas as pd
#importing pandas package
 
# Give the location of the file
file_name = ("/Users/chaitanyakunapareddi/Desktop/iconsult/ad/master_db.xlsx")
#location where the excel file is located.
#must be changed when run in local.

wordsData = pd.read_excel(file_name)

ableist_dictionary=[]
ableist_dictionary=wordsData['ablesit words']
suggestions_dictionary=wordsData['suggestion words']



text='I am an abnormal person and an addict and abnormal'
replacement_words=[]
words = text.split(' ')
rep_word=[]
for word in words:
    for ab in ableist_dictionary:
            if word == ab:
                rep_word.append(word)
                replacement_word = wordsData.loc[wordsData['ablesit words'] == word]['suggestion words']
                replacement_word=replacement_word.tolist()
                replacement_word=replacement_word[0].split(',')
                replacement_words.append(replacement_word)



solutiondf=pd.DataFrame()
solutiondf['ab word']=rep_word
solutiondf['sol word']=replacement_words
solutiondf.drop_duplicates(subset ='ab word',keep = 'first', inplace = True)



import language_tool_python
tool = language_tool_python.LanguageToolPublicAPI('en-US')
text2='i am atypical person impaired over control drug use'
tool.correct(text)

i=0
for line in text2:
        matches = tool.check(line)
        i = i + len(matches)     
        
print("No. of mistakes found in document is ", i)











