#  coding=utf-8
import numpy as np
import random

def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x,theta)
        loss = hypothesis - y
        cost = np.sum(loss**2)/(2*m)
        print ("Iteration %d  |  cost %f"% (i, cost))
        gradient = np.dot(xTrans, loss)/m
        theta = theta - alpha*gradient
    return theta

#variance :方差
def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        # our target variable
        y[i] = (i+bias)+random.uniform(0, 1)*variance
    return x,y
x, y = genData(100, 25, 10)
print('x:')
print(x)
print('y:')
print(y)

m, n = np.shape(x)
m_y= np.shape(y)

print ('x shape')
print (m)
print (n)
print ('y shape')
print (m_y)


numIterations = 100000
alpha = 0.0005
theta = np.ones(n)
theta =  gradientDescent(x, y, theta, alpha, m, numIterations)
print theta
