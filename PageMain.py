import sys
from PySide6.QtWidgets import *
from PageLogin import *

if __name__ == '__main__':
    app = QApplication([])
    window = LoginApp()
    window.show()
    app.exec()
