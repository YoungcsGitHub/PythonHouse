# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ScrollBar
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''

滚动条控件  QScrollBar

QScrollBar的作用：

1. 通过滚动条值的变化控制其他控件的状态变化
2. 通过滚动条值的变化控制控件位置的变化

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys


class ScrollBarDemo(QWidget):
    def __init__(self):
        super(ScrollBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ScrollBar Demo')
        self.resize(430, 230)

        hbox = QHBoxLayout()
        self.label = QLabel('拖动滚动条去改变文字颜色')

        hbox.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)

        self.scrollbar4 = QScrollBar()
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.sliderMoved.connect(self.sliderMoved1)

        hbox.addWidget(self.scrollbar1)
        hbox.addWidget(self.scrollbar2)
        hbox.addWidget(self.scrollbar3)
        hbox.addWidget(self.scrollbar4)

        self.setGeometry(600, 300, 600, 400)

        self.setLayout(hbox)

        self.y = self.label.pos().y()

    def sliderMoved(self):
        print(self.scrollbar1.value(),
              self.scrollbar2.value(),
              self.scrollbar3.value())
        palette = QPalette()
        c = QColor(self.scrollbar1.value(),
                   self.scrollbar2.value(),
                   self.scrollbar3.value(),255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        self.label.move(self.label.x(), self.y + self.scrollbar4.value())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ScrollBarDemo()
    mainWin.show()
    sys.exit(app.exec_())