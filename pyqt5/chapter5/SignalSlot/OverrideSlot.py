# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         OverrideSlot
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''

Override(覆盖）槽函数， 改变系统定义槽的行为

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class OverrideSlot(QWidget):
    def __init__(self):
        super(OverrideSlot, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Override(覆盖）槽函数 Demo')
        self.resize(430, 230)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle('按下Alt键')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = OverrideSlot()
    mainWin.show()
    sys.exit(app.exec_())