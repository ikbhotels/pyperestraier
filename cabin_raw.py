################################################################################################
# The utitlity API of QDBM
#                                                      Copyright (C) 2000-2007 Mikio Hirabayashi
# This file is part of QDBM, Quick Database Manager.
# QDBM is free software; you can redistribute it and/or modify it under the terms of the GNU
# Lesser General Public License as published by the Free Software Foundation; either version
# 2.1 of the License or any later version.  QDBM is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
# You should have received a copy of the GNU Lesser General Public License along with QDBM; if
# not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# 02111-1307 USA.
################################################################################################

from ctypes import CDLL, POINTER, c_int, c_uint, c_long, c_double
from ctypes import c_char_p, c_void_p, c_size_t

libest_raw = CDLL("libestraier.so")

############################################################
# API
############################################################

CB_DATUMUNIT   = 12                # allocation unit size of a datum handle
CB_LISTUNIT    = 64                # allocation unit number of a list handle
CB_MAPBNUM     = 4093              # bucket size of a map handle

# /* Call back function for handling a fatal error.
#    The argument specifies the error message.  The initial value of this variable is `NULL'.
#    If the value is `NULL', the default function is called when a fatal error occurs. A fatal
#    error occurs when memory allocation is failed. */
# MYEXTERN void (*cbfatalfunc)(const char *);

# void *cbmalloc(size_t size);
cbmalloc = libest_raw.cbmalloc
cbmalloc.__doc__ = \
    "Allocate a region on memory.\n"\
    "`size' specifies the size of the region.\n"\
    "The return value is the pointer to the allocated region.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbmalloc.restype = c_void_p
cbmalloc.argtypes = [c_size_t]

# void *cbrealloc(void *ptr, size_t size);
cbrealloc = libest_raw.cbrealloc
cbrealloc.__doc__ = \
    "Re-allocate a region on memory.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "The return value is the pointer to the re-allocated region.\n"\
    "Because the region of the return value is allocated with the `realloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbrealloc.restype = c_void_p
cbrealloc.argtypes = [c_void_p, c_size_t]

# char *cbmemdup(const char *ptr, int size);
cbmemdup = libest_raw.cbmemdup
cbmemdup.__doc__ = \
    "Duplicate a region on memory.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the pointer to the allocated region of the duplicate.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if\n"\
    "it is no longer in use."
cbmemdup.restype = c_char_p
cbmemdup.argtypes = [c_char_p, c_int]

# void cbfree(void *ptr);
cbfree = libest_raw.cbfree
cbfree.__doc__ = \
    "Free a region on memory.\n"\
    "`ptr' specifies the pointer to a region.  If it is `NULL', this function has no effect.\n"\
    "Although this function is just a wrapper of `free' call, this is useful in applications using\n"\
    "another package of the `malloc' series."
cbfree.restype = None
cbfree.argtypes = [c_void_p]

# void cbglobalgc(void *ptr, void (*func)(void *));
cbglobalgc = libest_raw.cbglobalgc
cbglobalgc.__doc__ = \
    "Register the pointer or handle of an object to the global garbage collector.\n"\
    "`ptr' specifies the pointer or handle of an object.\n"\
    "`func' specifies the pointer to a function to release resources of the object.  Its argument\n"\
    "is the pointer or handle of the object to release.\n"\
    "This function assures that resources of an object are released when the process exits\n"\
    "normally by returning from the `main' function or calling the `exit' function."
cbglobalgc.restype = None
cbglobalgc.argtypes = [c_void_p, c_void_p]

# void cbggcsweep(void);
cbggcsweep = libest_raw.cbggcsweep
cbggcsweep.__doc__ = \
    "Exercise the global garbage collector explicitly.\n"\
    "Note that you should not use objects registered to the global garbage collector any longer\n"\
    "after calling this function.  Because the global garbage collecter is initialized and you\n"\
    "can register new objects into it."
cbggcsweep.restype = None
cbggcsweep.argtypes = []

# int cbvmemavail(size_t size);
cbvmemavail = libest_raw.cbvmemavail
cbvmemavail.__doc__ = \
    "Check availability of allocation of the virtual memory.\n"\
    "`size' specifies the size of region to be allocated newly.\n"\
    "The return value is true if allocation should be success, or false if not."
cbvmemavail.restype = c_int
cbvmemavail.argtypes = [c_size_t]




# CBLIST *cblistopen(void);
cblistopen = libest_raw.cblistopen
cblistopen.__doc__ = \
    "Get a list handle.\n"\
    "The return value is a list handle."
cblistopen.restype = c_void_p
cblistopen.argtypes = []

# CBLIST *cblistdup(const CBLIST *list);
cblistdup = libest_raw.cblistdup
cblistdup.__doc__ = \
    "Copy a list.\n"\
    "`list' specifies a list handle.\n"\
    "The return value is a new list handle."
cblistdup.restype = c_void_p
cblistdup.argtypes = [c_void_p]

# void cblistclose(CBLIST *list);
cblistclose = libest_raw.cblistclose
cblistclose.__doc__ = \
    "Close a list handle.\n"\
    "`list' specifies a list handle.\n"\
    "Because the region of a closed handle is released, it becomes impossible to use the handle."
cblistclose.restype = None
cblistclose.argtypes = [c_void_p]

# int cblistnum(const CBLIST *list);
cblistnum = libest_raw.cblistnum
cblistnum.__doc__ = \
    "Get the number of elements of a list.\n"\
    "`list' specifies a list handle.\n"\
    "The return value is the number of elements of the list."
cblistnum.restype = c_int
cblistnum.argtypes = [c_void_p]

# const char *cblistval(const CBLIST *list, int index, int *sp);
cblistval = libest_raw.cblistval
cblistval.__doc__ = \
    "Get the pointer to the region of an element of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`index' specifies the index of an element.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the value.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  If `index' is equal to or more than\n"\
    "the number of elements, the return value is `NULL'."
cblistval.restype = c_char_p
cblistval.argtypes = [c_void_p, c_int, POINTER(c_int)]

# void cblistpush(CBLIST *list, const char *ptr, int size);
cblistpush = libest_raw.cblistpush
cblistpush.__doc__ = \
    "Add an element at the end of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`ptr' specifies the pointer to the region of an element.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'."
cblistpush.restype = None
cblistpush.argtypes = [c_void_p, c_char_p, c_int]

# char *cblistpop(CBLIST *list, int *sp);
cblistpop = libest_raw.cblistpop
cblistpop.__doc__ = \
    "Remove an element of the end of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the value.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  If the list is empty, the return value is `NULL'."
cblistpop.restype = c_char_p
cblistpop.argtypes = [c_void_p, c_int]

