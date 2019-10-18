from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class calcMethod(QMainWindow):
    def __init__(self):
        super(calcMethod, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计算公式集合')
        self.resize(400,300)

        layout = QVBoxLayout()

        label1 = QLabel(self)
        label1.setText("<font color = red>3600</font>")
        label1.setAlignment(Qt.AlignCenter)


        layout.addWidget(label1)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = calcMethod()
    mainWin.show()
    sys.exit(app.exec_())