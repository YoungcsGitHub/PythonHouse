# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         PlaceControlinCell
# Description:  
# Author:       Dell
# Date:         2019/10/20
#-------------------------------------------------------------------------------

'''
在单元格中放置控件

setItem：        将文本放到单元格中
setCellWidget   将控件放到单元格中
setStyleSheet： 设置控件的样式（QSS）
'''

from PyQt5.QtWidgets import *
import sys


class PlaceControlInCell(QWidget):
    def __init__(self, parent=None):
        super(PlaceControlInCell, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('PlaceControlInCell Demo')
        self.resize(430, 300)

        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['name', 'sex', 'weight(kg)'])
        textItem = QTableWidgetItem('xiaoming')
        tablewidget.setItem(0, 0, textItem)

        combox = QComboBox()
        combox.addItem('male')
        combox.addItem('female')

        # QSS
        combox.setStyleSheet('QComboBox{margin:3px};')
        tablewidget.setCellWidget(0, 1, combox)

        modifyButton = QPushButton('modify')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tablewidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PlaceControlInCell()
    mainWin.show()
    sys.exit(app.exec_())