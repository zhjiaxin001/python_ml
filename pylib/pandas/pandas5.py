import pandas as pd
import numpy as np
fandango = pd.read_csv('pandas/fandango_score_comparison.csv')
# print type(fandango)
fandango_films = fandango.set_index('FILM', drop=False)
# print fandango_films
# print fandango_films['Avengers: Age of Ultron (2015)':'Hot Tub Time Machine 2 (2015)']
# print fandango_films.loc['Avengers: Age of Ultron (2015)':'Hot Tub Time Machine 2 (2015)']
types = fandango_films.dtypes
float_columns = types[types.values == 'float64'].index
print float_columns
float_df = fandango_films[float_columns]
print float_df
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_user.apply(lambda x: np.std(x), axis=1)