# void cblistunshift(CBLIST *list, const char *ptr, int size);
cblistunshift = libest_raw.cblistunshift
cblistunshift.__doc__ = \
    "Add an element at the top of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`ptr' specifies the pointer to the region of an element.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
"`strlen(ptr)'."
cblistunshift.restype = None
cblistunshift.argtypes = [c_void_p, c_char_p, c_int]

# char *cblistshift(CBLIST *list, int *sp);
cblistshift = libest_raw.cblistshift
cblistshift.__doc__ = \
    "Remove an element of the top of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used."\
    "The return value is the pointer to the region of the value.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  If the list is empty, the return value is `NULL'."
cblistshift.restype = c_char_p
cblistshift.argtypes = [c_void_p, POINTER(c_int)]

# void cblistinsert(CBLIST *list, int index, const char *ptr, int size);
cblistinsert = libest_raw.cblistinsert
cblistinsert.__doc__ = \
    "Add an element at the specified location of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`index' specifies the index of an element.\n"\
    "`ptr' specifies the pointer to the region of the element.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'."
cblistinsert.restype = None
cblistinsert.argtypes = [c_void_p, c_int, c_char_p, c_int]

# char *cblistremove(CBLIST *list, int index, int *sp);
cblistremove = libest_raw.cblistremove
cblistremove.__doc__ = \
    "Remove an element at the specified location of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`index' specifies the index of an element.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the value.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  If `index' is equal to or more than the number of elements, no element\n"\
    "is removed and the return value is `NULL'."
cblistremove.restype = c_char_p
cblistremove.argtypes = [c_void_p, c_int, POINTER(c_int)]

# void cblistover(CBLIST *list, int index, const char *ptr, int size);
cblistover = libest_raw.cblistover
cblistover.__doc__ = \
    "Overwrite an element at the specified location of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`index' specifies the index of an element.\n"\
    "`ptr' specifies the pointer to the region of the new content.\n"\
    "`size' specifies the size of the new content.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "If `index' is equal to or more than the number of elements, this function has no effect."
cblistover.restype = None
cblistover.argtypes = [c_void_p, c_int, c_char_p, c_int]

# void cblistsort(CBLIST *list);
cblistsort = libest_raw.cblistsort
cblistsort.__doc__ = \
    "Sort elements of a list in lexical order.\n"\
    "`list' specifies a list handle.\n"\
    "Quick sort is used for sorting."
cblistsort.restype = None
cblistsort.argtypes = [c_void_p]

# int cblistlsearch(const CBLIST *list, const char *ptr, int size);
cblistlsearch = libest_raw.cblistlsearch
cblistlsearch.__doc__ = \
    "Search a list for an element using liner search.\n"\
    "`list' specifies a list handle.\n"\
    "`ptr' specifies the pointer to the region of a key.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the index of a corresponding element or -1 if there is no corresponding\n"\
    "element.  If two or more elements corresponds, the former returns."
cblistlsearch.restype = c_int
cblistlsearch.argtypes = [c_void_p, c_char_p, c_int]

# int cblistbsearch(const CBLIST *list, const char *ptr, int size);
cblistbsearch = libest_raw.cblistbsearch
cblistbsearch.__doc__ = \
    "Search a list for an element using binary search.\n"\
    "`list' specifies a list handle.  It should be sorted in lexical order.\n"\
    "`ptr' specifies the pointer to the region of a key.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the index of a corresponding element or -1 if there is no corresponding\n"\
    "element.  If two or more elements corresponds, which returns is not defined."
cblistbsearch.restype = c_int
cblistbsearch.argtypes = [c_void_p, c_char_p, c_int]

# char *cblistdump(const CBLIST *list, int *sp);
cblistdump = libest_raw.cblistdump
cblistdump.__doc__ = \
    "Serialize a list into a byte array.\n"\
    "`list' specifies a list handle.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "The return value is the pointer to the region of the result serial region.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cblistdump.restype = c_char_p
cblistdump.argtypes = [c_void_p, POINTER(c_int)]

# CBLIST *cblistload(const char *ptr, int size);
cblistload = libest_raw.cblistload
cblistload.__doc__ = \
    "Redintegrate a serialized list.\n"\
    "`ptr' specifies the pointer to a byte array.\n"\
    "`size' specifies the size of the region.\n"\
    "The return value is a new list handle."
cblistload.restype = c_void_p
cblistload.argtypes = [c_char_p, c_int]

# CBMAP *cbmapopen(void);
cbmapopen = libest_raw.cbmapopen
cbmapopen.__doc__ = \
    "Get a map handle.\n"\
    "The return value is a map handle."
cbmapopen.restype = c_void_p
cbmapopen.argtypes = []

# CBMAP *cbmapdup(CBMAP *map);
cbmapdup = libest_raw.cbmapdup
cbmapdup.__doc__ = \
    "Copy a map.\n"\
    "`map' specifies a map handle.\n"\
    "The return value is a new map handle.\n"\
    "The iterator of the source map is initialized."
cbmapdup.restype = c_void_p
cbmapdup.argtypes = [c_void_p]

# void cbmapclose(CBMAP *map);
cbmapclose = libest_raw.cbmapclose
cbmapclose.__doc__ = \
    "Close a map handle.\n"\
    "`map' specifies a map handle.\n"\
    "Because the region of a closed handle is released, it becomes impossible to use the handle."
cbmapclose.restype = None
cbmapclose.argtypes = [c_void_p]

# int cbmapput(CBMAP *map, const char *kbuf, int ksiz, const char *vbuf, int vsiz, int over);
cbmapput = libest_raw.cbmapput
cbmapput.__doc__ = \
    "Store a record into a map.\n"\
    "`map' specifies a map handle.\n"\
    "`kbuf' specifies the pointer to the region of a key.\n"\
    "`ksiz' specifies the size of the region of the key.  If it is negative, the size is assigned\n"\
    "with `strlen(kbuf)'.\n"\
    "`vbuf' specifies the pointer to the region of a value.\n"\
    "`vsiz' specifies the size of the region of the value.  If it is negative, the size is\n"\
    "assigned with `strlen(vbuf)'.\n"\
    "`over' specifies whether the value of the duplicated record is overwritten or not.\n"\
    "If `over' is false and the key is duplicated, the return value is false, else, it is true."
cbmapput.restype = c_int
cbmapput.argtypes = [c_void_p, c_char_p, c_int, c_char_p, c_int, c_int]

