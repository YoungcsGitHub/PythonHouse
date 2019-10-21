# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         MultiWindows
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''

容纳多文档窗口

QMdiArea

QMdiSubWindow

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MultiWindowDemo(QMainWindow):
    count = 0

    def __init__(self, parent = None):
        super(MultiWindowDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MultiWindow Demo')
        self.resize(430, 230)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowAction)

    def windowAction(self, q):
        if q.text() == 'New':
            MultiWindowDemo.count = MultiWindowDemo.count +1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口' + str(MultiWindowDemo.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == 'cascade':
            self.mdi.cascadeSubWindows()
        elif q.text() == 'Tiled':
            self.mdi.tileSubWindows()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MultiWindowDemo()
    mainWin.show()
    sys.exit(app.exec_())