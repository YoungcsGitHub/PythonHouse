# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         WindowPattern
# Description:  
# Author:       Dell
# Date:         2019/10/24
#-------------------------------------------------------------------------------

'''

设置窗口的样式

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class WindowPatternDemo(QMainWindow):
    def __init__(self):
        super(WindowPatternDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置窗口的样式 Demo')
        self.resize(500, 260)

        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/png/Basilisk.jpg);}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WindowPatternDemo()
    mainWin.show()
    sys.exit(app.exec_())