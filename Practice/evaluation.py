# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         evaluation
# Description:  
# Author:       Dell
# Date:         2019/10/19
#-------------------------------------------------------------------------------

# class TestA:
#     attr = 1
#     def __init__(self):
#         self.attr = 42
#
# obj_a = TestA()
# # obj_b = TestA()
# # obj_a.attr = 42
# print(obj_a.attr)
# # print(obj_b.attr)
# print(TestA.__dict__)
# print(obj_a.__dict__)

# obj1 = 1
# obj2 = 'String!'
# obj3 = []
# obj4 = {}
# print(type(obj1), type(obj2), type(obj3), type(obj4))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup
# print(type(soup))

'''一百道练习题'''

'''第一题'''

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and i != k and j != k:
#                 print (i,j,k)

'''第二题'''

# bonus1 = 100000 * 0.1
# bonus2 =
#
# profit = int(input('请输入利润：'))
#
# if profit <= 100000:
#     bonus1 = profit * 0.1
# elif profit <= 200000:
#     bonus2 = bonus1 + (profit - 100000) * 0.075
# elif profit <= 400000:
#     bonus3 = bonus2 + (profit - 200000) * 0.05
# elif profit <= 600000:
#     bonus4 = bonus3 + (profit - 400000) * 0.03
# elif 600000 < profit < 1000000:
#     bonus5 = bonus4 + (profit - 600000) * 0.015
# else:
#     bonus6 = (profit - 1000000) * 0.01
#
# print('bonus =  ', bonus)

'''第3题'''

# import math
# for i in range(10000):
#     x = int(math.sqrt(i + 100))
#     y = int(math.sqrt(i + 268))
#     if (x * x == i + 100) and (y * y == i + 268):
#         print(i)

'''第4题'''

year = int(input('year: \n'))
month = int(input('month: \n'))
day = int(input('day: \n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)
if 0 <= month <=12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 ==0) and (year % 100 != 0)):
    leap = 1
if leap == 1 and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)
