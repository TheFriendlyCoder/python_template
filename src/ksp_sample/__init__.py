"""Project Short Description"""
import logging
import os
import ast

_cur_file = os.path.realpath(__file__)
_cur_path = os.path.split(_cur_file)[0]
_props = open(os.path.join(_cur_path, 'version.prop')).read()
__version__ = ast.literal_eval(_props)

logging.getLogger(__name__).addHandler(logging.NullHandler())
