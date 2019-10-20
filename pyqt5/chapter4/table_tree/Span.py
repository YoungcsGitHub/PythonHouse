# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Span
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

合并单元格

setSpan(row, col, 要合并的行数，要合并的列数）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class SpanDemo(QWidget):
    def __init__(self):
        super(SpanDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('SpanDemo')
        self.resize(430, 230)

        layout = QHBoxLayout()

        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(3)
        layout.addWidget(self.tablewidget)

        self.tablewidget.setHorizontalHeaderLabels(['name', 'sex', 'weight(kg)'])

        newItem = QTableWidgetItem('leishen')
        self.tablewidget.setItem(0, 0,newItem)
        self.tablewidget.setSpan(0, 0, 3, 1)

        newItem = QTableWidgetItem('male')
        self.tablewidget.setItem(0, 1, newItem)
        self.tablewidget.setSpan(0, 1, 2, 1)

        newItem = QTableWidgetItem('75')
        self.tablewidget.setItem(0, 2, newItem)
        self.tablewidget.setSpan(0, 2, 4, 1)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = SpanDemo()
    mainWin.show()
    sys.exit(app.exec_())