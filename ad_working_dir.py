#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:14:33 2021

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

 
# Give the location of the file
#location where the excel file is located.
#must be changed when run in local.
file_name = ("/Users/chaitanyakunapareddi/Desktop/iconsult/AD-Local/master_db.xlsx")



#reading the excel file 
wordsData = pd.read_excel(file_name)


#creating a local array - dictionary of words from the excel.
ableist_dictionary=[]
ableist_dictionary=wordsData['ablesit words']
suggestions_dictionary=wordsData['suggestion words']


#text file (JD)
text='I am an abnormal person and an addict and abnormal. there are 14 deaf and dumb applicants.'


# converting the paragraphs into sentences
tokens_sents = nltk.sent_tokenize(text)
print(tokens_sents)
#converting sentences to words.
tokens_words = nltk.word_tokenize(text)
print(tokens_words)

#punct_words=['.']

#removing stopwordsf= from JD
filtered_sentence = []
filtered_sentence = [w for w in tokens_words if w.lower() not in stop_words]
filtered_sentence = [w for w in filtered_sentence if w.isalnum()]


'''
from nltk.stem import PorterStemmer

ps = PorterStemmer()
for word in tokens_words:
    stem_word=ps.stem(word)
    print(stem_word)
 '''   

#lemmeting the words to get root word.
lemmatizer = WordNetLemmatizer()
for word in tokens_words:
    lemm_word=lemmatizer.lemmatize(word)
    print(lemm_word)

#printing POS for each word - (for future R&D)
print("Parts of Speech: ",nltk.pos_tag(tokens_words))
#joining the lemmatized words back to sentence.
lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in tokens_words])
print(lemmatized_output)
    
    
#to detect the ableist word by matching it with masterDB 
#suggesting out alternate word.   
replacement_words=[]
words = text.split(' ')
rep_word=[]

## Function to replace the ableist words with the new replacement words
for word in words: 
    for ab in ableist_dictionary:
            if word == ab:
                rep_word.append(word) ## Inserting the replacement word into the replacement words list.
                replacement_word = wordsData.loc[wordsData['ablesit words'] == word]['suggestion words'] ## Fetching the replacement word for ableist words from the database.
                replacement_word=replacement_word.tolist() ## including the replacement words list from the database column.
                replacement_word=replacement_word[0].split(',') 
                replacement_words.append(replacement_word)


#creating a solution set for each ableist word.
#adding suggestion across each word.
solutiondf=pd.DataFrame()
solutiondf['ab word']=rep_word
solutiondf['sol word']=replacement_words
solutiondf.drop_duplicates(subset ='ab word',keep = 'first', inplace = True)



###################  R & D ##########################

import language_tool_python
tool = language_tool_python.LanguageToolPublicAPI('en-US')
text2='i am atypical person impaired over control drug use'
tool.correct(text)

i=0
for line in text2:
        matches = tool.check(line)
        i = i + len(matches)     
        
print("No. of mistakes found in document is ", i)


###################  R & D ##########################







