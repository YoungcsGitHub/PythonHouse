# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         DrawMultiLine
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

绘制不同类型的直线

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawMultiLineDemo(QWidget):
    def __init__(self):
        super(DrawMultiLineDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置Pen的样式')
        self.resize(300, 300)

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)

        pen = QPen(Qt.red,3,Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawMultiLineDemo()
    mainWin.show()
    sys.exit(app.exec_())