# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         CellFontAndColor
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

设置单元格文本图片混排

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class CellImageTextDemo(QWidget):
    def __init__(self):
        super(CellImageTextDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('CellFontAndColor Demo')
        self.resize(430, 230)

        layout = QHBoxLayout()

        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(4)
        layout.addWidget(self.tablewidget)

        self.tablewidget.setHorizontalHeaderLabels(['name', 'sex', 'weight(kg)', 'image'])


        newItem = QTableWidgetItem('雷神')
        self.tablewidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tablewidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        self.tablewidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon('./images/alien1.bmp'),'背包')
        self.tablewidget.setItem(0, 3, newItem)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellImageTextDemo()
    mainWin.show()
    sys.exit(app.exec_())