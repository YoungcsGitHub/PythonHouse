# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         PrintSupport
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

使用打印机


'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui,QtWidgets,QtPrintSupport


class PrintSupportDemo(QMainWindow):
    def __init__(self):
        super(PrintSupportDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('')
        # self.resize(300, 200)
        self.setGeometry(500,200,300,300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        self.button.setGeometry(20,20,260,30)
        self.editor = QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200,)

        self.button.clicked.connect(self.print)

    def print(self):
        printer = QtPrintSupport.QPrinter()

        painter = QtGui.QPainter()
        # 将绘制的目标重定向到打印机
        painter.begin(printer)
        screen = self.editor.grab()
        painter.drawPixmap(10,10,screen)
        painter.end()
        print("print")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PrintSupportDemo()
    mainWin.show()
    sys.exit(app.exec_())