# -*- coding:utf-8 -*-
# 1.语法错误，2.异常

# while True:
#     try:
#         x = int(raw_input('please enter a number'))
#         break
#     except ValueError:
#         print 'not valid input ,tray again...'


try:
    f = open('sentence.txt')
    s = f.readline()
    int(s.rstrip(s))
except OSError as err:
    print ('os error :{}'.format(err))
except ValueError:
    print ('Conld not convert data to integer.. ')
except :
    print '12312321'