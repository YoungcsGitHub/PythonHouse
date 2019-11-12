# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         WindowStyle
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''

窗口、绘图与特效： 设置窗口风格

QApplication.setStyle(...)

'''

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

# print(QStyleFactory.keys())
class WindowStyle(QWidget):
    def __init__(self):
        super(WindowStyle, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置窗口风格 Demo')
        # self.resize(430, 230)
        hlayout = QHBoxLayout()
        self.styleLabel = QLabel('设置窗口风格：')
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())

        # 获取当前窗口的风格
        # print(QApplication.style().objectName())
        index = self.styleComboBox.findText(QApplication.style().objectName(), QtCore.Qt.MatchFixedString)

        self.styleComboBox.setCurrentIndex(index)

        self.styleComboBox.activated[str].connect(self.handleStyleChanged)

        hlayout.addWidget(self.styleLabel)
        hlayout.addWidget(self.styleComboBox)
        self.setLayout(hlayout)


    def handleStyleChanged(self, style):
        QApplication.setStyle(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WindowStyle()
    mainWin.show()
    sys.exit(app.exec_())