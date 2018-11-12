# -*- coding:utf-8 -*-
import numpy as np
# data = np.sin(np.arange(20).reshape(5, 4))
# print data
# ind = data.argmax(axis = 0)
# print ind
# print range(data.shape[1])
# datamax = data[ind, range(data.shape[1])]
# print datamax

# inde = data.argmax(axis = 1)
# datamax = data[range(data.shape[0]), inde]
# print datamax
# a = np.arange(0, 40, 10)
#
# print a
# b = np.tile(a, (2, 2))
# print b

# a = np.array([[1, 9, 3], [10, 18, 16], [7, 8, 9]])
# b = np.sort(a, axis=1)
# print b
#
# a.sort(axis=1)
#
# print a

a = np.array([4, 2, 1, 2])
j = np.argsort(a) # 从小到大索引排序
print j

