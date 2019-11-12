# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Background
# Description:  
# Author:       Dell
# Date:         2019/10/25
#-------------------------------------------------------------------------------

'''

使用多种方式设置窗口背景色和背景图片

1. QSS
2. QPalette
3. 直接绘制

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class Background1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘制背景颜色和图片')

    # def paintEvent(self,event):
    #     painter = QPainter(self)
    #     painter.setBrush(Qt.yellow)
    #     painter.drawRect(self.rect())

    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap('.\images\Basilisk.jpg')
        painter.drawPixmap(self.rect(), pixmap)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Background1()
    mainWin.show()
    sys.exit(app.exec_())
