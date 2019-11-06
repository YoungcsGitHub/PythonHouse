import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        qbtn = QPushButton('Quit', self)
        qbtn.resize(250, 150)
        # qbtn.resize(80, 30)
        qbtn.move(50, 50)
        qbtn.setProperty("name", "qbtn")
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Quit Button')
        # qbtn.clicked.connect(self.change_css)
        # self.show()

    """
    def change_css(self):
        self.pushButton_2.setStyleSheet(("QPushButton{\n"
                                                  "   text-decoration:none;  \n"
                                                  "    background:#05B8CC;\n"
                                                  "    color:#f2f2f2;  \n"
                                                  "      \n"
                                                  "    padding: 10px 30px 10px 30px;  \n"
                                                  "    font-size:16px;  \n"
                                                  "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                                  "    font-weight:bold;  \n"
                                                  "    border-radius:3px;  \n"
                                                  "}\n"
                                                  ))"""

    def change_css(self, qssStyle):
        qssStyle = """
            QPushButton[name="qbtn"] {
                
                text-decoration:none;
                
                }
        
        """


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    qssStyle = """
                QPushButton[name="qbtn"] {
                    
                    text-decoration:none;
                    background:#05B8CC;
                    color:#f2f2f2;  
                     
                    padding: 10px 30px 10px 30px;
                    font-size:16px;
                    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;
                    font-weight:bold;
                    border-radius:3px;
                    }
    """
    ex.setStyleSheet(qssStyle)
    ex.show()
    sys.exit(app.exec_())