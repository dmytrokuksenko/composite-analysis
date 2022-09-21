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

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        laminate_analysis = menu.addMenu("&Laminate Analysis")
        filament_winding = menu.addMenu("&Filament Winding")
        report = menu.addMenu("&Report")
        help = menu.addMenu("&Help")
        about = menu.addMenu("&About")
