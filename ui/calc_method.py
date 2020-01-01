from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect

import sys

class calcMethod(QWidget):
    def __init__(self):
        super(calcMethod, self).__init__()
        self.initUI()

    def center(self):
        screen = QDesktopWidget().screenGeometry()

        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

    def initUI(self):
        self.setWindowTitle('计算公式集合')
        self.resize(400,300)

        formlayout = QFormLayout()
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()

        label = QLabel('3600*ADC/(2^14)/A')

        spacerItem1 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Expanding)
        spacerItem2 = QSpacerItem(260, 20, QSizePolicy.Maximum, QSizePolicy.Expanding)

        # label1 = QLabel(self)
        # label1.setText("<font color = red>3600</font>")
        # label1.setAlignment(Qt.AlignCenter)

        self.numline1 = QLineEdit()
        self.numline2 = QLineEdit()
        self.numline3 = QLineEdit()
        self.numline4 = QLineEdit()

        self.textvalue = QTextEdit()

        self.btn = QPushButton('计算')
        self.btn.clicked.connect(self.btnclicked)
        # btn.setGeometry(QRect(650, 450, 75, 23))

        self.numline1.setText('3600')
        self.numline3.setText('%s' % (2 ** 14))

        self.numline1.setPlaceholderText('常数')
        self.numline2.setPlaceholderText('ADC')
        self.numline3.setPlaceholderText('2^14')
        self.numline4.setPlaceholderText('A')


        # vlayout.addWidget()
        hlayout.addItem(spacerItem2)
        hlayout.addWidget(self.btn)

        formlayout.addRow('计算公式:',label)
        formlayout.addItem(spacerItem1)
        formlayout.addRow("常数   :", self.numline1)
        formlayout.addRow("ADC    :", self.numline2)
        formlayout.addRow("2^14   :", self.numline3)
        formlayout.addRow("A      :", self.numline4)
        formlayout.addRow('计算结果:', self.textvalue)
        # formlayout.addRow(btn)
        formlayout.addItem(hlayout)

        self.setLayout(formlayout)

        self.center()

        # self.calculate()

    def calculate(self):
        while True:
            if self.numline4.text() and self.numline2.text() is not '':
                try:
                    num1 = float(self.numline1.text())
                    ADC = float(self.numline2.text())
                    # print(self.numline2.text())
                    num2 = float(self.numline3.text())
                    amplification = float(self.numline4.text())
                    self.value = num1 * ADC / num2 / amplification
                except Exception as ret:
                    print(ret)
            else:
                QMessageBox.information(self, "warning", " %s " % "ADC 和 amplification 数值为空！")
            break

    def btnclicked(self):
        self.calculate()
        self.textvalue.setText('%s' % self.value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = calcMethod()
    mainWin.show()
    sys.exit(app.exec_())