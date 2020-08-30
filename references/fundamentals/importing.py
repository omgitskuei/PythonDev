"""
Overview of importing modules in Python.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""

# -*- coding: utf-8 -*-

from time import localtime
from time import asctime

"""
Syntax:
    import [module name]
    or
    from [module name] import [module class/function]
"""

t = localtime()
print(asctime(t))
# same as time.asctime(time.localtime()), if you had used "import time" at top
