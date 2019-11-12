# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         QSSSubControl
# Description:  
# Author:       Dell
# Date:         2019/10/24
#-------------------------------------------------------------------------------

'''

QSS子控件选择器

QComboBox

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys, math
import os


class QSSSubControl(QWidget):
    def __init__(self):
        super(QSSSubControl, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSSSubControl Demo')
        self.resize(430, 230)

        combo = QComboBox(self)
        combo.setObjectName("myComboBox")
        combo.addItem('Windows')
        combo.addItem('Linux')
        combo.addItem('MacOS X')

        combo.move(50, 50)

        self.setGeometry(250, 200, 320, 150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QSSSubControl()
    qssStyle = '''
        QComboBox#myComboBox::drop-down {
            image:url(./images/Knob Download.ico)
        }
    '''
    mainWin.setStyleSheet(qssStyle)
    mainWin.show()
    sys.exit(app.exec_())