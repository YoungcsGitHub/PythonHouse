# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         BasicQSS
# Description:  
# Author:       Dell
# Date:         2019/10/24
#-------------------------------------------------------------------------------

'''

QSS基础

QSS（Qt Style Sheets）
Qt样式表

用于设置控件的样式

CSS HTML

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class BasicQSS(QWidget):
    def __init__(self):
        super(BasicQSS, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BasicQSS Demo')
        self.resize(430, 230)

        btn1 = QPushButton()
        btn1.setText('按钮1')
        btn2 = QPushButton()
        btn2.setText('按钮2')
        btn3 = QPushButton()
        btn3.setText('按钮3')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = BasicQSS()
    qssStyle = '''
        QPushButton {
            background-color:red
        }
    '''
    mainWin.setStyleSheet(qssStyle)
    mainWin.show()
    sys.exit(app.exec_())