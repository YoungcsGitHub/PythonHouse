# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         InvestDemo
# Description:  
# Author:       Dell
# Date:         2019/10/16
#-------------------------------------------------------------------------------

def invest(amount, rate, time):
    print("principal amount:{}".format(amount))
    for t in range(1, time+1):
        amount = amount * (1 + rate)
        print("year {}: ${}".format(t, amount))

invest(100, .05, 8)
invest(2000, .025, 5)