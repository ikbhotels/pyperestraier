#! /usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import sys

from estraier_c import Document, Condition, Result, Database

if __name__=="__main__":
    # create the database object
    db = Database()
    
    # open the database
    if not db.open("casket", Database.DBWRITER | Database.DBCREAT):
        print("error: %s" % db.err_msg(db.error()), file=sys.stderr)
        sys.exit(1)
    
    # create a document object
    doc = Document()
    
    # add attributes to the document object
    doc.add_attr("@uri", "http://estraier.gov/example.txt")
    doc.add_attr("@title", "Over the Rainbow")
    
    # add the body text to the document object
    doc.add_text("Somewhere over the rainbow.  Way up high.")
    doc.add_text("There's a land that I heard of once in a lullaby.")
    
    # register the document object to the database
    if not db.put_doc(doc, Database.PDCLEAN):
        print("error: %s" % db.err_msg(db.error()), file=sys.stderr)
    
    # close the database
    if not db.close():
        print("error: %s" % db.err_msg(db.error()), file=sys.stderr)
