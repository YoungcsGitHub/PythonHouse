'''

单选按钮控件（QRadioButton）

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        self.resize(320,100)
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        # self.button2.setChecked(True)
        layout.addWidget(self.button2)

        self.button1.toggled.connect(self.buttonState)
        self.button2.toggled.connect(self.buttonState)

        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QRadioButtonDemo()
    mainWin.show()
    sys.exit(app.exec_())