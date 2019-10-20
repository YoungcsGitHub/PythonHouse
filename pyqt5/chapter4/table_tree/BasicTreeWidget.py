# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         BasicTreeWidget
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''
树控件（QTreeWidget）的基本用法


'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QColor
import sys


class BasicTreeWidgetDemo(QMainWindow):
    def __init__(self, parent = None):
        super(BasicTreeWidgetDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BasicTreeWidget Demo')
        self.resize(400,300)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 指定标签
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setIcon(0,QIcon('./images/alien1.bmp'))
        self.tree.setColumnWidth(0,120)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('./images/ship.bmp'))
        child1.setCheckState(0, Qt.Checked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon('./images/ship.bmp'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '新的值')
        child3.setIcon(0, QIcon('./images/ship.bmp'))

        self.tree.expandAll()

        self.setCentralWidget(self.tree)

        # self.tablewidget = QTableWidget()
        # self.tablewidget.setRowCount(4)
        # self.tablewidget.setColumnCount(3)
        # layout.addWidget(self.tablewidget)
        #
        # self.tablewidget.setHorizontalHeaderLabels(['name', 'sex', 'weight(kg)'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = BasicTreeWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())