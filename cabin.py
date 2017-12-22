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

from ctypes import CDLL, POINTER, c_int, c_double, c_char_p, c_void_p, c_size_t

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
