# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ColumnSort
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

按列排序

1. 按哪一列排序
2. 排序类型

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class ColumnSortDemo(QWidget):
    def __init__(self):
        super(ColumnSortDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('ColumnSort Demo')
        self.resize(430, 230)

        layout = QHBoxLayout()

        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(3)
        layout.addWidget(self.tablewidget)

        self.tablewidget.setHorizontalHeaderLabels(['name', 'sex', 'weight(kg)'])

        newItem = QTableWidgetItem('张三')
        self.tablewidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tablewidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('165')
        self.tablewidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem('李四')
        self.tablewidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('女')
        self.tablewidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('160')
        self.tablewidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王五')
        self.tablewidget.setItem(2, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tablewidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem('170')
        self.tablewidget.setItem(2, 2, newItem)

        button = QPushButton('排序')
        button.clicked.connect(self.order)
        layout.addWidget(button)

        self.orderType = Qt.DescendingOrder

        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tablewidget.sortItems(2, self.orderType)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ColumnSortDemo()
    mainWin.show()
    sys.exit(app.exec_())