# -*- coding: utf-8 -*-
# 默认参数


def repeat_str(s,  times = 1):
    repeat_s = s * times
    return repeat_s


repeat_s = repeat_str('Hello ', 4)
print (repeat_s)

# 关键字参数可以直接指定调用


def func(a, b = 2, c = 6 ):
    print ('a is ' + a + ',b is' + b + ',c is'+c)

# 使用VarChars 传递参数


def funcmv(a, *b, **c):
    print ("a is " + a)
    print ("b is " + str(b))
    print ("c is " + str(c))


funcmv('hello', 1, 2, 3, 4, 5, 'str', key1 =  'word1', key2 = 'word2')
