'''

按钮控件（QPushButton）

QAbstractButton

QPushButton   普通按钮
AToolButton   工具条按钮
QRadioButton  单选按钮
QCheckBox     多选按钮（复选框）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')
        self.resize(300,400)

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        layout.addWidget(self.button1)

        # 在文本前面显示图像

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('Basilisk.jpg')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QPushButtonDemo()
    mainWin.show()
    sys.exit(app.exec_())