# void cbmapputcat(CBMAP *map, const char *kbuf, int ksiz, const char *vbuf, int vsiz);
cbmapputcat = libest_raw.cbmapputcat
cbmapputcat.__doc__ = \
    "Concatenate a value at the end of the value of the existing record.\n"\
    "`map' specifies a map handle.\n"\
    "`kbuf' specifies the pointer to the region of a key.\n"\
    "`ksiz' specifies the size of the region of the key.  If it is negative, the size is assigned\n"\
    "with `strlen(kbuf)'.\n"\
    "`vbuf' specifies the pointer to the region of a value.\n"\
    "`vsiz' specifies the size of the region of the value.  If it is negative, the size is\n"\
    "assigned with `strlen(vbuf)'.\n"\
    "If there is no corresponding record, a new record is created."
cbmapputcat.restype = None
cbmapputcat.argtypes = [c_void_p, c_char_p, c_int, c_char_p, c_int]

# int cbmapout(CBMAP *map, const char *kbuf, int ksiz);
cbmapout = libest_raw.cbmapout
cbmapout.__doc__ = \
    "Delete a record in a map.\n"\
    "`map' specifies a map handle.\n"\
    "`kbuf' specifies the pointer to the region of a key.\n"\
    "`ksiz' specifies the size of the region of the key.  If it is negative, the size is assigned\n"\
    "with `strlen(kbuf)'.\n"\
    "If successful, the return value is true.  False is returned when no record corresponds to\n"\
    "the specified key."
cbmapout.restype = c_int
cbmapout.argtypes = [c_void_p, c_char_p, c_int]

# const char *cbmapget(const CBMAP *map, const char *kbuf, int ksiz, int *sp);
cbmapget = libest_raw.cbmapget
cbmapget.__doc__ = \
    "Retrieve a record in a map.\n"\
    "`map' specifies a map handle.\n"\
    "`kbuf' specifies the pointer to the region of a key.\n"\
    "`ksiz' specifies the size of the region of the key.  If it is negative, the size is assigned\n"\
    "with `strlen(kbuf)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the region of the value of the\n"\
    "corresponding record.  `NULL' is returned when no record corresponds.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
"the return value can be treated as a character string."
cbmapget.restype = c_char_p
cbmapget.argtypes = [c_void_p, c_char_p, c_int, POINTER(c_int)]

# int cbmapmove(CBMAP *map, const char *kbuf, int ksiz, int head);
cbmapmove = libest_raw.cbmapmove
cbmapmove.__doc__ = \
    "Move a record to the edge of a map.\n"\
    "`map' specifies a map handle.\n"\
    "`kbuf' specifies the pointer to the region of a key.\n"\
    "`ksiz' specifies the size of the region of the key.  If it is negative, the size is assigned\n"\
    "with `strlen(kbuf)'.\n"\
    "`head' specifies the destination which is head if it is true or tail if else.\n"\
    "If successful, the return value is true.  False is returned when no record corresponds to\n"\
    "the specified key."
cbmapmove.restype = c_int
cbmapmove.argtypes = [c_void_p, c_char_p, c_int, c_int]

# void cbmapiterinit(CBMAP *map);
cbmapiterinit = libest_raw.cbmapiterinit
cbmapiterinit.__doc__ = \
    "Initialize the iterator of a map.\n"\
    "`map' specifies a map handle.\n"\
    "The iterator is used in order to access the key of every record stored in a map."
cbmapiterinit.restype = None
cbmapiterinit.argtypes = [c_void_p]

# const char *cbmapiternext(CBMAP *map, int *sp);
cbmapiternext = libest_raw.cbmapiternext
cbmapiternext.__doc__ = \
    "Get the next key of the iterator of a map.\n"\
    "`map' specifies a map handle.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the region of the next key, else, it is\n"\
    "`NULL'.  `NULL' is returned when no record is to be get out of the iterator.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  The order of iteration is assured\n"\
    "to be the same of the one of storing."
cbmapiternext.restype = c_char_p
cbmapiternext.argtypes = [c_void_p, POINTER(c_int)]

# const char *cbmapiterval(const char *kbuf, int *sp);
cbmapiterval = libest_raw.cbmapiterval
cbmapiterval.__doc__ = \
    "Get the value binded to the key fetched from the iterator of a map.\n"\
    "`kbuf' specifies the pointer to the region of a iteration key.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the value of the corresponding record.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string."
cbmapiterval.restype = c_char_p
cbmapiterval.argtypes = [c_char_p, POINTER(c_int)]

# int cbmaprnum(const CBMAP *map);
cbmaprnum = libest_raw.cbmaprnum
cbmaprnum.__doc__ = \
    "Get the number of the records stored in a map.\n"\
    "`map' specifies a map handle.\n"\
    "The return value is the number of the records stored in the map."
cbmaprnum.restype = c_int
cbmaprnum.argtypes = [c_void_p]

# CBLIST *cbmapkeys(CBMAP *map);
cbmapkeys = libest_raw.cbmapkeys
cbmapkeys.__doc__ = \
    "Get the list handle contains all keys in a map.\n"\
    "`map' specifies a map handle.\n"\
    "The return value is the list handle contains all keys in the map.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use."
cbmapkeys.restype = c_void_p
cbmapkeys.argtypes = [c_void_p]

# CBLIST *cbmapvals(CBMAP *map);
cbmapvals = libest_raw.cbmapvals
cbmapvals.__doc__ = \
    "Get the list handle contains all values in a map.\n"\
    "`map' specifies a map handle.\n"\
    "The return value is the list handle contains all values in the map.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use."
cbmapvals.restype = c_void_p
cbmapvals.argtypes = [c_void_p]

# char *cbmapdump(CBMAP *map, int *sp);
cbmapdump = libest_raw.cbmapdump
cbmapdump.__doc__ = \
    "Serialize a map into a byte array.\n"\
    "`map' specifies a map handle.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "The return value is the pointer to the region of the result serial region.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbmapdump.restype = c_char_p
cbmapdump.argtypes = [c_void_p, POINTER(c_int)]

# CBMAP *cbmapload(const char *ptr, int size);
cbmapload = libest_raw.cbmapload
cbmapload.__doc__ = \
    "Redintegrate a serialized map.\n"\
    "`ptr' specifies the pointer to a byte array.\n"\
    "`size' specifies the size of the region.\n"\
    "The return value is a new map handle."
cbmapload.restype = c_void_p
cbmapload.argtypes = [c_char_p, c_int]

# char *cbmaploadone(const char *ptr, int size, const char *kbuf, int ksiz, int *sp);
cbmaploadone = libest_raw.cbmaploadone
cbmaploadone.__doc__ = \
    "Extract a record from a serialized map.\n"\
    "`ptr' specifies the pointer to a byte array.\n"\
    "`size' specifies the size of the region.\n"\
    "`kbuf' specifies the pointer to the region of a key.\n"\
    "`ksiz' specifies the size of the region of the key.  If it is negative, the size is assigned\n"\
    "with `strlen(kbuf)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the region of the value of the\n"\
    "corresponding record.  `NULL' is returned when no record corresponds.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string."
