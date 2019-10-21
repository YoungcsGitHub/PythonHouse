# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Counter
# Description:  
# Author:       Dell
# Date:         2019/10/21
#-------------------------------------------------------------------------------

'''

使用线程类 （QThread）编写计数器

从QThread 派生子类：

def run(self):
    while True:
        self.sleep(1)
        if sec == 5:
            break

QLCDNumber  模拟LED显示效果的空间  类似一个label

用到自定义信号

自定义类 WorkThread（QThread）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

sec = 0

class WorkThread(QThread):
    timer = pyqtSignal()        # 每隔1秒发送一个信号
    end = pyqtSignal()          # 计数完成后发送一次信号
    def run(self):
        while True:
            self.sleep(1)       # 休眠1秒
            if sec == 5:
                self.end.emit() # 发送end信号
                break
            self.timer.emit()   # 发送timer信号
class CounterDemo(QWidget):
    def __init__(self, parent=None):
        super(CounterDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Counter Demo')
        self.resize(430, 230)

        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()

        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        layout.addWidget(button)

        self.workThread = WorkThread()

        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    def countTime(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    def work(self):
        self.workThread.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CounterDemo()
    mainWin.show()
    sys.exit(app.exec_())