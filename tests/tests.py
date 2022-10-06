"""
    Main tests for the composite analysis software.

    @author: Dmytro Kuksenko
    @date: Oct 5, 2022
"""
from composite_analysis import __version__
from composite_analysis.material import Composite, Metal

def test_version():
    assert __version__ == "0.1.0"

def test_new_composite_material():
    assert Composite() is not None 

def test_new_metal_material():
    assert Composite() is not None 