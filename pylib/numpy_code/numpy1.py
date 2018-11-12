# -*- coding:utf-8 -*-
import pylib.numpy

# world_alcehol = numpy.genfromtxt("numpy/world_alcohol.txt", delimiter=",", dtype=str)
# print (type(world_alcehol))
# print (world_alcehol)
# print ( help(numpy.genfromtxt))

# vector = numpy.array([5, 10, "15"])
# matrix = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2]])
# print vector
# print matrix
# numpy.array里面必须是相同的结构
# print (vector.shape)
# print (matrix.shape)

# print (vector)
# print (vector.dtype)


# world_alcehol = numpy.genfromtxt("numpy/world_alcohol.txt", delimiter=",", dtype=str)
# print world_alcehol
# print world_alcehol[1, 3]
# print world_alcehol[2, 2]

# 冒号一种定义为表示取所有的
vector = pylib.numpy.array([5, 10, "15"])
matrix = pylib.numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2]])
print vector[0:2]
print matrix[:, -1]
