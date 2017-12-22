#! /usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from ctypes import CDLL, byref, c_int, c_void_p
import sys

from estraier import *
from cabin import *

if __name__=="__main__":
    libc = CDLL("libc.so")
    free = libc.free
    free.restype = None
    free.argtypes = [c_void_p]

    ecode = c_int()
    resnum = c_int()
    
    # open the database
    db = est_db_open("casket", ESTDBREADER, byref(ecode))
    if not db:
        print("error: %s" % est_err_msg(ecode), file=sys.stderr)
        sys.exit(1)
    
    # create a search condition object
    cond = est_cond_new()
    
    # set the search phrase to the search condition object
    est_cond_set_phrase(cond, "rainbow AND lullaby")
    
    # get the result of search
    result = est_db_search(db, cond, byref(resnum), None)
    
    # for each document in the result
    for i in range(resnum.value):
        
        # retrieve the document object
        doc = est_db_get_doc(db, result[i], 0)
        if not doc:
            continue
        
        # display attributes
        value = est_doc_attr(doc, "@uri")
        if value:
            print("URI: %s" % value)
        value = est_doc_attr(doc, "@title")
        if value:
            print("Title: %s" % value)
        
        # display the body text
        texts = est_doc_texts(doc)
        for j in range(cblistnum(texts)):
            value = cblistval(texts, j, None)
            print("%s" % value)
        
        # destroy the document object
        est_doc_delete(doc)
    
    # free the result of search
    free(result)
    
    # destroy the search condition object
    est_cond_delete(cond)
    
    # close the database
    rv = est_db_close(db, byref(ecode))
    if not rv:
        print("error: %s" % est_err_msg(ecode), file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)

