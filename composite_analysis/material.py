"""
    Material properteis

    @author: Dmytro Kuksenko
    @date: Sep 28, 2022
"""


class Material():

    def __init__(self, name, props):
        self.name = name
        self.props = props


class Composite(Material):
    pass


class Metal(Material):
    pass

    