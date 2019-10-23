# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         PartialSlotArg
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''

使用Partial对象为槽函数传递参数

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os
from functools import partial


class PartialSlotArg(QMainWindow):
    def __init__(self):
        super(PartialSlotArg, self).__init__()
        self.setWindowTitle('使用Partial表达式为槽函数传递参数')
        self.resize(430, 230)

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        ok = 100
        cancel = -100
        button1.clicked.connect(partial(self.onButtonClick, 10,20))
        button2.clicked.connect(partial(self.onButtonClick, 40,-20))
        # button1.clicked.connect(partial(QMessageBox.information(self,'结果', '单击了按钮1'))
        button1.clicked.connect(partial(self.onButtonClick, ok,cancel))



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
    mainWin = PartialSlotArg()
    mainWin.show()
    sys.exit(app.exec_())