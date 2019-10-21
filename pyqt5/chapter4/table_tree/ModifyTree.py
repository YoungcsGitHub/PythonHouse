# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ModifyTree
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''



'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class ModifyTreeDemo(QWidget):
    def __init__(self, parent = None):
        super(ModifyTreeDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ModifyTree Demo')
        self.resize(430, 230)

        operatorlayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorlayout.addWidget(addBtn)
        operatorlayout.addWidget(updateBtn)
        operatorlayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 指定标签
        self.tree.setHeaderLabels(['Key', 'Value'])
        # 根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        self.tree.setColumnWidth(0, 180)

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

        mainlayout = QVBoxLayout()
        mainlayout.addLayout(operatorlayout)
        mainlayout.addWidget(self.tree)

        self.setLayout(mainlayout)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        # print(index.row())
        print('key = %s, value = %s' % (item.text(0), item.text(1)))

    def addNode(self):
        # print('添加节点')
        item = self.tree.currentItem()
        # print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, '新节点')
        node.setText(1, '新的值')

    def updateNode(self):
        # print('修改节点')
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '已修改节点')

    def deleteNode(self):
        print('删除节点')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ModifyTreeDemo()
    mainWin.show()
    sys.exit(app.exec_())