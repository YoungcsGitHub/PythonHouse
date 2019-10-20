# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ClipBoard
# Description:  
# Author:       Dell
# Date:         2019/10/6
#-------------------------------------------------------------------------------

'''

使用剪贴板

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ClipBoardDemo(QDialog):
    def __init__(self):
        super(ClipBoardDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('剪贴板演示')
        self.resize(300, 200)

        textCopyButton = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textLabel = QLabel('默认文本')
        self.imageLabel = QLabel()
        # self.imageLabel.setPixmap(QPixmap('Basilisk.jpg'))

        layout = QGridLayout()
        layout.addWidget(textCopyButton,0,0)
        layout.addWidget(textPasteButton,0,1)
        layout.addWidget(htmlCopyButton,0,2)
        layout.addWidget(htmlPasteButton,1,0)
        layout.addWidget(imageCopyButton,1,1)
        layout.addWidget(imagePasteButton,1,2)

        layout.addWidget(self.textLabel,2,0,1,2)
        layout.addWidget(self.imageLabel,2,2)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('Hello World')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('Basilisk.jpg'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ClipBoardDemo()
    mainWin.show()
    sys.exit(app.exec_())