cbmaploadone.restype = c_char_p
cbmaploadone.argtypes = [c_char_p, c_int, c_char_p, c_int, c_int]

# CBHEAP *cbheapopen(int size, int max, int(*compar)(const void *, const void *));
cbheapopen = libest_raw.cbheapopen
cbheapopen.__doc__ = \
    "Get a heap handle.\n"\
    "`size' specifies the size of each record.\n"\
    "`max' specifies the maximum number of records in the heap.\n"\
    "`compar' specifies the pointer to comparing function.  The two arguments specify the pointers\n"\
    "of records.  The comparing function should returns positive if the former is big, negative\n"\
    "if the latter is big, 0 if both are equal.\n"\
    "The return value is a heap handle."
cbheapopen.restype = c_void_p
cbheapopen.argtypes = [c_int, c_int, c_void_p]

# CBHEAP *cbheapdup(CBHEAP *heap);
cbheapdup = libest_raw.cbheapdup
cbheapdup.__doc__ = \
    "Copy a heap.\n"\
    "`heap' specifies a heap handle.\n"\
    "The return value is a new heap handle."
cbheapdup.restype = c_void_p
cbheapdup.argtypes = [c_void_p]

# void cbheapclose(CBHEAP *heap);
cbheapclose = libest_raw.cbheapclose
cbheapclose.__doc__ = \
    "Close a heap handle.\n"\
    "`heap' specifies a heap handle.\n"\
    "Because the region of a closed handle is released, it becomes impossible to use the handle."
cbheapclose.restype = None
cbheapclose.argtypes = [c_void_p]

# int cbheapnum(CBHEAP *heap);
cbheapnum = libest_raw.cbheapnum
cbheapnum.__doc__ = \
    "Get the number of the records stored in a heap.\n"\
    "`heap' specifies a heap handle.\n"\
    "The return value is the number of the records stored in the heap."
cbheapnum.restype = c_int
cbheapnum.argtypes = [c_void_p]

# int cbheapinsert(CBHEAP *heap, const void *ptr);
cbheapinsert = libest_raw.cbheapinsert
cbheapinsert.__doc__ = \
    "Insert a record into a heap.\n"\
    "`heap' specifies a heap handle.\n"\
    "`ptr' specifies the pointer to the region of a record.\n"\
    "The return value is true if the record is added, else false.\n"\
    "If the new record is bigger than the biggest existing regord, the new record is not added.\n"\
    "If the new record is added and the number of records exceeds the maximum number, the biggest\n"\
    "existing record is removed."
cbheapinsert.restype = c_int
cbheapinsert.argtypes = [c_void_p, c_void_p]

# const void *cbheapval(CBHEAP *heap, int index);
cbheapval = libest_raw.cbheapval
cbheapval.__doc__ = \
    "Get the pointer to the region of a record in a heap.\n"\
    "`heap' specifies a heap handle.\n"\
    "`index' specifies the index of a record.\n"\
    "The return value is the pointer to the region of the record.\n"\
    "If `index' is equal to or more than the number of records, the return value is `NULL'.  Note\n"\
    "that records are organized by the nagative order the comparing function."
cbheapval.restype = c_void_p
cbheapval.argtypes = [c_void_p, c_int]

# void *cbheaptomalloc(CBHEAP *heap, int *np);
cbheaptomalloc = libest_raw.cbheaptomalloc
cbheaptomalloc.__doc__ = \
    "Convert a heap to an allocated region.\n"\
    "`heap' specifies a heap handle.\n"\
    "`np' specifies the pointer to a variable to which the number of records of the return value\n"\
    "is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the heap.  Records are sorted.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use.  Because the region of the original\n"\
    "heap is released, it should not be released again."
cbheaptomalloc.restype = c_void_p
cbheaptomalloc.argtypes = [c_void_p, POINTER(c_int)]

# char *cbsprintf(const char *format, ...);
cbsprintf = libest_raw.cbsprintf
cbsprintf.__doc__ = \
    "Allocate a formatted string on memory.\n"\
    "`format' specifies a printf-like format string.  The conversion character `%' can be used\n"\
    "with such flag characters as `d', `o', `u', `x', `X', `e', `E', `f', `g', `G', `c', `s', and\n"\
    "`%'.  Specifiers of the field length and the precision can be put between the conversion\n"\
    "characters and the flag characters.  The specifiers consist of decimal characters, `.', `+',\n"\
    "`-', and the space character.\n"\
    "The other arguments are used according to the format string.\n"\
    "The return value is the pointer to the allocated region of the result string.  Because the\n"\
    "region of the return value is allocated with the `malloc' call, it should be released with\n"\
    "the `free' call if it is no longer in use."
cbsprintf.restype = c_char_p
# cbsprintf.argtypes = [c_char_p, ]

# char *cbreplace(const char *str, CBMAP *pairs);
cbreplace = libest_raw.cbreplace
cbreplace.__doc__ = \
    "Replace some patterns in a string.\n"\
    "`str' specifies the pointer to a source string.\n"\
    "`pairs' specifies the handle of a map composed of pairs of replacement.  The key of each pair\n"\
    "specifies a pattern before replacement and its value specifies the pattern after replacement.\n"\
    "The return value is the pointer to the allocated region of the result string.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbreplace.restype = c_char_p
cbreplace.argtypes = [c_char_p, c_void_p]

# CBLIST *cbsplit(const char *ptr, int size, const char *delim);
cbsplit = libest_raw.cbsplit
cbsplit.__doc__ = \
    "Make a list by splitting a serial datum.\n"\
    "`ptr' specifies the pointer to the region of the source content.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`delim' specifies a string containing delimiting characters.  If it is `NULL', zero code is\n"\
    "used as a delimiter.\n"\
    "The return value is a list handle.\n"\
    "If two delimiters are successive, it is assumed that an empty element is between the two.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose'."
cbsplit.restype = c_void_p
cbsplit.argtypes = [c_char_p, c_int, c_char_p]

# char *cbreadfile(const char *name, int *sp);
cbreadfile = libest_raw.cbreadfile
cbreadfile.__doc__ = \
    "Read whole data of a file.\n"\
    "`name' specifies the name of a file.  If it is `NULL', the standard input is specified.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the allocated region of the read data.  Because an\n"\
    "additional zero code is appended at the end of the region of the return value, the return\n"\
    "value can be treated as a character string.  Because the region of the return value is\n"\
    "allocated with the `malloc' call, it should be released with the `free' call if it is no\n"\
    "longer in use."
