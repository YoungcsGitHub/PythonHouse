# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         AbnormityWindow
# Description:  
# Author:       Dell
# Date:         2019/10/25
#-------------------------------------------------------------------------------

'''

实现不规则窗口（异形窗口）

通过mask实现异形窗口

需要一张透明的png图， 透明部分被抠出，形成一个非矩形的区域

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class AbnormityWindow(QWidget):
    def __init__(self):
        super(AbnormityWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AbnormityWindow Demo')
        self.pix = QBitmap('.\images\IMG_0303.JPG')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),
                           self.pix.height(),
                           QPixmap('.\images\IDcardN.JPG'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = AbnormityWindow()
    mainWin.show()
    sys.exit(app.exec_())