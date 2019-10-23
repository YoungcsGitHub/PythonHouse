# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         AbsoluteLayout
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

绝对布局

'''

from PyQt5.QtWidgets import *

import sys,math



class AbsoluteLayoutDemo(QWidget):
    def __init__(self):
        super(AbsoluteLayoutDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AbsoluteLayout Demo')
        self.resize(430, 230)

        self.label1 = QLabel('欢迎',self)
        self.label1.move(15,20)

        self.label2 = QLabel('学习', self)
        self.label2.move(35, 40)

        self.label3 = QLabel('PyQt5', self)
        self.label3.move(55, 80)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = AbsoluteLayoutDemo()
    mainWin.show()
    sys.exit(app.exec_())