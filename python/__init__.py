#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# This application is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# The presence of this file turns this directory into a Python package

# import swig generated symbols into the howto namespace
from rds_swig import *

# import any pure python here
# First check for Qt5
qt5_available = False
try:
    from PyQt5 import Qt, QtCore, QtWidgets
    from gnuradio import gr
    if gr.version().startswith('3.8.'):
        qt5_available = True
    
except ImportError, e:
    print(e)
    qt5_available = False


if qt5_available:
    from rdspanel import *
else:
    print('Could not import "RDS Panel"!')
