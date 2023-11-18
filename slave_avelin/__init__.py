"""
slave_avelin
=====

Provides
  1. Easyer homework

How to use the documentation
----------------------------
Documentation is available in future

Available subpackages
---------------------
MathSlave
    Algorithms that are used in math, for example modular reverse, etc.

Utilities
---------
test
    Run unittests

"""
import os
import sys
import warnings

# I have no idea what I am doing there
__SLAVE_AVELIN_SETUP__ = False  # TODO: delete that line
# I have no idea what I am doing there


# We first need to detect if we're being called as part of the
# numpy, em slave_avelin setup procedure itself in a reliable manner.
try:
    __SLAVE_AVELIN_SETUP__
except NameError:
    __SLAVE_AVELIN_SETUP__ = False

if __SLAVE_AVELIN_SETUP__:
    sys.stderr.write('Running from numpy source directory.\n')
else:
    from .src import algorithms
    from .src import typewriters


