# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         TreeView
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''
QTreeView 控件与系统定制模式  复杂树时使用QTreeView

QTreeWidget

用Model  来装载不同控件

QDirModel

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)

    tree.resize(640, 480)
    tree.setWindowTitle('QTreeView Demo')

    tree.show()

    sys.exit(app.exec_())