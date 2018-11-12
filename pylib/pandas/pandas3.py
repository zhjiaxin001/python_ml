# -*- coding=utf-8 -*-
# axis=1 跨列 （across)    axis=0 跨行 （down)
import pandas as pd
import numpy as np

titanic_suivival = pd.read_csv('pandas/titanic_train.csv')
# print titanic_suivival.dtypes

passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_suivival[titanic_suivival['Pclass'] == this_class]
    pclass_fares = pclass_rows['Fare']
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
# print fares_by_class

passenger_survival = titanic_suivival.pivot_table(index='Pclass', values='Survived')
# print passenger_survival
passenger_age = titanic_suivival.pivot_table(index="Pclass", values="Age", aggfunc=np.mean)
# print passenger_age
srot_status = titanic_suivival.pivot_table(index='Embarked', values=['Fare', 'Survived'], aggfunc=np.sum)
# print srot_status
drop_na_columns = titanic_suivival.dropna(axis=1)
# print drop_na_columns
new_titanic_survival = titanic_suivival.dropna(axis=0, subset=['Age', 'Sex'])
# print new_titanic_survival

row_index_83_age = titanic_suivival.loc[83, 'Age']
# print row_index_83_age

new_titanic_survival = titanic_suivival.sort_values('Age', ascending=False)
# print new_titanic_survival[0:10]

titanic_reindexed = titanic_suivival.reset_index(drop=True)
# print titanic_reindexed.loc[0:10]

def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item
hundredth = titanic_suivival.apply(hundredth_row)
# print hundredth

def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
column_null_count = titanic_suivival.apply(not_null_count)
# print column_null_count

def which_class(row):
    # print row
    pclass = row['Pclass']
    if pd.isnull(pclass):
        return 'Unknow'
    elif pclass == 1:
        return 'First Class'
    elif pclass == 2:
        return 'Sencond Class'
    elif pclass == 3:
        return 'Third Class'
pclass = titanic_suivival.apply(which_class, axis=1)
# print pclass

def is_minor(row):
    age = row['Age']
    if pd.isnull(age):
        return 'Unknow'
    elif age<18:
        return 'minor'
    else:
        return 'adult'
age_labels = titanic_suivival.apply(is_minor,axis=1)
# print age_labels
titanic_suivival['age_labels'] = age_labels
age_group_survival = titanic_suivival.pivot_table(index='age_labels', values='Survived')

print age_group_survival