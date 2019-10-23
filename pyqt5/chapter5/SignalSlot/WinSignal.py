# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         WinSignal
# Description:  
# Author:       Dell
# Date:         2019/10/23
#-------------------------------------------------------------------------------

'''

为窗口类添加信号

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class WinSignal(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinSignal, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('为窗口类添加信号')
        self.resize(430, 230)

        btn = QPushButton('关闭窗口', self)

        btn.clicked.connect(self.btn_clicked)

        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WinSignal()
    mainWin.show()
    sys.exit(app.exec_())