# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         CellFontAndColor
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

设置单元格宽度和高度

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class CellSizeDemo(QWidget):
    def __init__(self):
        super(CellSizeDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('CellFontAndColor Demo')
        self.resize(430, 230)

        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['name', 'sex', 'weight(kg)'])
        tablewidget.setRowHeight(0,100)
        tablewidget.setColumnWidth(0,200)

        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times', 40, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tablewidget.setItem(0, 0, newItem)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellSizeDemo()
    mainWin.show()
    sys.exit(app.exec_())