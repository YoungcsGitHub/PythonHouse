'''
QLabel控件
setAlignment(): 设置文本的对其方式
setIndent():    设置文本缩进
text():         获取文本内容
setBuddy():     获取伙伴关系
setText():      设置文本内容
selectedText(): 返回所选择的字符
setWordWrap():  设置是否允许换行

QLabel常用的信号（事件）：
1. 当鼠标滑过QLabel控件时触发： linkHovered
2. 当鼠标单机QLabel控件时触发： linkActivated
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo,self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        # 支持附文本<font color = yellow>XXXXXXX</font>
        label1.setText('<font color = yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue) # 设置背景颜色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter) # 设置文字对齐方式
        # 只使用#号，并没有使用html
        label2.setText("<a href = '#'>欢迎使用Python GUI程序</a>")

        label3.setToolTip('这是一个图片标签')
        label3.setAlignment(Qt.AlignCenter)
        # 将标签设置为图片
        label3.setPixmap(QPixmap('./image/Basilisk.jpg'))

        label4.setText(" <a href = 'https://item.jd.com/12317265.html'>感谢关注《Python从菜鸟到高手》</a>")
        label4.setToolTip('这是一个超级链接')
        label4.setAlignment(Qt.AlignRight)
        label4.setOpenExternalLinks(False)
        # 设置垂直布局
        vbox = QVBoxLayout()
        # 将四个标签分别添加到布局上
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        # 将两个信号绑定到两个槽函数上
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        # 设置布局
        self.setLayout(vbox)
        # 设置标题栏信息
        self.setWindowTitle('QLabel控件显示')

    # 定义槽函数
    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')
    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')
# 运行主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLabelDemo()
    mainWin.show()
    sys.exit(app.exec_())