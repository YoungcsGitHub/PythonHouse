# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         TableWidget
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

扩展的表格控件（QTableWidget）

QTableView的子类

每一个cell（单元格）是一个QTableWidgetItem对象

'''

from PyQt5.QtWidgets import *
import sys

class TableWidgetDemo(QWidget):
    def __init__(self, parent=None):
        super(TableWidgetDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableWidget Demo')
        self.resize(430, 230)

        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['name', 'age', 'native'])
        nameItem = QTableWidgetItem('XIAOMING')
        tablewidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem('24')
        tablewidget.setItem(0, 1, ageItem)

        nativeItem = QTableWidgetItem('beijing')
        tablewidget.setItem(0, 2, nativeItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 调整列和行
        tablewidget.resizeColumnToContents(1)
        tablewidget.resizeRowsToContents()

        # 隐藏表头
        # tablewidget.verticalHeader().setVisible(False)
        # tablewidget.horizontalHeader().setVisible(False)

        # 重设表头
        tablewidget.setVerticalHeaderLabels(['a', 'b', 'c', 'd'])

        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TableWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())