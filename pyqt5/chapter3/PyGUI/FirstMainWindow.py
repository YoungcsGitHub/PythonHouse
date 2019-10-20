import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

# from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        # 设置窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口尺寸
        self.resize(600, 400)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./images/Dragon.ico'))
    mainWin = FirstMainWin()
    mainWin.show()
    sys.exit(app.exec_())
