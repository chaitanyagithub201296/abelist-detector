#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:09:32 2021

@author: chaitanyakunapareddi
"""

# Import Pandas
import pandas as pd

# Load Movies Metadata
metadata = pd.read_excel('/Users/chaitanyakunapareddi/Desktop/iconsult/ml-latest-small/reco_data.xlsx')

# Print the first three rows
metadata.head(3)


total_average = metadata['select avg'].mean()
print(total_average)

total_count = metadata['select count'].quantile(0.90)
print(total_count)

total_count_avg = metadata['select count'].mean()
print(total_count_avg)

#average count based recommender.
samplewords= metadata.copy().loc[metadata['select count'] >= total_count_avg]
samplewords.shape



def weighted_rating(x, m=total_count, C=total_average):
    v = x['select count']
    R = x['select avg']
    return (v/(v+m) * R) + (m/(m+v) * C)

samplewords['score'] = samplewords.apply(weighted_rating, axis=1)
samplewords = samplewords.sort_values('score', ascending=False)
samplewords[['ablesit words', 'select count', 'select avg', 'score']].head(10)


######################################################

#content- based recommender

metadata['ablesit words'].head()


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(metadata['syn'])
tfidf_matrix.shape


from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(metadata.index, index=metadata['ablesit words']).drop_duplicates()

def get_recommendations(val, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[val]
    # Get the pairwsie similarity scores of all words with that word
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the words based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar words
    sim_scores = sim_scores[1:3]
    # Get the word indices
    word_indices = [i[0] for i in sim_scores]
    return metadata['ablesit words'].iloc[word_indices]


get_recommendations('wild')
get_recommendations('silly')

























