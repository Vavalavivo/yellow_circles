from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic

from random import randint

import sys


class Master(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_form.ui', self)
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
        qp.setBrush(QColor(231, 237, 107))
        qp.setPen(QColor(231, 237, 107))

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