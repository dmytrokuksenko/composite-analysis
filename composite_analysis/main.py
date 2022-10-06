"""
    Desing and Simulation of Composite Materials.

    @author: Dmytro Kuksenko
    @date: Sept 21, 2022
"""

import sys
from PyQt6 import QtWidgets
from composite_analysis.layup import abd_estimation

from mainwindow import MainWindow

if __name__ == "__main__":

    # app = QtWidgets.QApplication(sys.argv)
    # main = MainWindow()
    # main.show()
    # sys.exit(app.exec())
    abd_estimation()