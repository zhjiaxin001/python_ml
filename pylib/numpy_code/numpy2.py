# -*- coding:utf-8 -*-

import pylib.numpy
# vector = numpy.array([5, 10, 15, 20])
# print (vector == 10)
#
# matrix = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2]])
# equal_to_ten = matrix == 10
# print equal_to_ten
# print matrix[equal_to_ten]
#
# sencond_column_equal_to_five = matrix[:, 1] == 5
# print sencond_column_equal_to_five
# line_equal_to_five = matrix[sencond_column_equal_to_five,:]
# print line_equal_to_five

# 与操作
# vector = numpy.array([5, 10, 15, 20])
# equal_to_ten_and_five = (vector == 5) & (vector == 10)
# print equal_to_ten_and_five
# equal_to_ten_or_five = (vector == 5) | (vector == 10)
# print equal_to_ten_or_five
# vector[equal_to_ten_or_five] = 90
# print vector



# matrix = numpy.array([
#                 [1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# second_column_25 = matrix[1, :] == 5
# print second_column_25
# matrix[second_column_25, 2] = 11
# print matrix


# vector = numpy.array(["5", "10", "15", "20"])
# print (vector.dtype)
# print (vector)
# vector = vector.astype(float)
# print (vector.dtype)
# print (vector)
# print (vector.min())
# print (vector.max())
# print help(numpy.array)

matrix = pylib.numpy.array([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print (matrix.sum(axis=1)) # 每行相加
print (matrix.sum(axis=0)) # 每列相加
