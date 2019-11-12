# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         WindowMaxMin
# Description:  
# Author:       Dell
# Date:         2019/10/24
#-------------------------------------------------------------------------------

'''

窗口最大化最小化

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class WindowMaxMin(QWidget):
    def __init__(self):
        super(WindowMaxMin, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('窗口最大化最小化 Demo')
        self.resize(430, 230)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint |
        #                     Qt.WindowCloseButtonHint |
        #                     Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

        layout = QVBoxLayout()
        maxButton1 = QPushButton()
        maxButton1.setText('窗口最大化1')
        maxButton1.clicked.connect(self.maxmized1)
        layout.addWidget(maxButton1)

        maxButton2 = QPushButton()
        maxButton2.setText('窗口最大化2')
        maxButton2.clicked.connect(self.showMaximized)
        layout.addWidget(maxButton2)

        minButton = QPushButton()
        minButton.setText('窗口最小化')
        minButton.clicked.connect(self.showMinimized)
        layout.addWidget(minButton)

        self.setLayout(layout)

    def maxmized1(self):
        desktop = QApplication.desktop()
        # 获取桌面可用尺寸
        rect = desktop.availableGeometry()
        self.setGeometry(rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WindowMaxMin()
    mainWin.show()
    sys.exit(app.exec_())