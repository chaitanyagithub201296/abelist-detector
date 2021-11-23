# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 23:07:19 2021

@author: Rahul Khairnar
"""

import pandas as pd ## IMPORTING PANDAS TO GET THE EXCEL SHEET AS A DATAFRAME INTO THE CODE

demo_db = pd.read_excel("demo_db.xlsx") ## SAMPLE DEMO DATABASE
ableist_words = demo_db["FIRST NAME"].tolist() ## CONVERTING A DATAFRAME COLUMN INTO A LIST

words_list= [] ## EMPTY LIST TO SPLIT A STRING INTO WORDS
replacement_words_dict = {} ## STORUNG THE FOUND ABLEIST WORDS AND THEIR REPLACEMENTS AFTER THEY ARE FETCHED FROM THE DATAFRAME

## FUNCTION TO REPLACE THE ABLEIST WORDS
def find_and_replace(x):
    words = x.split(" ") ## SPLITTING THE SENTENCE INTO WORDS
    for i in words: ## ITERATING ON EACH WORD
        if i in ableist_words: ## CHECKING IF WORD IS AN ABLEIST WORD BY CHECKING ITS PRESENCE IN THE ABLEIST WORDS LIST
            replacement_word = str(demo_db["LAST NAME"][demo_db["FIRST NAME"] == i]).split("    ")[1] ## FINDING ITS REPLACEMENT WORD FROM THE DATAFRAME.
            replacement_words_dict[i] = replacement_word.split("\n")[0].strip() ## STORING THE REPLACEMENT WORD IN THE DICTIONARY 
            return x.replace(i,replacement_words_dict[i]) ## REPLACING THE ABLEIST WORD WITH A REPLACEMENT WORD AND RETURNING IT
        
    
print(find_and_replace("I am ABC Khairnar ABC")) ## TO CHECK THE FUNCTION