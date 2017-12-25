#! /usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import codecs
import re

from estraier_c import Document, Condition, Result, Database

def removetags(str):
    rv = ""
    intag = False
    for i in range(len(str)):
        if str[i] == "<":
            intag = True
        if not intag:
            rv += str[i]
        if str[i] == ">":
            intag = False
    return rv

enttab = {
    "quot": u"\u0022",
    "lt"  : u"\u003c",
    "gt"  : u"\u003e",
    "copy": u"\u00a9",
}

def deentref(str):
    rv = ""
    ent = ""
    inent = False
    for i in range(len(str)):
        if inent:
            if str[i] == ";":
                inent = False
                if ent in enttab:
                    rv += enttab[ent]
                elif ent[0] == "#":
                    rv += ("\\U%08x" % int(ent[1:])).decode("unicode-escape")
                else:
                    rv += ("&" + ent + ";")
            else:
                ent += str[i]
        else:
            if str[i] == "&":
                inent = True
                ent = ""
            else:
                rv += str[i]
    return rv

class DatLine:
    line = None
    author = None
    mail = None
    timestamp = None
    id = None
    body = None
    formedbody = []
    title = None
    rets = re.compile(r"(?P<date>..../../..)(\(.*\))? *(?P<time>..:..(:..)?)")

    def __init__(self, line):
        self.line = line
        a = line.split(u"<>")
        if len(a) > 0:
            self.author = a[0]
        if len(a) > 1:
            self.mail = a[1]
        if len(a) > 2:
            a2 = a[2].split(u" ID:")
            if len(a2) > 1:
                self.id = a2[1]
            ts = a2[0]
            if len(ts) > 2 and ts[2] == "/":
                if ts[0] < u"5":
                    ts = u"20" + ts
                else:
                    ts = u"19" + ts
            m = self.rets.search(ts)
            if m:
                self.timestamp = m.group("date") + " " + m.group("time")
        if len(a) > 3:
            self.body = a[3]
            formedbody = a[3].split(u"<br>")
            for i in range(len(formedbody)):
                formedbody[i] = removetags(formedbody[i])
                formedbody[i] = deentref(formedbody[i])
            self.formedbody = formedbody
        if len(a) > 4:
            self.title = deentref(a[4])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage datgatherer casket urlfile datdir\n")
        sys.exit(1)
    (casket, urlfilename, datdir) = sys.argv[1:]
    redatpath = re.compile(r"^.*/(?P<file>[^/]+)/$")
    db = Database()
    if not db.open(casket, Database.DBWRITER | Database.DBCREAT):
        print("db open", file=sys.stderr)
        sys.exit(1)
    with open(urlfilename, "r") as furl:
        for line in furl:
            url = line.strip()
            m = redatpath.match(line)
            if m is not None:
                datpath = "{datdir}/{datfile}.dat".format(
                    datdir=datdir, datfile=m.group("file"))
                try:
                    with open(datpath, "r") as fdat:
                        i = 1
                        for datline_raw in fdat:
                            try:
                                datline = codecs.decode(datline_raw, "MS932")
                                d = DatLine(datline)
                                doc = Document()
                                if i == 1:
                                    title = d.title
                                doc.add_attr("@uri", "%s%d" % (url, i))
                                doc.add_attr("@type", "text/html")
                                doc.add_attr("@title", u"%s | Res %d" % (title, i))
                                if d.author:
                                    doc.add_attr("@author", d.author)
                                #doc.add_attr("@size", d.bodysize)
                                if d.timestamp:
                                    doc.add_attr("@cdate", d.timestamp)
                                    doc.add_attr("@mdate", d.timestamp)
                                #if d.body:
                                #    doc.add_text(d.body)
                                if d.formedbody:
                                    for fb in d.formedbody:
                                        doc.add_text(fb)
                                db.put_doc(doc, Database.PDCLEAN)
                            except ValueError as e:
                                print(e, file=sys.stderr)
                            i += 1
                except IOError as e:
                    print(e, file=sys.stderr)
    db.close()
