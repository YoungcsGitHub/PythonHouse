# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         DateTimeEdit
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

输入各种风格的日期和时间
QDateTimeEdit

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置不同风格的日期和时间')
        self.resize(300, 100)

        layout = QVBoxLayout()

        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit = dateTimeEdit1

        dateTimeEdit2.setCalendarPopup(True)

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd hh-mm-ss")

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.btn = QPushButton('获取日期和时间')
        self.btn.clicked.connect(self.onButtonClick)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    # 日期变化
    def onDateChanged(self,date):
        print(date)

    def onTimeChanged(self,time):
        print(time)

    def onDateTimeChanged(self, datetime):
        print(datetime)

    def onButtonClick(self):
        datetime = self.dateTimeEdit.dateTime()
        print(datetime)

        # 最大日期
        print(self.dateTimeEdit.maximumDate())
        # 最大日期和时间
        print(self.dateTimeEdit.maximumDateTime())
        # 最小日期
        print(self.dateTimeEdit.minimumDate())
        # 最小日期和时间
        print(self.dateTimeEdit.maximumDateTime())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = DateTimeEditDemo()
    mainWin.show()
    sys.exit(app.exec_())