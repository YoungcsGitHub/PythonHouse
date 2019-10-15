# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         whileLoop
# Description:  
# Author:       Dell
# Date:         2019/10/15
#-------------------------------------------------------------------------------

# ###############################################

# while 1 < 3:
#     print('1 is smaller than 3')

# ##############################################

# count = 0
# while True:
#     print('Repeat this line!')
#     count += 1
#     if count == 5:
#         break

# ##############################################

password_list = ['*#*#', '12345']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login success!')

        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Your password has changed successfully!')
            account_login()

        else:
            print('Wrong password or invalid input!')
            tries -= 1
            print(tries, 'times left')

    else:
        print('Your account has been suspended')

account_login()