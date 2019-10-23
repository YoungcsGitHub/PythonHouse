# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Calc
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

栅格布局： 实现计算器UI

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class CalcDemo(QWidget):
    def __init__(self):
        super(CalcDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calc Demo')
        # self.resize(430, 230)

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Back','','Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]
        print(positions)
        print(*(1, 2))

        for position, name in zip(positions,names):
            if name == '':
                continue
            # print(position)
            button = QPushButton(name)
            grid.addWidget(button, *position)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CalcDemo()
    mainWin.show()
    sys.exit(app.exec_())