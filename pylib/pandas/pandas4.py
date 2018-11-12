# -*- coding=utf-8 -*-
import pandas as pd
import numpy as np
fangdango = pd.read_csv('pandas/fandango_score_comparison.csv')
series_film = fangdango['FILM']
# print type(series_film)
# print series_film[0:5]
series_rt = fangdango['RottenTomatoes']
# print type(series_rt)
# print series_rt[0:5]
from pandas import Series
film_name = series_film.values
# print type(film_name)
rt_scores = series_rt.values
series_custom = Series(rt_scores, index=film_name)
# print series_custom
# print (series_custom[['Minions (2015)', 'Leviathan (2014)']])
# print series_custom[5:10]
original_index = series_custom.index.tolist()
# print original_index
# print series_custom
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
# print sorted_by_index
sc2 = series_custom.sort_index()
# print sc2
sc3 = series_custom.sort_values()
# print sc3

# print np.add(series_custom,series_custom).sort_values()

# print series_custom[series_custom>50]

rt_critiics = Series(fangdango['RottenTomatoes'].values, index=fangdango['FILM'])
rt_users = Series(fangdango['RottenTomatoes_User'].values, index=fangdango['FILM'])
rt_mean = (rt_critiics + rt_users)/2
print rt_mean