cbreadfile.restype = c_char_p
cbreadfile.argtypes = [c_char_p, POINTER(c_int)]

# int cbwritefile(const char *name, const char *ptr, int size);
cbwritefile = libest_raw.cbwritefile
cbwritefile.__doc__ = \
    "Write a serial datum into a file.\n"\
    "`name specifies the name of a file.  If it is `NULL', the standard output is specified.\n"\
    "`ptr' specifies the pointer to the region of the source content.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "If successful, the return value is true, else, it is false.\n"\
    "If the file exists, it is overwritten.  Else, a new file is created."
cbwritefile.restype = c_int
cbwritefile.argtypes = [c_char_p, c_char_p, c_int]

# CBLIST *cbreadlines(const char *name);
cbreadlines = libest_raw.cbreadlines
cbreadlines.__doc__ = \
    "Read every line of a file.\n"\
    "`name' specifies the name of a file.  If it is `NULL', the standard input is specified.\n"\
    "The return value is a list handle of the lines if successful, else it is NULL.  Line\n"\
    "separators are cut out.  Because the handle of the return value is opened with the function\n"\
    "`cblistopen', it should be closed with the function `cblistclose' if it is no longer in use."
cbreadlines.restype = c_void_p
cbreadlines.aargtypes = [c_char_p]

# CBLIST *cbdirlist(const char *name);
cbdirlist = libest_raw.cbdirlist
cbdirlist.__doc__ = \
    "Read names of files in a directory.\n"\
    "`name' specifies the name of a directory.\n"\
    "The return value is a list handle of names if successful, else it is NULL.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use."
cbdirlist.restype = c_void_p
cbdirlist.argtypes = [c_char_p]

# int cbfilestat(const char *name, int *isdirp, int *sizep, time_t *mtimep);
cbfilestat = libest_raw.cbfilestat
cbfilestat.__doc__ = \
    "Get the status of a file or a directory.\n"\
    "`name' specifies the name of a file or a directory.\n"\
    "`dirp' specifies the pointer to a variable to which whether the file is a directory is\n"\
    "assigned.  If it is `NULL', it is not used.\n"\
    "`sizep' specifies the pointer to a variable to which the size of the file is assigned.  If it\n"\
    "is `NULL', it is not used.\n"\
    "`mtimep' specifies the pointer to a variable to which the last modified time of the file is\n"\
    "assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is true, else, false.  False is returned when the file does\n"\
    "not exist or the permission is denied."
cbfilestat.restype = c_int
cbfilestat.argtypes = [c_char_p, POINTER(c_int), POINTER(c_int), POINTER(c_long)] # time_t

# int cbremove(const char *name);
cbremove = libest_raw.cbremove
cbremove.__doc__ = \
    "Remove a file or a directory and its sub ones recursively.\n"\
    "`name' specifies the name of a file or a directory.\n"\
    "If successful, the return value is true, else, false.  False is returned when the file does\n"\
    "not exist or the permission is denied."
cbremove.restype = c_int
cbremove.argtypes = [c_char_p]

# CBMAP *cburlbreak(const char *str);
cburlbreak = libest_raw.cburlbreak
cburlbreak.__doc__ = \
    "Break up a URL into elements.\n"\
    "`str' specifies the pointer to a string of URL.\n"\
    "The return value is a map handle.  Each key of the map is the name of an element.  The key\n"\
    "\"self\" specifies the URL itself.  The key \"scheme\" specifies the scheme.  The key \"host\"\n"\
    "specifies the host of the server.  The key \"port\" specifies the port number of the server.\n"\
    "The key \"authority\" specifies the authority information.  The key \"path\" specifies the path\n"\
    "of the resource.  The key \"file\" specifies the file name without the directory section.  The\n"\
    "key \"query\" specifies the query string.  The key \"fragment\" specifies the fragment string.\n"\
    "Supported schema are HTTP, HTTPS, FTP, and FILE.  Absolute URL and relative URL are supported.\n"\
    "Because the handle of the return value is opened with the function `cbmapopen', it should\n"\
    "be closed with the function `cbmapclose' if it is no longer in use."
cburlbreak.restype = c_void_p
cburlbreak.argtypes = [c_char_p]

# char *cburlresolve(const char *base, const char *target);
cburlresolve = libest_raw.cburlresolve
cburlresolve.__doc__ = \
    "Resolve a relative URL with another absolute URL.\n"\
    "`base' specifies an absolute URL of a base location.\n"\
    "`target' specifies a URL to be resolved.\n"\
    "The return value is a resolved URL.  If the target URL is relative, a new URL of relative\n"\
    "location from the base location is returned.  Else, a copy of the target URL is returned.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cburlresolve.restype = c_char_p
cburlresolve.argtypes = [c_char_p, c_char_p]

# char *cburlencode(const char *ptr, int size);
cburlencode = libest_raw.cburlencode
cburlencode.__doc__ = \
    "Encode a serial object with URL encoding.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the pointer to the result string.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cburlencode.restype = c_char_p
cburlencode.argtypes = [c_char_p, c_int]

# char *cburldecode(const char *str, int *sp);
cburldecode = libest_raw.cburldecode
cburldecode.__doc__ = \
    "Decode a string encoded with URL encoding.\n"\
    "`str' specifies the pointer to an encoded string.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the result.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if\n"\
    "it is no longer in use."
cburldecode.restype = c_char_p
cburldecode.argtypes = [c_char_p, POINTER(c_int)]

# char *cbbaseencode(const char *ptr, int size);
cbbaseencode = libest_raw.cbbaseencode
cbbaseencode.__doc__ = \
    "Encode a serial object with Base64 encoding.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the pointer to the result string.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbbaseencode.restype = c_char_p
cbbaseencode.argtypes = [c_char_p, c_int]

# char *cbbasedecode(const char *str, int *sp);
cbbasedecode = libest_raw.cbbasedecode
cbbasedecode.__doc__ = \
    "Decode a string encoded with Base64 encoding.\n"\
    "`str' specifies the pointer to an encoded string.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the result.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if\n"\
    "it is no longer in use."
cbbasedecode.restype = c_char_p
cbbasedecode.argtypes = [c_char_p, POINTER(c_int)]

# char *cbquoteencode(const char *ptr, int size);
cbquoteencode = libest_raw.cbquoteencode
cbquoteencode.__doc__ = \
    "Encode a serial object with quoted-printable encoding.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the pointer to the result string.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbquoteencode.restype = c_char_p
cbquoteencode.argtypes = [c_char_p, c_int]

