from PyQt5.Qt import *


class MyLabel(QLabel):

    def clear_points(self):
        [child.deleteLater() for child in self.children() if child.inherits("QPushButton")]

    def get_result(self):

        result = ",".join(["{}, {}".format(child.x()+10, child.y()-20) for child in self.children() if child.inherits("QPushButton")])
        print(result)
        return result

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.x() < 0 or evt.y() <= 30:
            return None

        point = QPushButton(self)
        point.resize(20, 20)
        point.move(evt.pos() - QPoint(10, 10))
        point.setStyleSheet("background-color:red; border-radius:10px;")
        point.show()

        point.clicked.connect(lambda _, btn=point: btn.deleteLater())

