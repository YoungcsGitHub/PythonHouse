# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         DrawTest
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

绘图API：绘制文本

1. 文本
2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
3. 图像

QPainter

painter = QPainter()
painter.begin()
painter.drawText(...)
painter.end()

必须在paintEvent事件方法中绘制各种元素
'''
import sys
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(400, 200)
        self.text = 'Python从菜鸟到高手'

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)
        print('aaa')
        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont('KaiTi',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawTextDemo()
    mainWin.show()
    sys.exit(app.exec_())