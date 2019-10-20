import sys
# 导入相关模块
import MainWindow1

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建一个应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainWindow = QMainWindow()
    # 引用类，由自动生成的类接管
    ui = MainWindow1.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    # 显示窗口
    mainWindow.show()
    # 退出应用程序
    sys.exit(app.exec_())