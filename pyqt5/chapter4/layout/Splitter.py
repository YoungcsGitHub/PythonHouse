# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Splitter
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

拖动控件之间的边界（QSplitter）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class SplitterDemo(QWidget):
    def __init__(self):
        super(SplitterDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Splitter Demo')
        # self.resize(430, 230)
        self.setGeometry(300, 300, 300, 200)

        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox = QHBoxLayout()
        hbox.addWidget(splitter2)

        self.setLayout(hbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = SplitterDemo()
    mainWin.show()
    sys.exit(app.exec_())