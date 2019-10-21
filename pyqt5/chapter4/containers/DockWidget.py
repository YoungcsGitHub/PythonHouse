# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         DockWidget
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''

停靠控件 QDockWidget

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys


class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DockWidget Demo')
        self.resize(430, 230)

        layout = QHBoxLayout()
        self.items = QDockWidget('DockWidget', self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.listWidget.addItems(['item4', 'item5'])

        self.items.setWidget(self.listWidget)

        self.setCentralWidget(QLineEdit())

        self.items.setFloating(True)
        
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DockWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())