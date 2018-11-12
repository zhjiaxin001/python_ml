# -*- coding:utf-8 -*-
# num = 59
# # guess_flag = False
# # while guess_flag == False:
# #     guess = int(input('Enter a num'))
# #     if guess == num:
# #         guess_flag = True
# #     elif guess < num:
# #         print ('lower')
# #     else:
# #         print ('higher')
# # print 'bingo'
# # print ('done')


num = 59
# guess_flag = False
num_chances = 3
print 'you have three chances'
for i in range(1,num_chances+1):
    guess = int(input('Enter a num'))
    if guess == num:
        # guess_flag = True
        print 'bingo'
        break
    elif guess < num:
        print ('lower.you have '+ str(num_chances-i)+ ' times chance')
    else:
        print ('higher')
print ('done')
