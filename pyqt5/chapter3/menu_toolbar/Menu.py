# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Menu
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

创建和使用菜单

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('菜单栏演示')
        self.resize(300, 200)
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu("文件")
        file.addAction('新建')

        save = QAction('保存',self)
        save.setShortcut("Ctrl + S")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction('退出',self)
        file.addAction(quit)

        save.triggered.connect(self.process)

    def process(self,a):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MenuDemo()
    mainWin.show()
    sys.exit(app.exec_())