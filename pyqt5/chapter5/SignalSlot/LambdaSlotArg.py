# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         LambdaSlotArg
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''

使用Lambda表达式为槽函数传递参数

Lambda表达式： 匿名函数，也就是没有名字的函数

fun = lambda :print('hello world')
fun()

fun1 = lambda x,y :print(x,y)
fun1('a','b')

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super(LambdaSlotArg, self).__init__()
        self.setWindowTitle('使用lambda表达式为槽函数传递参数')
        self.resize(430, 230)

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        ok = 100
        button1.clicked.connect(lambda :self.onButtonClick(10,ok))
        button2.clicked.connect(lambda :self.onButtonClick(40,-20))
        button1.clicked.connect(lambda :QMessageBox.information(self,'结果', '单击了按钮1'))


        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self,m,n):
        print('m + n =',m + n)
        QMessageBox.information(self,'结果', str(m+n))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = LambdaSlotArg()
    mainWin.show()
    sys.exit(app.exec_())