# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         SignalSlotDemo
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''



'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo, self).__init__()
        self.initUI()

        self.btn = QPushButton('我的按钮')
        self.btn.clicked.connect(self.onClicked)
        layout = QHBoxLayout()
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def onClicked(self):
        self.btn.setText('信号已经发出')
        self.btn.setStyleSheet("QPushButton(max-width:200px;min-width:200px")

    def initUI(self):
        self.setWindowTitle('SignalSlot Demo')
        self.resize(430, 230)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = SignalSlotDemo()
    mainWin.show()
    sys.exit(app.exec_())