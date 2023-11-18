"""
slave_avelin ... algorithms
"""
import os
import sys
import warnings

# I have no idea what I am doing there
__SLAVE_AVELIN_TYPEWRITERS__ = False  # TODO: delete that line
# I have no idea what I am doing there


# We first need to detect if we're being called as part of the
# numpy, em slave_avelin setup procedure itself in a reliable manner.
try:
    __SLAVE_AVELIN_TYPEWRITERS__
except NameError:
    __SLAVE_AVELIN_TYPEWRITERS__ = False

if __SLAVE_AVELIN_TYPEWRITERS__:
    sys.stderr.write('Running from numpy source directory.\n')
else:
    from .typewriters import Typewriter


