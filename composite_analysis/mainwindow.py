"""
    Main window of the graphical user interface (GUI).

    @author: Dmytro Kuksenko
    @date: Sept 21, 2022 
"""

import PyQt6.QtWidgets as QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desing & Simulation of Composite Materials")