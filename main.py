import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(lambda: self.repaint())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 204, 0))
        for i in range(randrange(1, 7)):
            parm = randrange(15, 100)
            qp.drawEllipse(randrange(10, 400), randrange(10, 400), parm, parm)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())