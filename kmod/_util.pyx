# Copyright (C) 2012 Red Hat, Inc. All rights reserved.
#               2012 W. Trevor King
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions
# of the GNU Lesser General Public License v.2.1.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import sys as _sys

cimport _libkmod_h


cdef object char_ptr_to_str(_libkmod_h.const_char_ptr char_ptr):
    if char_ptr is NULL:
        return None
    if _sys.version_info >= (3,):  # Python 3
        return str(char_ptr, 'ascii')
    # Python 2
    return unicode(char_ptr, 'ascii')