"""
    Material properteis

    @author: Dmytro Kuksenko
    @date: Sep 28, 2022
"""


class Material:
    def __init__(self, name, props, thx, dt, dm, theta=None):
        self.name = name
        self.props = props
        self.thickness = thx
        self.dt = dt
        self.dm = dm
        self.theta = None

    def __len__(self):
        return len(self.props)

    def __getitem__(self, key):
        return self.props[key]

    def __setitem__(self, key, val):
        self.props[key] = val
        return self.props[key]

    def __str__(self):
        return f"The material is {self.name}"


class Iso(Material):
    pass


class TransOrtho(Material):
    pass


class Ortho(Material):
    pass


class Aniso(Material):
    pass
