import random
import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class SqPainter(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            size = self.size()
            r = random.randint(10, 300)
            w, h = self.width(), self.height()
            x = random.randint(0, w - r)
            y = random.randint(0, h - r - 50)
            print(size)
            qp.setBrush(QColor(random.randint(0, 0xfffff)))

            qp.drawEllipse(x, y, 2 * r, 2 * r)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SqPainter()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
