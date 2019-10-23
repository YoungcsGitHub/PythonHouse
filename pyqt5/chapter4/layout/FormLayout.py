# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         FormLayout
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

表单布局  （QFormLayout）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class FormLayoutDemo(QWidget):
    def __init__(self):
        super(FormLayoutDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FormLayout Demo')
        self.resize(430, 230)

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        flayout = QFormLayout()
        flayout.setSpacing(10)

        flayout.addRow(titleLabel,titleEdit)
        flayout.addRow(authorLabel,authorEdit)
        flayout.addRow(contentLabel,contentEdit)

        self.setLayout(flayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = FormLayoutDemo()
    mainWin.show()
    sys.exit(app.exec_())