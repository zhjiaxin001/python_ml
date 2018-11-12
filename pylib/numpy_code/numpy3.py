# -*- coding:utf-8 -*-
import numpy as np

# a = np.arange(0, 15)
# print (a)
# a = a.reshape(3, 5)
# print (a)
# print (a.shape)
# print (a.ndim)
# print (a.dtype.name)
# print (a.size)


# b = np.zeros((3, 4))
# print (b)
#
# c = np.ones((2, 3, 4),dtype=np.int32)
# print (c)

d = np.arange(5, 35, 5)
print (d)
print (d.reshape(2, 3))
#
# e = np.random.random((2, 3))
# print e


# from numpy import pi
# f = np.linspace(0, 2*pi, 100)  # 从0到 2pi 平均取100个值
# print (f)
#
# print np.sin(f)

# g = np.array([5, 10, 15, 20])
h = np.arange(4)
# print (g)
print h
# i = g - h
# print i
# j = i - 1
# print j
#
# k = j * 2
# print k
# l = g < 18
# print l
# m = h**2
# print m


A = np.array([
    [1, 1],
    [0, 1]
])
B = np.array([
    [2, 0],
    [3, 4]
])
print A
print '-------------'
print B
print '-------------'
print (A*B)
print '-------------'
print (A.dot(B)) # 矩阵点乘
print '-------------'
print (np.dot(A, B))
