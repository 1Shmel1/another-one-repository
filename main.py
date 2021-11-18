import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from random import randint
from PyQt5 import uic


class CircleCreator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pB_create_circle.clicked.connect(self.startPaint)

    def startPaint(self):
        self.update()

    def paintEvent(self, event: QPaintEvent):
        paint = QPainter()
        paint.begin(self)
        self.draw_circle(paint)
        paint.end()

    def draw_circle(self, qp: QPainter):
        color = QColor(255, 255, 0)
        qp.setBrush(color)

        r = randint(10, 300)
        qp.drawEllipse(150, 200, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleCreator()
    ex.show()
    sys.exit(app.exec())
