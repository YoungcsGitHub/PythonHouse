# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         StatusBar
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

创建和使用状态栏

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('状态栏演示')
        self.resize(300, 200)

        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('show')
        file.triggered.connect(self.processTrigger)

        self.setCentralWidget(QTextEdit())

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self,q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + "菜单被点击了", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = StatusBarDemo()
    mainWin.show()
    sys.exit(app.exec_())