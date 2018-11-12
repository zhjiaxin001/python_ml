import pandas
food_info = pandas.read_csv("pandas/food_info.csv")
# print food_info
# print (type(food_info))
# print food_info.dtypes
# print help(pandas.read_csv)

# print food_info.head(2)
# print food_info.tail(3)
# print food_info.columns
# print food_info.shape
# print food_info.loc[1]

# object - For string values
# int - for interger balues
# float - for float values
# datatime - for time values
# bool -for boolean values

# print food_info.loc[1:2]
# ndb_col = food_info["NDB_No"]
# print ndb_col

# column = "NDB_No"
# ndb_col = food_info[column]
# print ndb_col

col_names = food_info.columns.tolist()
print col_names
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print gram_df.head(3)