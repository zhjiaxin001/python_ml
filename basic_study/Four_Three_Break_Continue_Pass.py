# -*- coding:utf-8 -*-
# num = 59
# # guess_flag = False
# num_chances = 3
# print 'you have three chances'
# while True:
#     guess = int(input('Enter a num'))
#     if guess == num:
#         # guess_flag = True
#         print 'bingo'
#         break
#     elif guess < num:
#         print ('lower.you have times chance')
#         continue
#     else:
#         print ('higher')
#         continue
# print ('done')

a_list = [0, 1, 2]
print 'useing continue'
for i in a_list:
    if not i:
        continue
    print i

print 'useing pass'
for i in a_list:
    if not i:
        pass
    print i
