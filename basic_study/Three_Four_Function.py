# -*- coding: utf-8 -*-
def say_hi():
    print ('hi!')


say_hi()
say_hi()


def repeat_str(string, times):
    repeated_str = string * times
    return repeated_str


repeated_strs = repeat_str('Hello ', 4)
print (repeated_strs)

# 全局变量与局部变量
