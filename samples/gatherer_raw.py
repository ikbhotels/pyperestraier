#! /usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from ctypes import byref, c_int
import sys

from estraier_raw import *

if __name__=="__main__":
    ecode = c_int()
    
    # open the database
    db = est_db_open("casket", ESTDBWRITER | ESTDBCREAT, byref(ecode))
    if not db:
        print("error: %s" % est_err_msg(ecode), file=sys.stderr)
        sys.exit(1)
    
    # create a document object
    doc = est_doc_new()
    
    # add attributes to the document object
    est_doc_add_attr(doc, "@uri", "http://estraier.gov/example.txt")
    est_doc_add_attr(doc, "@title", "Over the Rainbow")
    
    # add the body text to the document object
    est_doc_add_text(doc, "Somewhere over the rainbow.  Way up high.")
    est_doc_add_text(doc, "There's a land that I heard of once in a lullaby.")
    
    # register the document object to the database
    rv = est_db_put_doc(db, doc, ESTPDCLEAN)
    if not rv:
        print("error: %s" % est_err_msg(est_db_error(db)), file=sys.stderr)
    
    # destroy the document object
    est_doc_delete(doc)
    
    # close the database
    rv = est_db_close(db, byref(ecode))
    if not rv:
        print("error: %s" % est_err_msg(ecode), file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
