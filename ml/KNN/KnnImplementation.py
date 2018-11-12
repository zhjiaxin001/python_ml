#  -*- coding=utf-8 -*-
import csv
import math
import random
import operator

def loadDataset(filenam, split, trainingSet=[], testSet=[]):
    with open(filenam, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclidanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    print 'testInstance'+str(testInstance)
    lenth = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclidanDistance(trainingSet[x], testInstance, lenth)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes ={}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedClassVotes = sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassVotes[0][0]

def getAccyract(testSetm, predictions):
    correct = 0
    for x in range(len(testSetm)):
        if testSetm[x][-1] == predictions[x]:
            correct +=1
    return (correct/float(len(testSetm)))*100.0

def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'irisdata.txt', split, trainingSet, testSet)
    print ('trainSet:'+ repr(len(trainingSet)))
    print ('testSet:' + repr(len(testSet)))
    predictions = []
    k =3
    # print repr(trainingSet)
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted='+repr(result)+',actual=', repr(testSet[x][-1]))
    accyract = getAccyract(testSet, predictions)
    print ('accyract:'+ repr(accyract)+'%')
main()

