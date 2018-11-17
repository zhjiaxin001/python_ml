import numpy as np


def kmeans(x, k, maxIt):
    numPoints, numDim = x.shape

    dataSet = np.zeros((numPoints, numDim+1))
    dataSet[:, :-1] = x

    rangint = np.random.randint(numPoints, size=k)
    while len(rangint)!=len(set(rangint)):
        rangint = np.random.randint(numPoints, size=k)
    centroids = dataSet[rangint, :]
    centroids[:, -1] = range(1, k+1)
    # print rangint
    iterations = 0
    oldCentroids = None

    while not shouldStop(oldCentroids, centroids,iterations, maxIt):
        print('iteration: \n:', iterations)
        print('dataSet: \n:', dataSet)
        print('centroids \n:', centroids)
        oldCentroids = np.copy(centroids)
        iterations += 1
        updateLabels(dataSet,centroids)
        centroids = getCentroids(dataSet, k)
    return dataSet


def shouldStop(oldCentroids, centroids,iterations, maxIt):
    if iterations>maxIt:
        return True
    return np.array_equal(oldCentroids, centroids)
def updateLabels(dataSet, centeoids):
    numPoints, numDim = dataSet.shape
    for i in range(0,numPoints):
        dataSet[i, -1] = getLabelFromClosestCentroid(dataSet[i, :-1], centeoids)

def getLabelFromClosestCentroid(dataSetRow, centroids):
    label = centroids[0, -1]
    minDist = np.linalg.norm(dataSetRow - centroids[0, :-1])
    for i in range(1,centroids.shape[0]):
        dist = np.linalg.norm(dataSetRow - centroids[i, :-1])
        if dist<minDist:
            minDist = dist
            label = centroids[i, -1]
    print('minDist:', minDist)
    return label

def getCentroids(dataSet, k):
    result = np.zeros((k, dataSet.shape[1]))
    for i in range(1, k+1):
        oneCluster = dataSet[dataSet[:, -1] == i, :-1]
        result[i-1, :-1] = np.mean(oneCluster, axis=0)
        result[i-1, -1] = i
    return result


x1 = np.array([1, 1])
x2 = np.array([2, 1])
x3 = np.array([4, 3])
x4 = np.array([5, 4])
testX = np.vstack((x1, x2, x3, x4))

result = kmeans(testX, 2, 10)
print ('final result :', result)
