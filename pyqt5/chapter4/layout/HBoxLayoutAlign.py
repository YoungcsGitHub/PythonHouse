# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         HBoxLayout
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

设置控件的对齐方式

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys,math
import os


class HBoxLayoutAlign(QWidget):
    def __init__(self):
        super(HBoxLayoutAlign, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('HBoxLayoutAlign Demo')
        self.resize(430, 230)

        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'), 2, Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮2'), 4, Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮3'), 1, Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮4'), 1, Qt.AlignLeft | Qt.AlignBottom)
        hlayout.addWidget(QPushButton('按钮5'), 1, Qt.AlignLeft | Qt.AlignBottom)
        hlayout.setSpacing(40)
        self.setLayout(hlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = HBoxLayoutAlign()
    mainWin.show()
    sys.exit(app.exec_())