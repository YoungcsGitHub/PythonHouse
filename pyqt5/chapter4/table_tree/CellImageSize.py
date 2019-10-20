# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         CellFontAndColor
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''

设置单元格中图片尺寸

setIconSize(QSize(with,height))

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class CellImageSizeDemo(QWidget):
    def __init__(self):
        super(CellImageSizeDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('CellImageSize Demo')
        self.resize(1000, 900)

        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setIconSize(QSize(300, 200))
        tablewidget.setRowCount(5)
        tablewidget.setColumnCount(3)
        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['image1', 'image2', 'image3'])

        # 让列的宽度和图片的宽度相同
        for i in range(3):
            tablewidget.setColumnWidth(i, 300)

        # 让列的高度和图片的高度相同
        for j in range(15):
            tablewidget.setRowHeight(j, 200)

        for k in range(15):
            i = k / 3           # 行
            j = k % 3           # 列
            item = QTableWidgetItem()
            item.setIcon(QIcon('./images/alien%d.bmp' % k))
            tablewidget.setItem(i,j,item)



        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CellImageSizeDemo()
    mainWin.show()
    sys.exit(app.exec_())