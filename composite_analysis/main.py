"""
    Desing and Simulation of Composite Materials.

    @author: Dmytro Kuksenko
    @date: Sept 21, 2022
"""

import numpy as np
import sys
import PyQt6.QtWidgets as QtWidets

from mainwindow import MainWindow


if __name__ == "__main__":
    app = QtWidets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

