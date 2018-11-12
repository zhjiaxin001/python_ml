import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
reviews = pd.read_csv('plt/fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
# print norm_reviews[:5]

fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()
fandango_distribution = fandango_distribution.sort_index()
imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = imdb_distribution.sort_index()
# print fandango_distribution
# print imdb_distribution
fig, ax = plt.subplots()
# ax.hist(norm_reviews['Fandango_Ratingvalue'])
# ax.hist(norm_reviews['Fandango_Ratingvalue'], bins=20)
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(4, 5), bins=20)
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(4, 1, 1)
ax2 = fig.add_subplot(4, 1, 2)
ax3 = fig.add_subplot(4, 1, 3)
ax4 = fig.add_subplot(4, 1, 4)
ax1.hist()


