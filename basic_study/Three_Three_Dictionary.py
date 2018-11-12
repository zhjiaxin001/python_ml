# -*- coding: utf-8 -*-
# 键(key)，对应值(value)

# 创建词典
phone_book = {'Tom': 123, 'Jerry': 456, 'kim': 789}
mix_dict = {'Tom': 'boy', 11: 234.5}
# 访问一个值
print ("Tom has phone number " + str(phone_book['Tom']))
# 修改字典里面的值
phone_book['Tom'] = 999
print ("Tom has phone number " + str(phone_book['Tom']))
phone_book['Heath'] = 888
print ("The added book is " + str(phone_book))
# 删除字典元素及字典本身
del phone_book['Tom']
print ("The  book after del is " + str(phone_book))
# 清空词典
phone_book.clear()
print ('clear :' + str(phone_book))
del phone_book
# print (str(phone_book))
# 不允许key重复，若重复，以最后的覆盖前面的
rep_test = {'Name': 'aa', 'age': 15, 'Name': 'bb'}
print ('rep_test is ' + str(rep_test))
# 键不可变，所以可以用数字，字符串，元组来充当键，禁止使用列表当做键
tuple_dict = {('Name', "zh"): 'ceshi '}
print (str(tuple_dict))