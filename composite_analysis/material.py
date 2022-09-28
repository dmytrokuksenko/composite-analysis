"""
    Material properteis

    @author: Dmytro Kuksenko
    @date: Sep 28, 2022
"""


class Material:

    def __init__(self, *args, **kwargs):
        
        for key, value in kwargs.items():
            self.key = value
        

    def __str__(self, name):
        return f'The material is {name}'


class Composite(Material):
    def __init__ (self, **kwarg):
        Material.__init__(self, **kwarg)


class Metal(Material):
    def __init__ (self, **kwarg):
        Material.__init__(self, **kwarg)

    