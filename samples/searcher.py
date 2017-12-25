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
    if not db.open("casket", Database.DBREADER):
        print("error: %s" % db.err_msg(db.error()), file=sys.stderr)
        sys.exit(1)
    
    # create a search condition object
    cond = Condition()
    
    # set the search phrase to the search condition object
    cond.set_phrase("rainbow AND lullaby")
    
    # get the result of search
    result = db.search(cond)
    
    # for each document in the result
    dnum = result.doc_num()
    for i in range(dnum):
        # retrieve the document object
        doc = db.get_doc(result.get_doc_id(i), 0)
        if doc:
            # display attributes
            uri = doc.attr("@uri")
            if uri:
                print("URI: %s" % uri)
            title = doc.attr("@title")
            if title:
                print("Title: %s" % title)
            # display the body text
            for text in doc.texts():
                print("%s" % text)
    
    # close the database
    if not db.close():
        print("error: %s" % db.err_msg(db.error()))
    sys.exit(0)
