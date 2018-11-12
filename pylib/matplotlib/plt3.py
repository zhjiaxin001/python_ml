import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
reviews = pd.read_csv('plt/fandango_scores.csv')
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[num_cols]
# print norm_reviews[:1]
bar_heights = norm_reviews.ix[0, num_cols].values
print bar_heights
bar_position = arange(5) + 0.75
tick_positions = range(1, 6)
fig, ax = plt.subplots()
ax.bar(bar_position, bar_heights, 0.6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=45)
ax.set_xlabel('Rating Source')
ax.set_ylabel('Averange Rating')
ax.set_title('Averange User Rating For Averangers: Age of Ultron (2015)')

plt.show()


bar_heights = norm_reviews.ix[0, num_cols].values
# print bar_heights
bar_position = arange(5) + 0.75
tick_positions = range(1, 6)
fig, ax = plt.subplots()
ax.barh(bar_position, bar_heights, 0.6)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols, rotation=45)
ax.set_ylabel('Rating Source')
ax.set_xlabel('Averange Rating')
ax.set_title('Averange User Rating For Averangers: Age of Ultron (2015)')

plt.show()
fig, ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['Metacritic_user_nom'])
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()
