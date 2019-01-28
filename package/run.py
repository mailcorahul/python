"""A package(in a sense it is also a module) is a collection of python modules
or scripts
Adding __init__.py inside a folder in your current path makes Python treats them
as packages(or modules)

Why?
	- User-defined folders can collide with pre-defined python modules

"""

import pkg
import sys
sys.path.append('pkg_no_init')
import mod

print(pkg.arange(10));