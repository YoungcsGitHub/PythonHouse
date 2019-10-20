# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Datalocation
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

在表格中快速定位到特定的行

1. 数据的定位  findItems
2. 如果找到了满足条件的单元格，会定位到单元格所在的行: setSliderPosition(row)

'''

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush
import sys


class DataLocation(QWidget):
    def __init__(self, parent=None):
        super(DataLocation, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('DataLocation Demo')
        self.resize(600, 800)

        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(40)
        tablewidget.setColumnCount(4)

        layout.addWidget(tablewidget)

        for i in range(40):
            for j in range(4):
                itemContent = '(%d, %d)' % (i, j)
                tablewidget.setItem(i,j,QTableWidgetItem(itemContent))

        self.setLayout(layout)

        # 搜索满足条件的Cell
        text = '(13, 1)'
        items = tablewidget.findItems(text, QtCore.Qt.MatchExactly)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor(0, 255, 0)))
            item.setForeground(QBrush(QColor(255, 0, 0)))

            row = item.row()

            # 定位到指定的行
            tablewidget.verticalScrollBar().setSliderPosition(row)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DataLocation()
    mainWin.show()
    sys.exit(app.exec_())