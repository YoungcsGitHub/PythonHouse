# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         QSSSelector
# Description:  
# Author:       Dell
# Date:         2019/10/24
#-------------------------------------------------------------------------------

'''

QSS 选择器

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class QSSSelector(QWidget):
    def __init__(self):
        super(QSSSelector, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSSSelector Demo')
        # self.resize(430, 230)

        btn1 = QPushButton(self)
        btn1.setText('按钮1')

        btn2 = QPushButton(self)
        btn2.setProperty("name", "btn2")
        btn2.setText('按钮2')

        btn3 = QPushButton(self)
        btn3.setProperty("name", "btn3")
        btn3.setText('按钮3')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QSSSelector()
    qssStyle = '''
            QPushButton[name = "btn2"] {
                background-color:red;
                color:yellow;
                height:80;
                font-size:60px;
            }
            QPushButton[name = "btn3"] {
                background-color:orange;
                color:green;
                height:60;
                font-size:30px;
            }
        '''
    mainWin.setStyleSheet(qssStyle)
    mainWin.show()
    sys.exit(app.exec_())