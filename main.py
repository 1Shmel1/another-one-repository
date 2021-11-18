import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 502)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pB_create_circle = QtWidgets.QPushButton(self.centralwidget)
        self.pB_create_circle.setGeometry(QtCore.QRect(160, 60, 161, 41))
        self.pB_create_circle.setObjectName("pB_create_circle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pB_create_circle.setText(_translate("MainWindow", "Создать окружность"))


class CircleCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pB_create_circle.clicked.connect(self.startPaint)

    def startPaint(self):
        self.update()

    def paintEvent(self, event: QPaintEvent):
        paint = QPainter()
        paint.begin(self)
        self.draw_circle(paint)
        paint.end()

    def draw_circle(self, qp: QPainter):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = QColor(r, g, b)
        qp.setBrush(color)

        r = randint(10, 300)
        qp.drawEllipse(150, 200, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleCreator()
    ex.show()
    sys.exit(app.exec())
