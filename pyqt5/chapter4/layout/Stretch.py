# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Stretch
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

设置伸缩量（addStretch）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class StretchDemo(QWidget):
    def __init__(self):
        super(StretchDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stretch Demo')
        self.resize(430, 230)

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn4 = QPushButton(self)
        btn5 = QPushButton(self)

        btn6 = QPushButton(self)
        btn7 = QPushButton(self)
        btn8 = QPushButton(self)
        btn9 = QPushButton(self)
        btn10 = QPushButton(self)

        btn1.setText("按钮1")
        btn2.setText("按钮2")
        btn3.setText("按钮2")
        btn4.setText("按钮4")
        btn5.setText("按钮5")

        btn6.setText("按钮6")
        btn7.setText("按钮7")
        btn8.setText("按钮8")
        btn9.setText("按钮9")
        btn10.setText("按钮10")

        layout = QHBoxLayout()

        layout.addStretch(0)
        layout.addWidget(btn1)

        layout.addStretch(1)
        layout.addWidget(btn2)

        layout.addStretch(2)
        layout.addWidget(btn3)

        layout.addStretch(3)
        layout.addWidget(btn4)

        layout.addStretch(3)
        layout.addWidget(btn5)

        layout1 = QHBoxLayout()

        layout1.addStretch(0)
        layout1.addWidget(btn6)
        layout1.addWidget(btn7)
        layout1.addWidget(btn8)
        layout1.addWidget(btn9)

        layout1.addStretch(3)
        layout1.addWidget(btn10)

        flayout = QFormLayout()

        flayout.addItem(layout)
        flayout.addItem(layout1)


        self.setLayout(flayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = StretchDemo()
    mainWin.show()
    sys.exit(app.exec_())