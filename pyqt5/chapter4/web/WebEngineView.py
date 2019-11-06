# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         WebEngineView
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''

用web浏览器控件（QWebEngineView）显示网页

PyQt5 和 Web的交互技术

同时使用python和web开发程序， 混合开发

'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys


class WebEngineViewDemo(QMainWindow):
    def __init__(self,parent = None):
        super(WebEngineViewDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('打开外部网页 Demo')
        # self.resize(430, 230)
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://geekori.com'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WebEngineViewDemo()
    mainWin.show()
    sys.exit(app.exec_())