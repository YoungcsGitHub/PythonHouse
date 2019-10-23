# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         AutoSignalSlot
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''

信号与槽自动连接

self.okButton.setObjectName

'''

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class AutoSinalSlotDemo(QWidget):
    def __init__(self):
        super(AutoSinalSlotDemo, self).__init__()
    #     self.initUI()
    #
    # def initUI(self):
        self.setWindowTitle('AutoSinalSlot Demo')
        self.resize(430, 230)
        self.okButton = QPushButton('ok', self)
        self.okButton.setObjectName('okButton')
        self.okButton1 = QPushButton('cancel', self)
        self.okButton1.setObjectName('cancelButton')

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.okButton1)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

        # self.okButton.clicked.connect(self.on_clicked)
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print('点击了ok按钮')

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print('点击了cancel按钮')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = AutoSinalSlotDemo()
    mainWin.show()
    sys.exit(app.exec_())