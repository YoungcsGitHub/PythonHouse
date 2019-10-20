# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         TableView
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

显示二维表数据（QTableView控件）

数据源

Model

需要创建QTableView实例和一个数据源（Model）， 然后将两者关联

MVC： Model   Viewer   Controller

MVC 的目的是将后端的数据和前端页面的耦合度降低

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TableViewDemo(QWidget):
    def __init__(self, arg = None):
        super(TableViewDemo, self).__init__(arg)
        self.setWindowTitle('QTableView表格视图控件演示')
        self.resize(500,300)

        self.model = QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['id', 'name', 'age'])

        self.tableview = QTableView()
        # 关联QTableView控件和Model
        self.tableview.setModel(self.model)

        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item31 = QStandardItem('30')
        item32 = QStandardItem('死亡女神')
        item33 = QStandardItem('3000')
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TableViewDemo()
    mainWin.show()
    sys.exit(app.exec_())