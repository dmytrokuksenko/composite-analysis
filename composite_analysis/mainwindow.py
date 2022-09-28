"""
    Main window of the graphical user interface (GUI).

    @author: Dmytro Kuksenko
    @date: Sept 21, 2022
"""

from PyQt6 import QtWidgets, QtGui
from plot import Plot


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set title for the main window
        self.setWindowTitle("Desing & Simulation of Composite Materials")
        self.setGeometry(100, 100, 800, 400)

        layout = QtWidgets.QVBoxLayout()
        self.grapWidget = Plot()
        layout.addWidget(self.grapWidget)
        self.refresh_button = QtWidgets.QPushButton('Refresh')
        layout.addWidget(self.refresh_button)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.refresh_button.setCheckable(True)
        self.refresh_button.clicked.connect(self.on_refreshed_clicked)


        # Add menu bar to the software layout
        menu = self.menuBar()

        # Add items to File menu bar
        file_menu = menu.addMenu("&File")
        self.exit = QtGui.QAction("Exit", self)
        self.open = QtGui.QAction("Open...", self)
        self.save = QtGui.QAction("Save...", self)
        file_menu.addAction(self.open)
        file_menu.addAction(self.save)
        file_menu.addAction(self.exit)

        self.open.triggered.connect(self.on_refreshed_clicked)

        # Add items to Laminate Analysis menu bar
        laminate_analysis = menu.addMenu("&Laminate Analysis")
        self.effective_props = QtGui.QAction("Effective Properties", self)
        self.failure = QtGui.QAction("Failure Analysis", self)
        self.failure_envelope = QtGui.QAction("Failure Envelop", self)
        laminate_analysis.addAction(self.effective_props)
        laminate_analysis.addAction(self.failure)
        laminate_analysis.addAction(self.failure_envelope)

        # Add items to Filament Winding menu bar
        filament_winding = menu.addMenu("&Filament Winding")

        # Add items to Mircomechanics menu bar
        micormechanics = menu.addMenu("&Micromechanics")

        # Add items to Report menu bar
        report = menu.addMenu("&Report")

        # Add items to Help menu bar
        help = menu.addMenu("&Help")
        self.about = QtGui.QAction("About", self)
        self.help = QtGui.QAction("Help", self)
        help.addAction(self.help)
        help.addAction(self.about)

    def on_refreshed_clicked(self):
        layout = QtWidgets.QVBoxLayout()
        self.refresh_button = QtWidgets.QPushButton('Refresh')
        layout.addWidget(self.refresh_button)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)