# char *cbquotedecode(const char *str, int *sp);
cbquotedecode = libest_raw.cbquotedecode
cbquotedecode.__doc__ = \
    "Decode a string encoded with quoted-printable encoding.\n"\
    "`str' specifies the pointer to an encoded string.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the region of the result.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if\n"\
    "it is no longer in use."
cbquotedecode.restype = c_char_p
cbquotedecode.argtypes = [c_char_p, POINTER(c_int)]

# char *cbmimebreak(const char *ptr, int size, CBMAP *attrs, int *sp);
cbmimebreak = libest_raw.cbmimebreak
cbmimebreak.__doc__ = \
    "Split a string of MIME into headers and the body.\n"\
    "`ptr' specifies the pointer to the region of MIME data.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`attrs' specifies a map handle to store attributes.  If it is `NULL', it is not used.  Each\n"\
    "key of the map is an attribute name uncapitalized.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer of the body data.\n"\
    "If the content type is defined, the attribute map has the key \"TYPE\" specifying the type.  If\n"\
    "the character encoding is defined, the key \"CHARSET\" specifies the encoding name.  If the\n"\
    "boundary string of multipart is defined, the key \"BOUNDARY\" specifies the string.  If the\n"\
    "content disposition is defined, the key \"DISPOSITION\" specifies the direction.  If the file\n"\
    "name is defined, the key \"FILENAME\" specifies the name.  If the attribute name is defined,\n"\
    "the key \"NAME\" specifies the name.  Because the region of the return value is allocated with\n"\
    "the `malloc' call, it should be released with the `free' call if it is no longer in use"
cbmimebreak.restype = c_char_p
cbmimebreak.argtypes = [c_char_p, c_int, c_void_p, POINTER(c_int)]

# CBLIST *cbmimeparts(const char *ptr, int size, const char *boundary);
cbmimeparts = libest_raw.cbmimeparts
cbmimeparts.__doc__ = \
    "Split multipart data of MIME into its parts.\n"\
    "`ptr' specifies the pointer to the region of multipart data of MIME.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`boundary' specifies the pointer to the region of the boundary string.\n"\
    "The return value is a list handle.  Each element of the list is the string of a part.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use."
cbmimeparts.restype = c_void_p
cbmimeparts.argtypes = [c_char_p, c_int, c_char_p]

# char *cbmimeencode(const char *str, const char *encname, int base);
cbmimeencode = libest_raw.cbmimeencode
cbmimeencode.__doc__ = \
    "Encode a string with MIME encoding.\n"\
    "`str' specifies the pointer to a string.\n"\
    "`encname' specifies a string of the name of the character encoding.\n"\
    "The return value is the pointer to the result string.\n"\
    "`base' specifies whether to use Base64 encoding.  If it is false, quoted-printable is used.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbmimeencode.restype = c_char_p
cbmimeencode.argtypes = [c_char_p, c_char_p, c_int]

# char *cbmimedecode(const char *str, char *enp);
cbmimedecode = libest_raw.cbmimedecode
cbmimedecode.__doc__ = \
    "Decode a string encoded with MIME encoding.\n"\
    "`str' specifies the pointer to an encoded string.\n"\
    "`enp' specifies the pointer to a region into which the name of encoding is written.  If it is\n"\
    "`NULL', it is not used.  The size of the buffer should be equal to or more than 32 bytes.\n"\
    "The return value is the pointer to the result string.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbmimedecode.restype = c_char_p
cbmimedecode.argtypes = [c_char_p, c_char_p]

# CBLIST *cbcsvrows(const char *str);
cbcsvrows = libest_raw.cbcsvrows
cbcsvrows.__doc__ = \
    "Split a string of CSV into rows.\n"\
    "`str' specifies the pointer to the region of an CSV string.\n"\
    "The return value is a list handle.  Each element of the list is a string of a row.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use.  The character encoding\n"\
    "of the input string should be US-ASCII, UTF-8, ISO-8859-*, EUC-*, or Shift_JIS.  Being\n"\
    "compatible with MS-Excel, these functions for CSV can handle cells including such meta\n"\
    "characters as comma, between double quotation marks."
cbcsvrows.restype = c_void_p
cbcsvrows.argtypes = [c_char_p]

# CBLIST *cbcsvcells(const char *str);
cbcsvcells = libest_raw.cbcsvcells
cbcsvcells.__doc__ = \
    "Split the string of a row of CSV into cells.\n"\
    "`str' specifies the pointer to the region of a row of CSV.\n"\
    "The return value is a list handle.  Each element of the list is the unescaped string of a\n"\
    "cell of the row.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use."
cbcsvcells.restype = c_void_p
cbcsvcells.argtypes = [c_char_p]

# char *cbcsvescape(const char *str);
cbcsvescape = libest_raw.cbcsvescape
cbcsvescape.__doc__ = \
    "Escape a string with the meta characters of CSV.\n"\
    "`str' specifies the pointer to the region of a string.\n"\
    "The return value is the pointer to the escaped string sanitized of meta characters.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbcsvescape.restype = c_char_p
cbcsvescape.argtypes = [c_char_p]

# char *cbcsvunescape(const char *str);
cbcsvunescape = libest_raw.cbcsvunescape
cbcsvunescape.__doc__ = \
    "Unescape a string with the escaped meta characters of CSV.\n"\
    "`str' specifies the pointer to the region of a string with meta characters.\n"\
    "The return value is the pointer to the unescaped string.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbcsvunescape.restype = c_char_p
cbcsvunescape.argtypes = [c_char_p]

# CBLIST *cbxmlbreak(const char *str, int cr);
cbxmlbreak = libest_raw.cbxmlbreak
cbxmlbreak.__doc__ = \
    "Split a string of XML into tags and text sections.\n"\
    "`str' specifies the pointer to the region of an XML string.\n"\
    "`cr' specifies whether to remove comments.\n"\
    "The return value is a list handle.  Each element of the list is the string of a tag or a\n"\
    "text section.\n"\
    "Because the handle of the return value is opened with the function `cblistopen', it should\n"\
    "be closed with the function `cblistclose' if it is no longer in use.  The character encoding\n"\
    "of the input string should be US-ASCII, UTF-8, ISO-8859-*, EUC-*, or Shift_JIS.  Because\n"\
    "these functions for XML are not XML parser with validation check, it can handle also HTML\n"\
    "and SGML."
cbxmlbreak.restype = c_void_p
cbxmlbreak.argtypes = [c_char_p, c_int]

