# QDesktopWidget
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QDesktopWidget

# from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        # 设置窗口的标题
        self.setWindowTitle('让窗口居中')

        # 设置窗口尺寸
        self.resize(600, 400)
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft,newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./images/Dragon.ico'))
    mainWin = CenterForm()
    mainWin.show()
    sys.exit(app.exec_())
