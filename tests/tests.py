"""
    Main tests for the composite analysis software.

    @author: Dmytro Kuksenko
    @date: Oct 5, 2022
"""
from composite_analysis import __version__
from composite_analysis.material import Iso, TransOrtho, Ortho, Aniso

def test_version():
    """Tests a software version."""
    assert __version__ == "0.1.0"

def test_new_iso_mat():
    """Tests a creation of a new isotropic material"""
    assert Iso() is not None 

def test_new_trans_mat():
    """Tests a creation of a new transversely isotropic material"""
    assert TransOrtho() is not None

def test_new_ortho_mat():
    """Tests a creation of a new orthotropic material"""
    assert Ortho() is not None

def test_new_aniso_mat():
    """Tests a creation of a new anisotropic material"""
    assert Aniso() is not None

def test_len_trans_mat():
    """Tests a to"""
    assert len(TransOrtho(props=[1,2,3,4,5])) == 5
