"""
    A set of functions for data pre-processing.

    @author: Dmytro Kuksenko
    @date: Sep 28, 2022
"""

import yaml


def get_material_props(file_name=None):
    
    if not file_name:
        assert("Please provide a name of the file")
    else:
        with open('composite_analysis/parameters.yaml') as f:
            props = yaml.safe_load(f)

    return props