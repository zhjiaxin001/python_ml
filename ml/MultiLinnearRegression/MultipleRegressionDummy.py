# coding=utf-8
from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model
datePath = r"Delivery_Dummy.csv"
deliverData = genfromtxt(datePath, delimiter=',')
print 'data'
print deliverData

X = deliverData[:, : -1]
Y = deliverData[:, -1]

print 'X:'
print X

print 'Y:'
print Y

abc = linear_model.LinearRegression()
abc.fit(X, Y)
print(X.shape)
# print('coefficients:')
# print abc.coef_
# print 'intercept:'
# print abc.intercept_
xPred = [100,4,0,1,0]
yPred = abc.predict([xPred])
print 'y:'
print yPred
