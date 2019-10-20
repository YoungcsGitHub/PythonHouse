import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,\
                            QToolTip,QPushButton,QWidget,QHBoxLayout
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()
    def initUI(self):
        # 设置坐标系
        self.setGeometry(1200,300,450,250)
        # 设置窗口的标题
        self.setWindowTitle('设置窗口图标')
        QToolTip.setFont(QFont('KaiTi', 12))
        self.setToolTip('今天是<b>星期五</b>')

        self.button = QPushButton('这是一个按钮')
        self.button.setToolTip('这是我的一个按钮，Are u ok？')

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFram = QWidget()
        mainFram.setLayout(layout)

        self.setCentralWidget(mainFram)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TooltipForm()
    mainWin.show()
    sys.exit(app.exec_())
