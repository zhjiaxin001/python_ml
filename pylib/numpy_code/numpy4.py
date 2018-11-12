# -*- coding:utf-8 -*-
import numpy as np
# B = np.arange(3)
# print (B)
# print (np.exp(B))
# print np.sqrt(B)

# a = np.floor(10*np.random.random((3,4)))
# print a
#
# print a.shape
#
# # print a.ravel()   # 矩阵拉成向量
# a.shape = (6, 2)
# print a
# print a.T # 转置
#
# print a.reshape(4, -1)

# a = np.floor(10 * np.random.random((2, 2)))
# b = np.floor(10 * np.random.random((2, 2)))
# print a
# print b

# print (np.hstack((a, b)))
# print (np.vstack((a, b)))

# a = np.floor(10*np.random.random((2, 12)))
# b = np.floor(10*np.random.random((2, 12)))

# print a
# print np.hsplit(a, 3)
#
# print np.hsplit(a, (2, 4))

# b = a.T
# print b
# print np.vsplit(b, (3, 4))


# 复制操作
a = np.arange(12)
print a
b = a
print b is a
b.shape = (3, 4)
print id(a)
print id(b)

c = a.view()  # 浅复制
print (c is a)
c.shape = (2,6)
print a.shape
print c[0, 4]
c[0, 4] = 1234
print a

d = a.copy()  # 深复制
print d is a
d[0, 0] =9999
print d
print a

