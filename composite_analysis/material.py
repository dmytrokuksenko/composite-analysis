"""
    Material properteis

    @author: Dmytro Kuksenko
    @date: Sep 28, 2022
"""


class Material():

    def __init__(self, name=None, props=None):
        self.name = name
        self.props = props
    
    def __len__(self):
        return len(self.props)

class Iso(Material):
    pass

class TransOrtho(Material):
    pass

class Ortho(Material):
    pass

class Aniso(Material):
    pass
    