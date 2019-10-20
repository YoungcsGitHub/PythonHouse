# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         CellTextAlignment
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

设置单元格文本的对齐方式

setTextAlignment

Qt.AlignRight    Qt.AlignBottom

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class CellTextAlignmentDemo(QWidget):
    def __init__(self):
        super(CellTextAlignmentDemo, self).__init__()
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

        newItem = QTableWidgetItem('LeiShen')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.tablewidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('male')
        newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.tablewidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('70')
        newItem.setTextAlignment(Qt.AlignBottom)
        self.tablewidget.setItem(0, 2, newItem)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellTextAlignmentDemo()
    mainWin.show()
    sys.exit(app.exec_())