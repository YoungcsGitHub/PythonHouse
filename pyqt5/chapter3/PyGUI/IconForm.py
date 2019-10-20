import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()
    def initUI(self):
        # 设置坐标系
        self.setGeometry(300,300,250,250)
        # 设置窗口的标题
        self.setWindowTitle('设置窗口图标')
        # 设置窗口图标
        self.setWindowIcon(QIcon('./image/Basilisk.jpg'))
        # 获取窗口状态栏
        self.status = self.statusBar()
        # 向状态栏添加显示信息并限定时间
        self.status.showMessage('只存在5秒的消息...', 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./image/Basilisk.jpg'))
    mainWin = IconForm()
    mainWin.show()
    sys.exit(app.exec_())