# CBMAP *cbxmlattrs(const char *str);
cbxmlattrs = libest_raw.cbxmlattrs
cbxmlattrs.__doc__ = \
    "Get the map of attributes of an XML tag.\n"\
    "`str' specifies the pointer to the region of a tag string.\n"\
    "The return value is a map handle.  Each key of the map is the name of an attribute.  Each\n"\
    "value is unescaped.  You can get the name of the tag with the key of an empty string.\n"\
    "Because the handle of the return value is opened with the function `cbmapopen', it should\n"\
    "be closed with the function `cbmapclose' if it is no longer in use."
cbxmlattrs.restype = c_void_p
cbxmlattrs.argtypes = [c_char_p]

# char *cbxmlescape(const char *str);
cbxmlescape = libest_raw.cbxmlescape
cbxmlescape.__doc__ = \
    "Escape a string with the meta characters of XML.\n"\
    "`str' specifies the pointer to the region of a string.\n"\
    "The return value is the pointer to the escaped string sanitized of meta characters.\n"\
    "This function converts only `&', `<', `>', and `\"'.  Because the region of the return value\n"\
    "is allocated with the `malloc' call, it should be released with the `free' call if it is no\n"\
    "longer in use."
cbxmlescape.restype = c_char_p
cbxmlescape.argtypes = [c_char_p]

# char *cbxmlunescape(const char *str);
cbxmlunescape = libest_raw.cbxmlunescape
cbxmlunescape.__doc__ = \
    "Unescape a string with the entity references of XML.\n"\
    "`str' specifies the pointer to the region of a string with meta characters.\n"\
    "The return value is the pointer to the unescaped string.\n"\
    "This function restores only `&amp;', `&lt;', `&gt;', and `&quot;'.  Because the region of the\n"\
    "return value is allocated with the `malloc' call, it should be released with the `free' call\n"\
    "if it is no longer in use."
cbxmlunescape.restype = c_char_p
cbxmlunescape.argtypes = [c_char_p]

# char *cbdeflate(const char *ptr, int size, int *sp);
cbdeflate = libest_raw.cbdeflate
cbdeflate.__doc__ = \
    "Compress a serial object with ZLIB.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use.  This function is available only if\n"\
    "QDBM was built with ZLIB enabled."
cbdeflate.restype = c_char_p
cbdeflate.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cbinflate(const char *ptr, int size, int *sp);
cbinflate = libest_raw.cbinflate
cbinflate.__doc__ = \
    "Decompress a serial object compressed with ZLIB.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  This function is available only if QDBM was built with ZLIB enabled."
cbinflate.restype = c_char_p
cbinflate.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cbgzencode(const char *ptr, int size, int *sp);
cbgzencode = libest_raw.cbgzencode
cbgzencode.__doc__ = \
    "Compress a serial object with GZIP.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use.  This function is available only if\n"\
    "QDBM was built with ZLIB enabled."
cbgzencode.restype = c_char_p
cbgzencode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cbgzdecode(const char *ptr, int size, int *sp);
cbgzdecode = libest_raw.cbgzdecode
cbgzdecode.__doc__ = \
    "Decompress a serial object compressed with GZIP.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  This function is available only if QDBM was built with ZLIB enabled."
cbgzdecode.restype = c_char_p
cbgzdecode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# unsigned int cbgetcrc(const char *ptr, int size);
cbgetcrc = libest_raw.cbgetcrc
cbgetcrc.__doc__ = \
    "Get the CRC32 checksum of a serial object.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the CRC32 checksum of the object.\n"\
    "This function is available only if QDBM was built with ZLIB enabled."
cbgetcrc.restype = c_uint
cbgetcrc.argtypes = [c_char_p, c_int]

# char *cblzoencode(const char *ptr, int size, int *sp);
cblzoencode = libest_raw.cblzoencode
cblzoencode.__doc__ = \
    "Compress a serial object with LZO.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use.  This function is available only if\n"\
    "QDBM was built with LZO enabled."
cblzoencode.restype = c_char_p
cblzoencode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cblzodecode(const char *ptr, int size, int *sp);
cblzodecode = libest_raw.cblzodecode
cblzodecode.__doc__ = \
    "Decompress a serial object compressed with LZO.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  This function is available only if QDBM was built with LZO enabled."
cblzodecode.restype = c_char_p
cblzodecode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cbbzencode(const char *ptr, int size, int *sp);
cbbzencode = libest_raw.cbbzencode
cbbzencode.__doc__ = \
    "Compress a serial object with BZIP2.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use.  This function is available only if\n"\
    "QDBM was built with LZO enabled."
cbbzencode.restype = c_char_p
cbbzencode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cbbzdecode(const char *ptr, int size, int *sp);
cbbzdecode = libest_raw.cbbzdecode
cbbzdecode.__doc__ = \
    "Decompress a serial object compressed with BZIP2.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  This function is available only if QDBM was built with LZO enabled."
cbbzdecode.restype = c_char_p
cbbzdecode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *cbiconv(const char *ptr, int size, const char *icode, const char *ocode, int *sp, int *mp);
cbiconv = libest_raw.cbiconv
cbiconv.__doc__ = \
    "Convert the character encoding of a string.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`icode' specifies the name of encoding of the input string.\n"\
    "`ocode' specifies the name of encoding of the output string.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "`mp' specifies the pointer to a variable to which the number of missing characters by failure\n"\
    "of conversion is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use.  This function is available only if QDBM was built with ICONV enabled."
cbiconv.restype = c_char_p
cbiconv.argtypes = [c_char_p, c_int, c_char_p, c_char_p, POINTER(c_int), POINTER(c_int)]

# const char *cbencname(const char *ptr, int size);
cbencname = libest_raw.cbencname
cbencname.__doc__ = \
    "Detect the encoding of a string automatically.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "The return value is the string of the encoding name of the string.\n"\
    "As it stands, US-ASCII, ISO-2022-JP, Shift_JIS, CP932, EUC-JP, UTF-8, UTF-16, UTF-16BE,\n"\
    "and UTF-16LE are supported.  If none of them matches, ISO-8859-1 is selected.  This function\n"\
    "is available only if QDBM was built with ICONV enabled."
cbencname.restype = c_char_p
cbencname.argtypes = [c_char_p, c_int]

# int cbjetlag(void);
cbjetlag = libest_raw.cbjetlag
cbjetlag.__doc__ = \
    "Get the jet lag of the local time in seconds.\n"\
    "The return value is the jet lag of the local time in seconds."
cbjetlag.restype = c_int
cbjetlag.argtypes = []

# void cbcalendar(time_t t, int jl, int *yearp, int *monp, int *dayp,
#                 int *hourp, int *minp, int *secp);
cbcalendar = libest_raw.cbcalendar
cbcalendar.__doc__ = \
    "Get the Gregorian calendar of a time.\n"\
    "`t' specifies a source time.  If it is negative, the current time is specified.\n"\
    "`jl' specifies the jet lag of a location in seconds.\n"\
    "`yearp' specifies the pointer to a variable to which the year is assigned.  If it is `NULL',\n"\
    "it is not used.\n"\
    "`monp' specifies the pointer to a variable to which the month is assigned.  If it is `NULL',\n"\
    "it is not used.  1 means January and 12 means December.\n"\
    "`dayp' specifies the pointer to a variable to which the day of the month is assigned.  If it\n"\
    "is `NULL', it is not used.\n"\
    "`hourp' specifies the pointer to a variable to which the hours is assigned.  If it is `NULL',\n"\
    "it is not used.\n"\
    "`minp' specifies the pointer to a variable to which the minutes is assigned.  If it is `NULL',\n"\
    "it is not used.\n"\
    "`secp' specifies the pointer to a variable to which the seconds is assigned.  If it is `NULL',\n"\
    "it is not used."
