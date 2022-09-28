"""
    A set of visualization tools with PyQtGraph.

    @author: Dmytro Kuksenko
    @date: Sept 22, 2022
"""

import matplotlib.pyplot as plt
import pyqtgraph as pg
import numpy as np


class Plot(pg.PlotWidget):

    def __init__(self):
        pg.PlotWidget.__init__(self)
        self.set_graph()

    def set_graph(self):
        self.setBackground('w')
        self.setTitle('Stress-Strain Curve', color='b', size='14pt')
        self.setLabel('left', 'Stress', color='k')
        self.setLabel('bottom', 'Strain', color='k')
        self.addLegend()

    def plot_line(self, x, y, title, color):
        self.plot(x, y, name=title, color=color, symbol='*', symbolSize=10)