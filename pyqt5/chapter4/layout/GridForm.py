# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         GridForm
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

栅格布局： 表单设计

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class GridFormDemo(QWidget):
    def __init__(self):
        super(GridFormDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GridForm Demo')
        self.resize(430, 230)

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(titleLabel, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(authorLabel, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(contentLabel, 3, 0)
        grid.addWidget(contentEdit, 3, 1, 5, 1)

        self.setLayout(grid)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = GridFormDemo()
    mainWin.show()
    sys.exit(app.exec_())