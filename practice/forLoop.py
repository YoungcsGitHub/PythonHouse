# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         forLoop
# Description:  
# Author:       Dell
# Date:         2019/10/15
#-------------------------------------------------------------------------------

# ##############################################

# for every_letter in 'Hello world':
#     print(every_letter, end=' ')

# ##############################################

# for num in range(1,11):
#     print(str(num) + '+ 1 =', num+1)

# ##############################################

# songlist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
# for song in songlist:
#     if song == 'Holy Diver':
#         print(song,' - Dio')
#     elif song == 'Thunderstruck':
#         print(song, ' - AC/DC')
#     elif song == 'Rebel Rebel':
#         print(song, ' - David Bowie')

# ##############################################

for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i*j))