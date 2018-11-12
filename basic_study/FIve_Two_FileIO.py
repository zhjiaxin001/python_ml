# -*- coding:utf-8 -*-
# 读入写出文件
# str1 = '''I love study python
# becuase python is fun
# and alse easy to use
# '''
#
# f = open('sentence.txt', 'w')
# f.write(str1)
# f.close()

# 读入一个文件
f = open('sentence.txt')
while True:
    line =f.readline()
    if len(line) == 0:
        break
    print (line)
f.close()
