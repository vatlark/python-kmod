# Copyright (C) 2012 Red Hat, Inc.
#                    W. Trevor King <wking@tremily.us>
#
# This file is part of python-kmod.
#
# python-kmod is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License version 2.1 as published
# by the Free Software Foundation.
#
# python-kmod is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with python-kmod.  If not, see <http://www.gnu.org/licenses/>.
from setuptools import setup
from distutils.extension import Extension as _Extension
import os as _os
import sys as _sys
import platform

# setuptools DWIM monkey-patch madness
# http://mail.python.org/pipermail/distutils-sig/2007-September/thread.html#8204
import sys
if sys.version_info < (3,0):
    if 'setuptools.extension' in sys.modules:
        m = sys.modules['setuptools.extension']
        m.Extension.__dict__ = m._Extension.__dict__

package_name = 'kmod'

# read version from local kmod/version.py without pulling in
# kmod/__init__.py
_sys.path.insert(0, package_name)
from version import __version__


_this_dir = _os.path.dirname(__file__)

ext_modules = []
if platform.system() == "Linux":
    for filename in sorted(_os.listdir(package_name)):
        basename,extension = _os.path.splitext(filename)
        if extension == '.pyx':
            ext_modules.append(
                _Extension(
                    '{0}.{1}'.format(package_name, basename),
                    [_os.path.join(package_name, filename)],
                    libraries=['kmod'],
                    ))

setup(
    name=package_name,
    version=__version__,
    description='Python binding for kmod',
    packages=[package_name],
    provides=[package_name],
    maintainer="Andy Grover",
    maintainer_email="agrover@redhat.com",
    ext_modules=ext_modules,
    install_requires=["Cython"],
    setup_requires=["setuptools_cython"],
    )
