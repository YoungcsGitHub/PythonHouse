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




app = QApplication(sys.argv)
mainWin = QMainWindow()
mainWin.setWindowTitle('背景图片')
mainWin.resize(640, 480)
mainWin.setObjectName("MainWindow")

# 通过QSS动态修改窗口的背景颜色和背景图片
mainWin.setStyleSheet("#MainWindow{border-image:url(./images/Basilisk.jpg);")
# mainWin.setStyleSheet("#MainWindow{background-color: yellow}")


# 通过QPalette设置背景图片和背景色
# palette = QPalette()
# palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/Basilisk.jpg")))
# mainWin.setPalette(palette)
mainWin.show()
sys.exit(app.exec())