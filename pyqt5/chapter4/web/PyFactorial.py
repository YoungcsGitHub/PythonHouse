# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         PyFactorial
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

JavaScript 调用 Python 函数计算阶乘

将Python的一个对象映射到JavaScript中

将槽函数映射到JavaScript中

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
from factorial import Factorial

channel = QWebChannel()
factorial = Factorial()
class PyFactorialDemo(QWidget):
    def __init__(self):
        super(PyFactorialDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyFactorial Demo')
        self.resize(600, 300)

        layout = QVBoxLayout()

        self.browser = QWebEngineView()
        url = os.getcwd() + '/f.html'
        self.browser.load(QUrl.fromLocalFile(url))

        channel.registerObject("obj", factorial)
        self.browser.page().setWebChannel(channel)

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PyFactorialDemo()
    mainWin.show()
    sys.exit(app.exec_())