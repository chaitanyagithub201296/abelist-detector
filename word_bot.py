#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:01:39 2021

@author: chaitanyakunapareddi
"""


#importing packages
import pandas as pd
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
from nltk.stem import WordNetLemmatizer 
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


text='I am an abnormal person and an addict and abnormal. there are 14 deaf and dumb applicants.'


# converting the paragraphs into sentences
tokens_sents = nltk.sent_tokenize(text)
print(tokens_sents)

#collection=pd.DataFrame()
collection=[]
collection2=[]
collection3=[]
collectiondf=pd.DataFrame()
for token in tokens_sents:
    print(token)
    data_word=input(' enter the ablesit word :')
    data_word2=input(' enter the suggestion word word :')
    collection.append(data_word)
    collection2.append(data_word2)
    collection3.append(token)
    


collectiondf['word']=collection
collectiondf['alter']=collection2
collectiondf['text']=collection3

abc=collectiondf.groupby(by='word',axis=1)


#converting sentences to words.
#tokens_words = nltk.word_tokenize(text)
#print(tokens_words)



###########################################################


#check if the word exists in the sentence.
















