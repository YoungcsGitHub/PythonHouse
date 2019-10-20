import sys
from PyQt5.QtWidgets import QHBoxLayout,QPushButton,QMainWindow,QApplication,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,240)
        self.setWindowTitle('退出应用程序')

        # 添加Button1
        self.button1 = QPushButton('退出应用程序')
        # 将信号（单击）与槽（按钮1）关联
        self.button1.clicked.connect(self.onClick_Button)
        # 设置水平布局
        layout = QHBoxLayout()
        # 添加按钮1到窗口
        layout.addWidget(self.button1)
        # 添加主框架
        mainFrame = QWidget()
        # 将布局放置到mainFrame组件上
        mainFrame.setLayout(layout)
        # 把主框架放到整个窗口上
        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.move(300,400)
    main.show()

    sys.exit(app.exec_())