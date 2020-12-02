from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QColor, QPainter

from random_circles_2.py_form import Ui_MainWindow

from random import randint

import sys


class Master(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_soft()

    def main_soft(self):
        self.pushButton.clicked.connect(self.click)

        self.flag = False

    def paintEvent(self, event):
        if not self.flag:
            return

        qp = QPainter()
        qp.begin(self)

        self.draw_circles(qp)

        qp.end()

    def draw_circles(self, qp):
        r, g, b = [randint(0, 255) for i in range(3)]
        qp.setBrush(QColor(r, g, b))
        qp.setPen(QColor(r, g, b))

        radius = randint(20, 150)

        x, y = radius + randint(0, self.size().width() - 3 * radius), radius + randint(0, 460 - 3 * radius)

        qp.drawEllipse(x, y, 2 * radius, 2 * radius)

    def click(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    qpp = QApplication(sys.argv)
    ent = Master()
    ent.show()
    sys.exit(qpp.exec())