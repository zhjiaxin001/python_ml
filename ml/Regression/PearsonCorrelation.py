import numpy as np
import math

def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR =0
    varX = 0
    varY =0
    for i in range(0, len(X)):
        diffXXbar = X[i]-xBar
        diffYYbar = Y[i]-yBar
        SSR += (diffXXbar*diffYYbar)
        varX += diffYYbar**2
        varY += diffXXbar**2
    SST = math.sqrt(varX * varY)
    return SSR / SST

def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat - ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['determination'] = ssreg/sstot
    return results





testX = [1, 3, 8, 7, 9]
testY = [10, 12, 24, 21, 34]
print('r:', computeCorrelation(testX, testY))
print polyfit(testX, testY, 1)['determination']