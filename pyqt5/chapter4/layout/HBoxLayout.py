# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         HBoxLayout
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

水平盒布局（QHBoxLayout）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys,math
import os


class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('HBoxLayout Demo')
        self.resize(430, 230)

        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))
        hlayout.addWidget(QPushButton('按钮6'))
        hlayout.setSpacing(40)
        self.setLayout(hlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = HBoxLayout()
    mainWin.show()
    sys.exit(app.exec_())