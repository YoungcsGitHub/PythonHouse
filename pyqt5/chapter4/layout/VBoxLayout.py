# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         HBoxLayout
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

垂直盒布局（QVBoxLayout）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys,math
import os


class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('VBoxLayout Demo')
        self.resize(430, 230)

        label = QLabel()
        label.setStyleSheet("background-color:red")
        label.resize(20, 50)
        label.setText('1555555555555555555555555555')
        label.setWordWrap(True)

        vlayout = QVBoxLayout()
        vlayout.addWidget(QPushButton('按钮1'))
        vlayout.addWidget(QPushButton('按钮2'))
        vlayout.addWidget(QPushButton('按钮3'))
        vlayout.addWidget(QPushButton('按钮4'))
        vlayout.addWidget(QPushButton('按钮5'))
        vlayout.addWidget(QPushButton('按钮6'))

        # vlayout.addWidget(label)
        vlayout.setSpacing(40)
        self.setLayout(vlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = VBoxLayout()
    mainWin.show()
    sys.exit(app.exec_())