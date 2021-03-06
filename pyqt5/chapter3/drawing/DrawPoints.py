# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         DrawPoints
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

用像素点绘制正弦曲线

-2pi   2pi

drawPoint(x,y)

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class DrawPointsDemo(QWidget):
    def __init__(self):
        super(DrawPointsDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在窗口上用像素点绘制两个周期的正弦曲线')
        self.resize(300, 300)

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            x = 100 * (-1 + 2.0 * i/1000) + size.width()/2.0
            y = -50 * math.sin((x - size.width()/2.0) * math.pi/50) + size.height()/2.0
            painter.drawPoint(x,y)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DrawPointsDemo()
    mainWin.show()
    sys.exit(app.exec_())