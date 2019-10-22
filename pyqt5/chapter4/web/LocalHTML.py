# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         LocalHTML
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

结合HTML与PyQt5 装载本地页面

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os


class LocalHTML(QMainWindow):
    def __init__(self,parent = None):
        super(LocalHTML, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('装载本地页面 Demo')
        # self.resize(430, 230)
        self.setGeometry(5, 30, 1355, 730)
        url = os.getcwd() + '/test.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = LocalHTML()
    mainWin.show()
    sys.exit(app.exec_())