"""
    A set of visualization tools with PyQtGraph.

    @author: Dmytro Kuksenko
    @date: Sept 22, 2022
"""

import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget
import numpy as np


class Plot(PlotWidget):

    def __init__(self):
        PlotWidget.__init__(self)
        self.set_graph()

    def set_graph(self):
        
        self.setBackground('w')
        self.setTitle('Stress-Strain Curve', color='b', size='14pt')
        self.setLabel('left', 'Stress', color='k')
        self.setLabel('bottom', 'Strain', color='k')
        self.addLegend()
        self.showGrid(x=True, y=True)
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 3, 4, 5]
        self.plot_line(x, y, title='Test', color='r')


    def plot_line(self, x, y, title, color):
        self.plot(x, y, name=title, color=color, symbol='+', symbolSize=10)