cbcalendar.restype = None
cbcalendar.argtypes = [c_long, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# int cbdayofweek(int year, int mon, int day);
cbdayofweek = libest_raw.cbdayofweek
cbdayofweek.__doc__ = \
    "Get the day of week of a date.\n"\
    "`year' specifies the year of a date.\n"\
    "`mon' specifies the month of the date.\n"\
    "`day' specifies the day of the date.\n"\
    "The return value is the day of week of the date.  0 means Sunday and 6 means Saturday."
cbdayofweek.restype = c_int
cbdayofweek.argtypes = [c_int, c_int, c_int]

# char *cbdatestrwww(time_t t, int jl);
cbdatestrwww = libest_raw.cbdatestrwww
cbdatestrwww.__doc__ = \
    "Get the string for a date in W3CDTF.\n"\
    "`t' specifies a source time.  If it is negative, the current time is specified.\n"\
    "`jl' specifies the jet lag of a location in seconds.\n"\
    "The return value is the string of the date in W3CDTF (YYYY-MM-DDThh:mm:ddTZD).\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbdatestrwww.restype = c_char_p
cbdatestrwww.argtypes = [c_long, c_int]

# char *cbdatestrhttp(time_t t, int jl);
cbdatestrhttp = libest_raw.cbdatestrhttp
cbdatestrhttp.__doc__ = \
    "Get the string for a date in RFC 1123 format.\n"\
    "`t' specifies a source time.  If it is negative, the current time is specified.\n"\
    "`jl' specifies the jet lag of a location in seconds.\n"\
    "The return value is the string of the date in RFC 1123 format (Wdy, DD-Mon-YYYY hh:mm:dd TZD).\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
cbdatestrhttp.restype = c_char_p
cbdatestrhttp.argtypes = [c_long, c_int]

# time_t cbstrmktime(const char *str);
cbstrmktime = libest_raw.cbstrmktime
cbstrmktime.__doc__ = \
    "Get the time value of a date string in decimal, hexadecimal, W3CDTF, or RFC 822 (1123).\n"\
    "`str' specifies a date string in decimal, hexadecimal, W3CDTF, or RFC 822 (1123).\n"\
    "The return value is the time value of the date or -1 if the format is invalid.\n"\
    "Decimal can be trailed by \"s\" for in seconds, \"m\" for in minutes, \"h\" for in hours,\n"\
    "and \"d\" for in days."
cbstrmktime.restype = c_long
cbstrmktime.argtypes = [c_char_p]

# void cbproctime(double *usrp, double *sysp);
cbproctime = libest_raw.cbproctime
cbproctime.__doc__ = \
    "Get user and system processing times.\n"\
    "`usrp' specifies the pointer to a variable to which the user processing time is assigned.\n"\
    "If it is `NULL', it is not used.  The unit of time is seconds.\n"\
    "`sysp' specifies the pointer to a variable to which the system processing time is assigned.\n"\
    "If it is `NULL', it is not used.  The unit of time is seconds."
cbproctime.restype = None
cbproctime.argtypes = [POINTER(c_double), POINTER(c_double)]

# void cbstdiobin(void);
cbstdiobin = libest_raw.cbstdiobin
cbstdiobin.__doc__ = \
    "Ensure that the standard I/O is binary mode.\n"\
    "This function is useful for applications on dosish file systems."
cbstdiobin.restype = None
cbstdiobin.argtypes = []


############################################################
# features for experts
############################################################

# void *cbmyfatal(const char *message);
cbmyfatal = libest_raw.cbmyfatal
cbmyfatal.__doc__ = \
    "Show error message on the standard error output and exit.\n"\
    "`message' specifies an error message.\n"\
    "This function does not return."
cbmyfatal.restype = c_void_p
cbmyfatal.argtypes = [c_char_p]

# CBDATUM *cbdatumopenbuf(char *ptr, int size);
cbdatumopenbuf = libest_raw.cbdatumopenbuf
cbdatumopenbuf.__doc__ = \
    "Create a datum handle from an allocated region.\n"\
    "`ptr' specifies the pointer to the region of an element.  The region should be allocated with\n"\
    "malloc and it is released by the function.\n"\
    "`size' specifies the size of the region."
cbdatumopenbuf.restype = c_void_p
cbdatumopenbuf.argtypes = [c_char_p, c_int]

# void cbdatumsetbuf(CBDATUM *datum, char *ptr, int size);
cbdatumsetbuf = libest_raw.cbdatumsetbuf
cbdatumsetbuf.__doc__ = \
    "Set a buffer to a datum handle.\n"\
    "`ptr' specifies the pointer to the region of an element.  The region should be allocated with\n"\
    "malloc and it is released by the function.\n"\
    "`size' specifies the size of the region."
cbdatumsetbuf.restype = None
cbdatumsetbuf.argtypes = [c_void_p, c_char_p, c_int]

# void cblistpushbuf(CBLIST *list, char *ptr, int size);
cblistpushbuf = libest_raw.cblistpushbuf
cblistpushbuf.__doc__ = \
    "Add an allocated element at the end of a list.\n"\
    "`list' specifies a list handle.\n"\
    "`ptr' specifies the pointer to the region of an element.  The region should be allocated with\n"\
    "malloc and it is released by the function.\n"\
    "`size' specifies the size of the region."
cblistpushbuf.restype = None
cblistpushbuf.argtypes = [c_void_p, c_char_p, c_int]

# CBMAP *cbmapopenex(int bnum);
cbmapopenex = libest_raw.cbmapopenex
cbmapopenex.__doc__ = \
    "Get a map handle with specifying the number of buckets.\n"\
    "`bnum' specifies the number of buckets.\n"\
    "The return value is a map handle."
cbmapopenex.restype = c_void_p
cbmapopenex.argtypes = [c_int]
