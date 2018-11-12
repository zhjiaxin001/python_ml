# -*- coding: utf-8 -*-
a_tuple = (2,)
# Tuple中的List
mix_tuple = (1,2,['a','b'])
print ("mix_tuple is " + str(mix_tuple))
mix_tuple[2][0] = 'cddddd'
mix_tuple[2][1] = 'daaaaaa'
print ("mix_tuple after " + str(mix_tuple))

num_list = [1,2,3,4,5,6,7,8]
del num_list[1]
print (num_list[1])

# tuple提取
