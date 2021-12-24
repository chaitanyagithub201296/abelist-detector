#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:41:32 2021

@author: chaitanyakunapareddi
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = "This is an example resume for a job"
reference = "This is an example reference for a job advertisement"
compare = [resume,reference]
cVect = CountVectorizer()
cMatrix = cVect.fit_transform(compare)

#prints how well the resume matches as a percentage
matPercent = cosine_similarity(cMatrix)[0][1] * 100
matPercent = round(matPercent, 2) # round to two decimal
print("Resume is a "+ str(matPercent)+ "% match to the job.")