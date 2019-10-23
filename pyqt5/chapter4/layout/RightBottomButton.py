# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         RightBottomButton
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

让按钮永远在窗口右下角

一般不使用绝对布局，适应性不强

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class RightBottomButtonDemo(QWidget):
    def __init__(self):
        super(RightBottomButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('RightBottomButton Demo')
        self.resize(400, 300)

        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')

        vbox.addStretch(0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(1)

        vbox.addLayout(hbox)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = RightBottomButtonDemo()
    mainWin.show()
    sys.exit(app.exec_())