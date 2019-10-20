# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         BasicTreeWidget
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

为树节点添加响应时间


'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QColor
import sys


class TreeEventDemo(QMainWindow):
    def __init__(self, parent = None):
        super(TreeEventDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TreeEvent Demo')
        self.resize(400,300)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 指定标签
        self.tree.setHeaderLabels(['Key', 'Value'])
        # 根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        self.tree.setColumnWidth(0,180)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)

        self.tree.expandAll()

        self.setCentralWidget(self.tree)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key = %s, value = %s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TreeEventDemo()
    mainWin.show()
    sys.exit(app.exec_())