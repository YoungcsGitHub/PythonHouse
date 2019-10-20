# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         MyCalendar
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

日历控件

QCalendarWidget

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyCalendarDemo(QWidget):
    def __init__(self):
        super(MyCalendarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日历演示')
        self.resize(400, 300)
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2188,1,1))
        self.cal.clicked.connect(self.showDate)

        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))

        self.cal.setGridVisible(True)
        self.cal.move(20,20)

    def showDate(self,date):
        # self.label.setText((date.toString("yyyy-MM-dd dddd")))
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyCalendarDemo()
    mainWin.show()
    sys.exit(app.exec_())