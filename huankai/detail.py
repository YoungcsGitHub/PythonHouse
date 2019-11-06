import sys
from PyQt5 import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Detail(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这个是QCheckBox的构造器。
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # 要设置窗口标题，我们就要检查单选框的状态。
        # 默认情况下，窗口没有标题，单选框未选中。
        cb.toggle()
        # 把changeTitle()方法和stateChanged信号关联起来。
        # 这样，changeTitle()就能切换窗口标题了。
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()
    def changeTitle(self, state):
        # 控件的状态是由changeTitle()方法控制的，
        # 如果空间被选中，我们就给窗口添加一个标题，
        # 如果没被选中，就清空标题。
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ui_Detail()
    # ex.show()
    sys.exit(app.exec_())