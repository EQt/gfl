"""
In this module, we determine the path of the extension module libgraphfl
"""

from setuptools.command.build_ext import build_ext
from setuptools.dist import Distribution
from os import path

__all__ = ['libgraphfl']

b = build_ext(Distribution())
libgraphfl = b.get_ext_filename('libgraphfl')
libgraphfl = path.normpath(path.join(path.dirname(__file__), '..', libgraphfl))
