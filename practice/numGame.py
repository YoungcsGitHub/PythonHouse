# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         numGame
# Description:  
# Author:       Dell
# Date:         2019/10/16
#-------------------------------------------------------------------------------

# a_list = [1, 2, 3]
# print(sum(a_list))
#
# import  random
#
# point1 = random.randrange(1, 7)
# point2 = random.randrange(1, 7)
# point3 = random.randrange(1, 7)
#
# print(point1, point2, point3)

import random

def roll_dice(numbers = 3, points = None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers -= 1
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    print('<<<<< GAME STRATS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small:')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are', points, 'You win!')
        else:
            print('The points are', points, 'You lose!')
    else:
        print('Invalid Words')
        start_game()
start_game()