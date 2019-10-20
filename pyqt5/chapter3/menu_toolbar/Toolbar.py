# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Toolbar
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

创建和使用工具栏
工具栏默认按钮：只显示图标，将文本作为悬停提示

工具栏按钮的3种显示状态
1. 只显示图标
2. 只显示文本
3. 同时显示文本和图标

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ToolbarDemo(QMainWindow):
    def __init__(self):
        super(ToolbarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏实例')
        self.resize(300, 200)

        tb1 = self.addToolBar('File')

        new = QAction(QIcon('Knob Add.ico'),"new",self)
        tb1.addAction(new)

        open = QAction(QIcon('Knob Play Green.ico'),"open",self)
        tb1.addAction(open)

        save = QAction(QIcon('Knob Blue.ico'), "save", self)
        tb1.addAction(save)

        tb2 = self.addToolBar('File1')

        new = QAction(QIcon('Knob Add.ico'), "新建", self)
        tb2.addAction(new)

        open = QAction(QIcon('Knob Play Green.ico'), "打开", self)
        tb2.addAction(open)

        save = QAction(QIcon('Knob Blue.ico'), "保存", self)
        tb2.addAction(save)

        tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # 按钮显示风格
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)
        tb2.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self,a):
        print("按下的按钮是：",a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ToolbarDemo()
    mainWin.show()
    sys.exit(app.exec_())