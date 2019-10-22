# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         InnerHTML
# Description:  
# Author:       Dell
# Date:         2019/10/22
#-------------------------------------------------------------------------------

'''

显示嵌入的HTML代码

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys


class InnerHTML(QMainWindow):
    def __init__(self):
        super(InnerHTML, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('InnerHTML Demo')
        # self.resize(430, 230)
        self.setGeometry(5, 30, 1355, 730)

        self.browser = QWebEngineView()
        self.browser.setHtml('''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试页面</title>
</head>
<body>
    <h1>Hello PyQt5</h1>
    <h2>Hello PyQt5</h2>
    <h3>Hello PyQt5</h3>
    <h4>Hello PyQt5</h4>
</body>
</html>
        ''')
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = InnerHTML()
    mainWin.show()
    sys.exit(app.exec_())