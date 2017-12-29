################################################################################################
# The core API of Hyper Estraier
#                                                      Copyright (C) 2004-2007 Mikio Hirabayashi
# This file is part of Hyper Estraier.
# Hyper Estraier is free software; you can redistribute it and/or modify it under the terms of
# the GNU Lesser General Public License as published by the Free Software Foundation; either
# version 2.1 of the License or any later version.  Hyper Estraier is distributed in the hope
# that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
# You should have received a copy of the GNU Lesser General Public License along with Hyper
# Estraier; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA 02111-1307 USA.
################################################################################################

from ctypes import CDLL, POINTER
from ctypes import c_int, c_long, c_ulong, c_double, c_size_t
from ctypes import c_char_p, c_void_p

libest_raw = CDLL("libestraier.so")

############################################################
# API for document
############################################################

ESTDATTRID     = "@id"             # name of the attribute of the ID number
ESTDATTRURI    = "@uri"            # name of the attribute of the URI
ESTDATTRDIGEST = "@digest"         # name of the attribute of message digest
ESTDATTRCDATE  = "@cdate"          # name of the attribute of creation date
ESTDATTRMDATE  = "@mdate"          # name of the attribute of modification date
ESTDATTRADATE  = "@adate"          # name of the attribute of access date
ESTDATTRTITLE  = "@title"          # name of the attribute of title
ESTDATTRAUTHOR = "@author"         # name of the attribute of author
ESTDATTRTYPE   = "@type"           # name of the attribute of content type
ESTDATTRLANG   = "@lang"           # name of the attribute of language
ESTDATTRGENRE  = "@genre"          # name of the attribute of genre
ESTDATTRSIZE   = "@size"           # name of the attribute of entity size
ESTDATTRWEIGHT = "@weight"         # name of the attribute of scoring weight
ESTDATTRMISC   = "@misc"           # name of the attribute of miscellaneous information
ESTDCNTLVECTOR = "%VECTOR"         # name of the control code for keyword vector
ESTDCNTLSCORE  = "%SCORE"          # name of the control code for substitute score
ESTDCNTLSHADOW = "%SHADOW"         # name of the control code for shadow document

# ESTDOC *est_doc_new(void);
est_doc_new = libest_raw.est_doc_new
est_doc_new.__doc__ = \
    "Create a document object.\n"\
    "The return value is an object of a document."
est_doc_new.restype = c_void_p
est_doc_new.argtypes = []

# ESTDOC *est_doc_new_from_draft(const char *draft);
est_doc_new_from_draft = libest_raw.est_doc_new_from_draft
est_doc_new_from_draft.__doc__ = \
    "Create a document object made from draft data.\n"\
    "`draft' specifies a string of draft data.\n"\
    "The return value is an object of a document."
est_doc_new_from_draft.restype = c_void_p
est_doc_new_from_draft.argtypes = [c_char_p]

# void est_doc_delete(ESTDOC *doc);
est_doc_delete = libest_raw.est_doc_delete
est_doc_delete.__doc__ = \
    "Destroy a document object.\n"\
    "`doc' specifies a document object."
est_doc_delete.restype = None
est_doc_delete.argtypes = [c_void_p]

# void est_doc_add_attr(ESTDOC *doc, const char *name, const char *value);
est_doc_add_attr = libest_raw.est_doc_add_attr
est_doc_add_attr.__doc__ = \
    "Add an attribute to a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`name' specifies the name of an attribute.\n"\
    "`value' specifies the value of the attribute.  If it is `NULL', the attribute is removed.\n"
est_doc_add_attr.restype = None
est_doc_add_attr.argtypes = [c_void_p, c_char_p, c_char_p]

# void est_doc_add_text(ESTDOC *doc, const char *text);
est_doc_add_text = libest_raw.est_doc_add_text
est_doc_add_text.__doc__ = \
    "Add a sentence of text to a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`text' specifies a sentence of text."
est_doc_add_text.restype = None
est_doc_add_text.argtypes = [c_void_p, c_char_p]

# void est_doc_add_hidden_text(ESTDOC *doc, const char *text);
est_doc_add_hidden_text = libest_raw.est_doc_add_hidden_text
est_doc_add_hidden_text.__doc__ = \
    "Add a hidden sentence to a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`text' specifies a hidden sentence."
est_doc_add_hidden_text.restype = None
est_doc_add_hidden_text.argtypes = [c_void_p, c_char_p]

# void est_doc_set_keywords(ESTDOC *doc, CBMAP *kwords);
est_doc_set_keywords = libest_raw.est_doc_set_keywords
est_doc_set_keywords.__doc__ = \
    "Attach keywords to a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`kwords' specifies a map object of keywords.  Keys of the map should be keywords of the\n"\
    "document and values should be their scores in decimal string.  The map object is copied\n"\
    "internally."
est_doc_set_keywords.restype = None
est_doc_set_keywords.argtypes = [c_void_p, c_void_p]

# void est_doc_set_score(ESTDOC *doc, int score);
est_doc_set_score = libest_raw.est_doc_set_score
est_doc_set_score.__doc__ = \
    "Set the substitute score of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`score' specifies the substitute score.  It it is negative, the substitute score setting is\n"\
    "nullified."
est_doc_set_score.restype = None
est_doc_set_score.argtypes = [c_void_p, c_int]

# int est_doc_id(ESTDOC *doc);
est_doc_id = libest_raw.est_doc_id
est_doc_id.__doc__ = \
    "Get the ID number of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is the ID number of the document object.  If the object has not been\n"\
    "registered, -1 is returned."
est_doc_id.restype = c_int
est_doc_id.argtypes = [c_void_p]

# CBLIST *est_doc_attr_names(ESTDOC *doc);
est_doc_attr_names = libest_raw.est_doc_attr_names
est_doc_attr_names.__doc__ =\
    "Get a list of attribute names of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is a new list object of attribute names of the document object.  Because\n"\
    "the object of the return value is opened with the function `cblistopen', it should be closed\n"\
    "with the function `cblistclose' if it is no longer in use."
est_doc_attr_names.restype = c_void_p
est_doc_attr_names.argtypes = [c_void_p]

# const char *est_doc_attr(ESTDOC *doc, const char *name);
est_doc_attr = libest_raw.est_doc_attr
est_doc_attr.__doc__ = \
    "Get the value of an attribute of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`name' specifies the name of an attribute.\n"\
    "The return value is the value of the attribute or `NULL' if it does not exist.  The life\n"\
    "duration of the returned string is synchronous with the one of the document object."
est_doc_attr.restype = c_char_p
est_doc_attr.argtypes = [c_void_p, c_char_p]

# const CBLIST *est_doc_texts(ESTDOC *doc);
est_doc_texts = libest_raw.est_doc_texts
est_doc_texts.__doc__ = \
    "Get a list of sentences of the text of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is a list object of sentences of the text of the document object.  The life\n"\
    "duration of the returned object is synchronous with the one of the document object."
est_doc_texts.restype = c_void_p
est_doc_texts.argtypes = [c_void_p]

# char *est_doc_cat_texts(ESTDOC *doc);
est_doc_cat_texts = libest_raw.est_doc_cat_texts
est_doc_cat_texts.__doc__ = \
    "Concatenate sentences of the text of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is concatenated sentences of the document object.  Because the region of the\n"\
    "return value is allocated with the `malloc' call, it should be released with the `free' call\n"\
    "if it is no longer in use."
est_doc_cat_texts.restype = c_char_p
est_doc_cat_texts.argtypes = [c_void_p]

# CBMAP *est_doc_keywords(ESTDOC *doc);
est_doc_keywords = libest_raw.est_doc_keywords
est_doc_keywords.__doc__ = \
    "Get attached keywords of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is a map object of keywords and their scores in decimal string.  If no\n"\
    "keyword is attached, `NULL' is returned.  The life duration of the returned object is\n"\
    "synchronous with the one of the document object."
est_doc_keywords.restype = c_void_p
est_doc_keywords.argtypes = [c_void_p]

# int est_doc_score(ESTDOC *doc);
est_doc_score = libest_raw.est_doc_score
est_doc_score.__doc__ = \
    "Get the substitute score of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is the substitute score or -1 if it is not set."
est_doc_score.restype = c_int
est_doc_score.argtypes = [c_void_p]

# char *est_doc_dump_draft(ESTDOC *doc);
est_doc_dump_draft = libest_raw.est_doc_dump_draft
est_doc_dump_draft.__doc__ = \
    "Dump draft data of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is draft data of the document object.  Because the region of the return value\n"\
    "is allocated with the `malloc' call, it should be released with the `free' call if it is no\n"\
    "longer in use."
est_doc_dump_draft.restype = c_char_p
est_doc_dump_draft.argtypes = [c_void_p]

# char *est_doc_make_snippet(ESTDOC *doc, const CBLIST *words, int wwidth, int hwidth, int awidth);
est_doc_make_snippet = libest_raw.est_doc_make_snippet
est_doc_make_snippet.__doc__ = \
    "Make a snippet of the body text of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`word' specifies a list object of words to be highlight.\n"\
    "`wwidth' specifies whole width of the result.\n"\
    "`hwidth' specifies width of strings picked up from the beginning of the text.\n"\
    "`awidth' specifies width of strings picked up around each highlighted word.\n"\
    "The return value is a snippet string of the body text of the document object.  There are tab\n"\
    "separated values.  Each line is a string to be shown.  Though most lines have only one field,\n"\
    "some lines have two fields.  If the second field exists, the first field is to be shown with\n"\
    "highlighted, and the second field means its normalized form.  Because the region of the\n"\
    "return value is allocated with the `malloc' call, it should be released with the `free' call\n"\
    "if it is no longer in use."
est_doc_make_snippet.restype = c_char_p
est_doc_make_snippet.argtypes = [c_void_p, c_void_p, c_int, c_int, c_int]

############################################################
# API for search conditions
############################################################

ESTOPUVSET     = "[UVSET]"         # universal set
ESTOPID        = "[ID]"            # ID matching search
ESTOPURI       = "[URI]"           # URI matching search
ESTOPSIMILAR   = "[SIMILAR]"       # similarity search
ESTOPRANK      = "[RANK]"          # ranking search

ESTOPUNION     = "OR"              # union (conjunction)
ESTOPISECT     = "AND"             # intersection (disjunction)
ESTOPDIFF      = "ANDNOT"          # difference (intersection with negation)
ESTOPWCBW      = "[BW]"            # wild card for words beginning with a string
ESTOPWCEW      = "[EW]"            # wild card for words ending with a string
ESTOPWCRX      = "[RX]"            # wild card for words matching regular expressions
ESTOPWITH      = "WITH"            # delimiter for elements

ESTOPSTREQ     = "STREQ"           # string is equal
ESTOPSTRNE     = "STRNE"           # string is not equal
ESTOPSTRINC    = "STRINC"          # string is included in
ESTOPSTRBW     = "STRBW"           # string begins with
ESTOPSTREW     = "STREW"           # string ends with
ESTOPSTRAND    = "STRAND"          # string includes all tokens in
ESTOPSTROR     = "STROR"           # string includes at least one token in
ESTOPSTROREQ   = "STROREQ"         # string is equal at least one token in
ESTOPSTRRX     = "STRRX"           # string matches regular expressions of
ESTOPNUMEQ     = "NUMEQ"           # number or date is equal
ESTOPNUMNE     = "NUMNE"           # number or date is not equal
ESTOPNUMGT     = "NUMGT"           # number or date is greater than
ESTOPNUMGE     = "NUMGE"           # number or date is greater than or equal to
ESTOPNUMLT     = "NUMLT"           # number or date is less than
ESTOPNUMLE     = "NUMLE"           # number or date is less than or equal to
ESTOPNUMBT     = "NUMBT"           # number or date is between two tokens of

ESTORDIDA      = "[IDA]"           # ID numbers in ascending order
ESTORDIDD      = "[IDD]"           # ID numbers in descending order
ESTORDSCA      = "[SCA]"           # scores in ascending order
ESTORDSCD      = "[SCD]"           # scores in descending order
ESTORDSTRA     = "STRA"            # strings in ascending order
ESTORDSTRD     = "STRD"            # strings in descending order
ESTORDNUMA     = "NUMA"            # numbers in ascending order
ESTORDNUMD     = "NUMD"            # numbers in descending order

ESTECLSIMURL   = 10.0              # eclipse considering similarity and URL
ESTECLSERV     = 100.0             # eclipse on server basis
ESTECLDIR      = 101.0             # eclipse on directory basis
ESTECLFILE     = 102.0             # eclipse on file basis

# enumeration for options
ESTCONDSURE = 1 << 0               # check every N-gram key
ESTCONDUSUAL = 1 << 1              # check N-gram keys skipping by one
ESTCONDFAST = 1 << 2               # check N-gram keys skipping by two
ESTCONDAGITO = 1 << 3              # check N-gram keys skipping by three
ESTCONDNOIDF = 1 << 4              # without TF-IDF tuning
ESTCONDSIMPLE = 1 << 10            # with the simplified phrase
ESTCONDROUGH = 1 << 11             # with the rough phrase
ESTCONDUNION = 1 << 15             # with the union phrase
ESTCONDISECT = 1 << 16             # with the intersection phrase
ESTCONDSCFB = 1 << 30              # feed back scores (for debug)

# ESTCOND *est_cond_new(void);
est_cond_new = libest_raw.est_cond_new
est_cond_new.__doc__ = \
    "Create a condition object.\n"\
    "The return value is an object of search conditions."
est_cond_new.restype = c_void_p
est_cond_new.argtypes = []

# void est_cond_delete(ESTCOND *cond);
est_cond_delete = libest_raw.est_cond_delete
est_cond_delete.__doc__ = \
    "Destroy a condition object.\n"\
    "`cond' specifies a condition object."
est_cond_delete.restype = None
est_cond_delete.argtypes = [c_void_p]

# void est_cond_set_phrase(ESTCOND *cond, const char *phrase);
est_cond_set_phrase = libest_raw.est_cond_set_phrase
est_cond_set_phrase.__doc__ = \
    "Set the search phrase to a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`phrase' specifies a search phrase."
est_cond_set_phrase.restype = None
est_cond_set_phrase.argtypes = [c_void_p, c_char_p]

# void est_cond_add_attr(ESTCOND *cond, const char *expr);
est_cond_add_attr = libest_raw.est_cond_add_attr
est_cond_add_attr.__doc__ = \
    "Add an expression for an attribute to a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`expr' specifies an expression for an attribute."
est_cond_add_attr.restype = None
est_cond_add_attr.argtypes = [c_void_p, c_char_p]

# void est_cond_set_order(ESTCOND *cond, const char *expr);
est_cond_set_order = libest_raw.est_cond_set_order
est_cond_set_order.__doc__ = \
    "Set the order of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`expr' specifies an expression for the order.  By default, the order is by score descending."
est_cond_set_order.restype = None
est_cond_set_order.argtypes = [c_void_p, c_char_p]

# void est_cond_set_max(ESTCOND *cond, int max);
est_cond_set_max = libest_raw.est_cond_set_max
est_cond_set_max.__doc__ = \
    "Set the maximum number of retrieval of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`max' specifies the maximum number of retrieval.  By default, the number of retrieval is not\n"\
    "limited."
est_cond_set_max.restype = None
est_cond_set_max.argtypes = [c_void_p, c_int]

# void est_cond_set_skip(ESTCOND *cond, int skip);
est_cond_set_skip = libest_raw.est_cond_set_skip
est_cond_set_skip.__doc__ = \
    "Set the number of skipped documents of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`skip' specifies the number of documents to be skipped in the search result."
est_cond_set_skip.restype = None
est_cond_set_skip.argtypes = [c_void_p, c_int]

# void est_cond_set_options(ESTCOND *cond, int options);
est_cond_set_options = libest_raw.est_cond_set_options
est_cond_set_options.__doc__ = \
    "Set options of retrieval of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`options' specifies options: `ESTCONDSURE' specifies that it checks every N-gram key,\n"\
    "`ESTCONDUSUAL', which is the default, specifies that it checks N-gram keys with skipping one\n"\
    "key, `ESTCONDFAST' skips two keys, `ESTCONDAGITO' skips three keys, `ESTCONDNOIDF' specifies\n"\
    "not to perform TF-IDF tuning, `ESTCONDSIMPLE' specifies to use simplified phrase,\n"\
    "`ESTCONDROUGH' specifies to use rough phrase, `ESTCONDUNION' specifies to use union phrase,\n"\
    "`ESTCONDISECT' specifies to use intersection phrase, `ESTCONDSCFB' specifies to feed back\n"\
    "scores (only for debugging).  Each option can be specified at the same time by bitwise or.  If\n"\
    "keys are skipped, though search speed is improved, the relevance ratio grows less."
est_cond_set_options.restype = None
est_cond_set_options.argtypes = [c_void_p, c_int]

# void est_cond_set_auxiliary(ESTCOND *cond, int min);
est_cond_set_auxiliary = libest_raw.est_cond_set_auxiliary
est_cond_set_auxiliary.__doc__ = \
    "Set permission to adopt result of the auxiliary index.\n"\
    "`cond' specifies a condition object.\n"\
    "`min' specifies the minimum hits to adopt result of the auxiliary index.  If it is not more\n"\
    "than 0, the auxiliary index is not used.  By default, it is 32."
est_cond_set_auxiliary.restype = None
est_cond_set_auxiliary.argtypes = [c_void_p, c_int]

# void est_cond_set_eclipse(ESTCOND *cond, double limit);
est_cond_set_eclipse = libest_raw.est_cond_set_eclipse
est_cond_set_eclipse.__doc__ = \
    "Set the lower limit of similarity eclipse.\n"\
    "`cond' specifies a condition object.\n"\
    "`limit' specifies the lower limit of similarity for documents to be eclipsed.  Similarity is\n"\
    "between 0.0 and 1.0.  If the limit is added by `ESTECLSIMURL', similarity is weighted by URL.\n"\
    "If the limit is `ESTECLSERV', similarity is ignored and documents in the same server are\n"\
    "eclipsed.  If the limit is `ESTECLDIR', similarity is ignored and documents in the same\n"\
    "directory are eclipsed.  If the limit is `ESTECLFILE', similarity is ignored and documents of\n"\
    "the same file are eclipsed."
est_cond_set_eclipse.restype = None
est_cond_set_eclipse.argtypes = [c_void_p, c_double]

# void est_cond_set_distinct(ESTCOND *cond, const char *name);
est_cond_set_distinct = libest_raw.est_cond_set_distinct
est_cond_set_distinct.__doc__ = \
    "Set the attribute distinction filter.\n"\
    "`cond' specifies a condition object.\n"\
    "`name' specifies the name of an attribute to be distinct.\n"\
    "If this filter is set, candidates which have same value of the attribute is omitted."
est_cond_set_distinct.restype = None
est_cond_set_distinct.argtypes = [c_void_p, c_char_p]

# void est_cond_set_mask(ESTCOND *cond, int mask);
est_cond_set_mask = libest_raw.est_cond_set_mask
est_cond_set_mask.__doc__ = \
    "Set the mask of targets of meta search.\n"\
    "`cond' specifies a condition object.\n"\
    "`mask' specifies a masking number.  1 means the first target, 2 means the second target, 4\n"\
    "means the third target, and power values of 2 and their summation compose the mask."
est_cond_set_mask.restype = None
est_cond_set_mask.argtypes = [c_void_p, c_int]

############################################################
# API for database
############################################################

ESTIDXDMAX     = 256               # max number of the inverted index */
ESTIDXDSTD     = 16                # standard number of the inverted index */
ESTPDOCIDMIN   = 2000000001        # minimum ID number of pseudo documents */

( # enumeration for error codes
  ESTENOERR,                       # no error
  ESTEINVAL,                       # invalid argument
  ESTEACCES,                       # access forbidden
  ESTELOCK,                        # lock failure
  ESTEDB,                          # database problem
  ESTEIO,                          # I/O problem
  ESTENOITEM,                      # no item
) = range(7)
ESTEMISC = 9999                    # miscellaneous

# enumeration for open modes
ESTDBREADER = 1 << 0               # open as a reader
ESTDBWRITER = 1 << 1               # open as a writer
ESTDBCREAT = 1 << 2                # a writer creating
ESTDBTRUNC = 1 << 3                # a writer truncating
ESTDBNOLCK = 1 << 4                # open without locking
ESTDBLCKNB = 1 << 5                # lock without blocking
ESTDBPERFNG = 1 << 10              # use perfect N-gram analyzer
ESTDBCHRCAT = 1 << 11              # use character category analyzer
ESTDBSMALL = 1 << 20               # small tuning
ESTDBLARGE = 1 << 21               # large tuning
ESTDBHUGE = 1 << 22                # huge tuning
ESTDBHUGE2 = 1 << 23               # huge tuning second
ESTDBHUGE3 = 1 << 24               # huge tuning third
ESTDBSCVOID = 1 << 25              # store scores as void
ESTDBSCINT = 1 << 26               # store scores as integer
ESTDBSCASIS = 1 << 27              # refrain from adjustment of scores

( # enumeration for data types of attribute index
  ESTIDXATTRSEQ,                   # for multipurpose sequencial access method
  ESTIDXATTRSTR,                   # for narrowing with attributes as strings
  ESTIDXATTRNUM,                   # for narrowing with attributes as numbers
) = range(3)

# enumeration for options of optimization */
ESTOPTNOPURGE = 1 << 0             # omit purging dispensable region of deleted
ESTOPTNODBOPT = 1 << 1             # omit optimization of the database files

# enumeration for options of document merger
ESTMGCLEAN = 1 << 0                # clean up dispensable regions

# enumeration for options of document registration
ESTPDCLEAN = 1 << 0                # clean up dispensable regions
ESTPDWEIGHT = 1 << 1               # weight scores statically when indexing

# enumeration for options of document deletion
ESTODCLEAN = 1 << 0                # clean up dispensable regions

# enumeration for options of document retrieval
ESTGDNOATTR = 1 << 0               # no attributes
ESTGDNOTEXT = 1 << 1               # no text
ESTGDNOKWD = 1 << 2                # no keywords

# const char *est_err_msg(int ecode);
est_err_msg = libest_raw.est_err_msg
est_err_msg.__doc__ = \
    "Get the string of an error code.\n"\
    "`ecode' specifies an error code.\n"\
    "The return value is the string of the error code."
est_err_msg.restype = c_char_p
est_err_msg.argtypes = [c_int]

# ESTDB *est_db_open(const char *name, int omode, int *ecp);
est_db_open = libest_raw.est_db_open
est_db_open.__doc__ = \
    "Open a database.\n"\
    "`name' specifies the name of a database directory.\n"\
    "`omode' specifies open modes: `ESTDBWRITER' as a writer, `ESTDBREADER' as a reader.  If the\n"\
    "mode is `ESTDBWRITER', the following may be added by bitwise or: `ESTDBCREAT', which means it\n"\
    "creates a new database if not exist, `ESTDBTRUNC', which means it creates a new database\n"\
    "regardless if one exists.  Both of `ESTDBREADER' and  `ESTDBWRITER' can be added to by\n"\
    "bitwise or: `ESTDBNOLCK', which means it opens a database file without file locking, or\n"\
    "`ESTDBLCKNB', which means locking is performed without blocking.  If `ESTDBNOLCK' is used,\n"\
    "the application is responsible for exclusion control.  `ESTDBCREAT' can be added to by bitwise\n"\
    "or: `ESTDBPERFNG', which means N-gram analysis is performed against European text also,\n"\
    "`ESTDBCHRCAT', which means character category analysis is performed instead of N-gram analysis,\n"\
    "`ESTDBSMALL', which means the index is tuned to register less than 50000 documents,\n"\
    "`ESTDBLARGE', which means the index is tuned to register more than 300000 documents,\n"\
    "`ESTDBHUGE', which means the index is tuned to register more than 1000000 documents,\n"\
    "`ESTDBHUGE2', which means the index is tuned to register more than 5000000 documents,\n"\
    "`ESTDBHUGE3', which means the index is tuned to register more than 10000000 documents,\n"\
    "`ESTDBSCVOID', which means scores are stored as void, `ESTDBSCINT', which means scores are\n"\
    "stored as 32-bit integer, `ESTDBSCASIS', which means scores are stored as-is and marked not\n"\
    "to be tuned when search.\n"\
    "`ecp' specifies the pointer to a variable to which the error code is assigned.\n"\
    "The return value is a database object of the database or `NULL' if failure."
est_db_open.restype = c_void_p
est_db_open.argtypes = [c_char_p, c_int, POINTER(c_int)]

# int est_db_close(ESTDB *db, int *ecp);
est_db_close = libest_raw.est_db_close
est_db_close.__doc__ = \
    "Close a database.\n"\
    "`db' specifies a database object.\n"\
    "`ecp' specifies the pointer to a variable to which the error code is assigned.\n"\
    "The return value is true if success, else it is false."
est_db_close.restype = c_int
est_db_close.argtypes = [c_void_p, POINTER(c_int)]

# int est_db_error(ESTDB *db);
est_db_error = libest_raw.est_db_error
est_db_error.__doc__ = \
    "Get the last happened error code of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the last happened error code of the database."
est_db_error.restype = c_int
est_db_error.argtypes = [c_void_p]

# int est_db_fatal(ESTDB *db);
est_db_fatal = libest_raw.est_db_fatal
est_db_fatal.__doc__ = \
    "Check whether a database has a fatal error.\n"\
    "`db' specifies a database object.\n"\
    "The return value is true if the database has fatal erroor, else it is false."
est_db_fatal.restype = c_int
est_db_fatal.argtypes = [c_void_p]

# int est_db_add_attr_index(ESTDB *db, const char *name, int type);
est_db_add_attr_index = libest_raw.est_db_add_attr_index
est_db_add_attr_index.__doc__ = \
    "Add an index for narrowing or sorting with document attributes.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`name' specifies the name of an attribute.\n"\
    "`type' specifies the data type of attribute index; `ESTIDXATTRSEQ' for multipurpose sequencial\n"\
    "access method, `ESTIDXATTRSTR' for narrowing with attributes as strings, `ESTIDXATTRNUM' for\n"\
    "narrowing with attributes as numbers.\n"\
    "The return value is true if success, else it is false.\n"\
    "Note that this function should be called before the first document is registered."
est_db_add_attr_index.restype = c_int
est_db_add_attr_index.argtypes = [c_void_p, c_char_p, c_int]

# int est_db_flush(ESTDB *db, int max);
est_db_flush = libest_raw.est_db_flush
est_db_flush.__doc__ = \
    "Flush index words in the cache of a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`max' specifies the maximum number of words to be flushed.  If it not more than zero, all\n"\
    "words are flushed.\n"\
    "The return value is true if success, else it is false."
est_db_flush.restype = c_int
est_db_flush.argtypes = [c_void_p, c_int]

# int est_db_sync(ESTDB *db);
est_db_sync = libest_raw.est_db_sync
est_db_sync.__doc__ = \
    "Synchronize updating contents of a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "The return value is true if success, else it is false."
est_db_sync.restype = c_int
est_db_sync.argtypes = [c_void_p]

# int est_db_optimize(ESTDB *db, int options);
est_db_optimize = libest_raw.est_db_optimize
est_db_optimize.__doc__ = \
    "Optimize a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`options' specifies options: `ESTOPTNOPURGE' to omit purging dispensable region of deleted\n"\
    "documents, `ESTOPTNODBOPT' to omit optimization of the database files.  The two can be\n"\
    "specified at the same time by bitwise or.\n"\
    "The return value is true if success, else it is false."
est_db_optimize.restype = c_int
est_db_optimize.argtypes = [c_void_p, c_int]

# int est_db_merge(ESTDB *db, const char *name, int options);
est_db_merge = libest_raw.est_db_merge
est_db_merge.__doc__ = \
    "Merge another database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`name' specifies the name of another database directory.\n"\
    "`options' specifies options: `ESTMGCLEAN' to clean up dispensable regions of the deleted\n"\
    "document.\n"\
    "The return value is true if success, else it is false.\n"\
    "Creation options of the two databases should be same entirely.  ID numbers of imported\n"\
    "documents are changed within the sequence of the desitination database.  If URIs of imported\n"\
    "documents conflict ones of exsisting documents, existing documents are removed."
est_db_merge.restype = c_int
est_db_merge.argtypes = [c_void_p, c_char_p, c_int]

# int est_db_put_doc(ESTDB *db, ESTDOC *doc, int options);
est_db_put_doc = libest_raw.est_db_put_doc
est_db_put_doc.__doc__ = \
    "Add a document to a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`doc' specifies a document object.  The document object should have the URI attribute.\n"\
    "`options' specifies options: `ESTPDCLEAN' to clean up dispensable regions of the overwritten\n"\
    "document, `ESTPDWEIGHT' to weight scores statically with score weighting attribute.\n"\
    "The return value is true if success, else it is false.\n"\
    "If the URI attribute is same with an existing document in the database, the existing one is\n"\
    "deleted."
est_db_put_doc.restype = c_int
est_db_put_doc.argtypes = [c_void_p, c_void_p, c_int]

# int est_db_out_doc(ESTDB *db, int id, int options);
est_db_out_doc = libest_raw.est_db_out_doc
est_db_out_doc.__doc__ = \
    "Remove a document from a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`id' specifies the ID number of a registered document.\n"\
    "`options' specifies options: `ESTODCLEAN' to clean up dispensable regions of the deleted\n"\
    "document.\n"\
    "The return value is true if success, else it is false."
est_db_out_doc.restype = c_int
est_db_out_doc.argtypes = [c_void_p, c_int, c_int]

# int est_db_edit_doc(ESTDB *db, ESTDOC *doc);
est_db_edit_doc = libest_raw.est_db_edit_doc
est_db_edit_doc.__doc__ = \
    "Edit attributes of a document in a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is true if success, else it is false.\n"\
    "The ID can not be changed.  If the URI is changed and it overlaps the URI of another\n"\
    "registered document, this function fails."
est_db_edit_doc.restype = c_int
est_db_edit_doc.argtypes = [c_void_p, c_void_p]

# ESTDOC *est_db_get_doc(ESTDB *db, int id, int options);
est_db_get_doc = libest_raw.est_db_get_doc
est_db_get_doc.__doc__ = \
    "Retrieve a document in a database.\n"\
    "`db' specifies a database object.\n"\
    "`id' specifies the ID number of a registered document.\n"\
    "`options' specifies options: `ESTGDNOATTR' to ignore attributes, `ESTGDNOTEXT' to ignore\n"\
    "the body text, `ESTGDNOKWD' to ignore keywords.  The three can be specified at the same time\n"\
    "by bitwise or.\n"\
    "The return value is a document object.  It should be deleted with `est_doc_delete' if it is\n"\
    "no longer in use.  On error, `NULL' is returned."
est_db_get_doc.restype = c_void_p
est_db_get_doc.argtypes = [c_void_p, c_int, c_int]

# char *est_db_get_doc_attr(ESTDB *db, int id, const char *name);
est_db_get_doc_attr = libest_raw.est_db_get_doc_attr
est_db_get_doc_attr.__doc__ = \
    "Retrieve the value of an attribute of a document in a database.\n"\
    "`db' specifies a database object.\n"\
    "`id' specifies the ID number of a registered document.\n"\
    "`name' specifies the name of an attribute.\n"\
    "The return value is the value of the attribute or `NULL' if it does not exist.  Because the\n"\
    "region of the return value is allocated with the `malloc' call, it should be released with\n"\
    "the `free' call if it is no longer in use."
est_db_get_doc_attr.restype = c_char_p
est_db_get_doc_attr.argtypes = [c_void_p, c_int, c_char_p]

# int est_db_uri_to_id(ESTDB *db, const char *uri);
est_db_uri_to_id = libest_raw.est_db_uri_to_id
est_db_uri_to_id.__doc__ = \
    "Get the ID of a document specified by URI.\n"\
    "`db' specifies a database object.\n"\
    "`uri' specifies the URI of a registered document.\n"\
    "The return value is the ID of the document.  On error, -1 is returned."
est_db_uri_to_id.restype = c_int
est_db_uri_to_id.argtypes = [c_void_p, c_char_p]

# const char *est_db_name(ESTDB *db);
est_db_name = libest_raw.est_db_name
est_db_name.__doc__ = \
    "Get the name of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the name of the database.  The life duration of the returned string is\n"\
    "synchronous with the one of the database object."
est_db_name.restype = c_char_p
est_db_name.argtypes = [c_void_p]

# int est_db_doc_num(ESTDB *db);
est_db_doc_num = libest_raw.est_db_doc_num
est_db_doc_num.__doc__ = \
    "Get the number of documents in a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the number of documents in the database."
est_db_doc_num.restype = c_int
est_db_doc_num.argtypes = [c_void_p]

# int est_db_word_num(ESTDB *db);
est_db_word_num = libest_raw.est_db_word_num
est_db_word_num.__doc__ = \
    "Get the number of unique words in a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the number of unique words in the database."
est_db_word_num.restype = c_int
est_db_word_num.argtypes = [c_void_p]

# double est_db_size(ESTDB *db);
est_db_size = libest_raw.est_db_size
est_db_size.__doc__ = \
    "Get the size of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the size of the database."
est_db_size.restype = c_double
est_db_size.argtypes = [c_void_p]

# int *est_db_search(ESTDB *db, ESTCOND *cond, int *nump, CBMAP *hints);
est_db_search = libest_raw.est_db_search
est_db_search.__doc__ = \
    "Search a database for documents corresponding a condition.\n"\
    "`db' specifies a database object.\n"\
    "`cond' specifies a condition object.\n"\
    "`nump' specifies the pointer to a variable to which the number of elements in the result is\n"\
    "assigned.\n"\
    "`hints' specifies a map object into which the number of documents corresponding to each word\n"\
    "is stored.  If a word is in a negative condition, the number is negative.  The element whose\n"\
    "key is an empty string specifies the number of whole result.  If it is `NULL', it is not used.\n"\
    "The return value is an array whose elements are ID numbers of corresponding documents.\n"\
    "This function does never fail.  Even if no document corresponds or an error occurs, an empty\n"\
    "array is returned.  Because the region of the return value is allocated with the `malloc'\n"\
    "call, it should be released with the `free' call if it is no longer in use."
est_db_search.restype = POINTER(c_int)
est_db_search.argtypes = [c_void_p, c_void_p, POINTER(c_int), c_void_p]

# int *est_db_search_meta(ESTDB **dbs, int dbnum, ESTCOND *cond, int *nump, CBMAP *hints);
est_db_search_meta = libest_raw.est_db_search_meta
est_db_search_meta.__doc__ = \
    "Search plural databases for documents corresponding a condition.\n"\
    "`dbs' specifies an array whose elements are database objects.\n"\
    "`dbnum' specifies the number of elements of the array.\n"\
    "`cond' specifies a condition object.\n"\
    "`nump' specifies the pointer to a variable to which the number of elements in the result is\n"\
    "assigned.\n"\
    "`hints' specifies a map object into which the number of documents corresponding to each word\n"\
    "is stored.  If a word is in a negative condition, the number is negative.  The element whose\n"\
    "key is an empty string specifies the number of whole result.  If it is `NULL', it is not used.\n"\
    "The return value is an array whose elements are indexes of container databases and ID numbers\n"\
    "of in each database alternately.\n"\
    "This function does never fail.  Even if no document corresponds or an error occurs, an empty\n"\
    "array is returned.  Because the region of the return value is allocated with the `malloc'\n"\
    "call, it should be released with the `free' call if it is no longer in use."
est_db_search_meta.restype = POINTER(c_int)
est_db_search_meta.argtypes = [POINTER(c_void_p), c_int, c_void_p, POINTER(c_int), c_void_p]

# int est_db_scan_doc(ESTDB *db, ESTDOC *doc, ESTCOND *cond);
est_db_scan_doc = libest_raw.est_db_scan_doc
est_db_scan_doc.__doc__ = \
    "Check whether a document object matches the phrase of a search condition object definitely.\n"\
    "`db' specifies a database object.\n"\
    "`doc' specifies a document object.\n"\
    "`cond' specifies a search condition object.\n"\
    "The return value is true if the document matches the phrase of the condition object\n"\
    "definitely, else it is false."
est_db_scan_doc.restype = c_int
est_db_scan_doc.argtypes = [c_void_p, c_void_p, c_void_p]

# void est_db_set_cache_size(ESTDB *db, size_t size, int anum, int tnum, int rnum);
est_db_set_cache_size = libest_raw.est_db_set_cache_size
est_db_set_cache_size.__doc__ = \
    "Set the maximum size of the cache memory of a database.\n"\
    "`db' specifies a database object.\n"\
    "`size' specifies the maximum size of the index cache.  By default, it is 64MB.  If it is\n"\
    "negative, the current size is not changed.\n"\
    "`anum' specifies the maximum number of cached records for document attributes.  By default, it\n"\
    "is 8192.  If it is negative, the current size is not changed.\n"\
    "`tnum' specifies the maximum number of cached records for document texts.  By default, it is\n"\
    "1024.  If it is negative, the current size is not changed.\n"\
    "`rnum' specifies the maximum number of cached records for occurrence results.  By default, it\n"\
    "is 256.  If it is negative, the current size is not changed."
est_db_set_cache_size.restype = None
est_db_set_cache_size.argtypes = [c_void_p, c_size_t, c_int, c_int, c_int]

# int est_db_add_pseudo_index(ESTDB *db, const char *path);
est_db_add_pseudo_index = libest_raw.est_db_add_pseudo_index
est_db_add_pseudo_index.__doc__ = \
    "Add a pseudo index directory to a database.\n"\
    "`db' specifies a database object.\n"\
    "`path' specifies the path of a pseudo index directory.\n"\
    "The return value is true if success, else it is false."
est_db_add_pseudo_index.restype = c_int
est_db_add_pseudo_index.argtypes = [c_void_p, c_char_p]

############################################################
# features for experts
############################################################

_EST_VERSION   = "1.4.13"
_EST_LIBVER    = 838
_EST_PROTVER   = "1.0"

_EST_PROJURL   = "http://hyperestraier.sourceforge.net/"
_EST_XNSEARCH  = "http://hyperestraier.sourceforge.net/xmlns/search"
_EST_XNNODE    = "http://hyperestraier.sourceforge.net/xmlns/node"

( # enumeration for languages
    ESTLANGEN,                     # English
    ESTLANGJA,                     # Japanese
    ESTLANGZH,                     # Chinese
    ESTLANGKO,                     # Korean
    ESTLANGMISC,                   # miscellaneous
) = range(5)

# enumeration for document parts
ESTMDATTR = 1 << 0                 # attributes
ESTMDTEXT = 1 << 1                 # texts
ESTMDKWD = 1 << 2                  # keywords

# enumeration for database repair
ESTRPSTRICT = 1 << 0               # perform strict consistency check
ESTRPSHODDY = 1 << 1               # omit consistency check

( # enumeration for scoring for result map
    ESTRMLOSUM,                    # summation
    ESTRMLOMAX,                    # maximum
    ESTRMLOMIN,                    # minimum
    ESTRMLOAVG,                    # average
) = range(4)

# void est_break_text(const char *text, CBLIST *list, int norm, int tail);
est_break_text = libest_raw.est_break_text
est_break_text.__doc__ = \
    "Break a sentence of text and extract words.\n"\
    "`text' specifies a sentence of text.\n"\
    "`list' specifies a list object to which extract words are added.\n"\
    "`norm' specifies whether to normalize the text.\n"\
    "`tail' specifies whether to pick up oddness N-gram at the end."
est_break_text.restype = None
est_break_text.argtypes = [c_char_p, c_void_p, c_int, c_int]

# void est_break_text_perfng(const char *text, CBLIST *list, int norm, int tail);
est_break_text_perfng = libest_raw.est_break_text_perfng
est_break_text_perfng.__doc__ = \
    "Break a sentence of text and extract words using perfect N-gram analyzer.\n"\
    "`text' specifies a sentence of text.\n"\
    "`list' specifies a list object to which extract words are added.\n"\
    "`norm' specifies whether to normalize the text.\n"\
    "`tail' specifies whether to pick up oddness N-gram at the end."
est_break_text_perfng.restype = None
est_break_text_perfng.argtypes = [c_char_p, c_void_p, c_int, c_int]

# void est_break_text_chrcat(const char *text, CBLIST *list, int norm);
est_break_text_chrcat = libest_raw.est_break_text_chrcat
est_break_text_chrcat.__doc__ = \
    "Break a sentence of text and extract words, using character category analyzer.\n"\
    "`text' specifies a sentence of text.\n"\
    "`list' specifies a list object to which extract words are added.\n"\
    "`norm' specifies whether to normalize the text."
est_break_text_chrcat.restype = None
est_break_text_chrcat.argtypes = [c_char_p, c_void_p, c_int]

# char *est_str_make_snippet(const char *str, const CBLIST *words,
#                            int wwidth, int hwidth, int awidth);
est_str_make_snippet = libest_raw.est_str_make_snippet
est_str_make_snippet.__doc__ = \
    "Make a snippet of an arbitrary string.\n"\
    "`word' specifies a list object of words to be highlight.\n"\
    "`wwidth' specifies whole width of the result.\n"\
    "`hwidth' specifies width of strings picked up from the beginning of the text.\n"\
    "`awidth' specifies width of strings picked up around each highlighted word.\n"\
    "The return value is a snippet string of the string.  Because the region of the return value is\n"\
    "allocated with the `malloc' call, it should be released with the `free' call if it is no\n"\
    "longer in use."
est_str_make_snippet.restype = c_char_p
est_str_make_snippet.argtypes = [c_char_p, c_void_p, c_int, c_int, c_int]

# char *est_iconv(const char *ptr, int size, const char *icode, const char *ocode,
#                 int *sp, int *mp);
est_iconv = libest_raw.est_iconv
est_iconv.__doc__ = \
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
    "is no longer in use."
est_iconv.restype = c_char_p
est_iconv.argtypes = [c_char_p, c_int, c_char_p, c_char_p,
                      POINTER(c_int), POINTER(c_int)]

# const char *est_enc_name(const char *ptr, int size, int plang);
est_enc_name = libest_raw.est_enc_name
est_enc_name.__doc__ = \
    "Detect the encoding of a string automatically.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`plang' specifies a preferred language.  As for now, `ESTLANGEN', `ESTLANGJA', `ESTLANGZH',\n"\
    "and `ESTLANGKO' are supported.\n"\
    "The return value is the string of the encoding name of the string."
est_enc_name.restype = c_char_p
est_enc_name.argtypes = [c_char_p, c_int, c_int]

# char *est_uconv_in(const char *ptr, int size, int *sp);
est_uconv_in = libest_raw.est_uconv_in
est_uconv_in.__doc__ = \
    "Convert a UTF-8 string into UTF-16BE.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "The return value is the pointer to the result object.  Because an additional zero code is\n"\
    "appended at the end of the region of the return value, the return value can be treated as a\n"\
    "character string.  Because the region of the return value is allocated with the `malloc' call,\n"\
    "it should be released with the `free' call if it is no longer in use.\n"
est_uconv_in.restype = c_char_p
est_uconv_in.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *est_uconv_out(const char *ptr, int size, int *sp);
est_uconv_out = libest_raw.est_uconv_out
est_uconv_out.__doc__ = \
    "Convert a UTF-16BE string into UTF-8.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "The return value is the pointer to the result object.  Because an additional zero code is\n"\
    "appended at the end of the region of the return value, the return value can be treated as a\n"\
    "character string.  Because the region of the return value is allocated with the `malloc' call,\n"\
    "it should be released with the `free' call if it is no longer in use."
est_uconv_out.restype = c_char_p
est_uconv_out.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *est_deflate(const char *ptr, int size, int *sp, int mode);
est_deflate = libest_raw.est_deflate
est_deflate.__doc__ = \
    "Compress a serial object with ZLIB.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "`mode' specifies detail behavior.  0 specifies using the standard deflate encoding, -1\n"\
    "specifies the raw deflate encoding, and 1 specifies the GZIP encoding.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
est_deflate.restype = c_char_p
est_deflate.argtypes = [c_char_p, c_int, POINTER(c_int), c_int]

# char *est_inflate(const char *ptr, int size, int *sp, int mode);
est_inflate = libest_raw.est_inflate
est_inflate.__doc__ = \
    "Decompress a serial object compressed with ZLIB.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "`mode' specifies detail behavior.  0 specifies using the standard deflate encoding, -1\n"\
    "specifies the raw deflate encoding, and 1 specifies the GZIP encoding.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use."
est_inflate.restype = c_char_p
est_inflate.argtypes = [c_char_p, c_int, POINTER(c_int), c_int]

# char *est_lzoencode(const char *ptr, int size, int *sp);
est_lzoencode = libest_raw.est_lzoencode
est_lzoencode.__doc__ = \
    "Compress a serial object with LZO.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
est_lzoencode.restype = c_char_p
est_lzoencode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *est_lzodecode(const char *ptr, int size, int *sp);
est_lzodecode = libest_raw.est_lzodecode
est_lzodecode.__doc__ = \
    "Decompress a serial object compressed with LZO.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use."
est_lzodecode.restype = c_char_p
est_lzodecode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *est_bzencode(const char *ptr, int size, int *sp);
est_bzencode = libest_raw.est_bzencode
est_bzencode.__doc__ = \
    "Compress a serial object with BZIP2.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.  If it is negative, the size is assigned with\n"\
    "`strlen(ptr)'.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because the region of the return value is allocated with the `malloc' call, it should be\n"\
    "released with the `free' call if it is no longer in use."
est_bzencode.restype = c_char_p
est_bzencode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# char *est_bzdecode(const char *ptr, int size, int *sp);
est_bzdecode = libest_raw.est_bzdecode
est_bzdecode.__doc__ = \
    "Decompress a serial object compressed with BZIP2.\n"\
    "`ptr' specifies the pointer to a region.\n"\
    "`size' specifies the size of the region.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return\n"\
    "value is assigned.  If it is `NULL', it is not used.\n"\
    "If successful, the return value is the pointer to the result object, else, it is `NULL'.\n"\
    "Because an additional zero code is appended at the end of the region of the return value,\n"\
    "the return value can be treated as a character string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use."
est_bzdecode.restype = c_char_p
est_bzdecode.argtypes = [c_char_p, c_int, POINTER(c_int)]

# const char *est_border_str(void);
est_border_str = libest_raw.est_border_str
est_border_str.__doc__ = \
    "Get the border string for draft data of documents.\n"\
    "The return value is the border string for draft data of documents."
est_border_str.restype = c_char_p
est_border_str.argtypes = []

# double est_random(void);
est_random = libest_raw.est_random
est_random.__doc__ = \
    "Get the real random number.\n"\
    "The return value is the real random number between 0.0 and 1.0."
est_random.restype = c_double
est_random.argtypes = []

# double est_random_nd(void);
est_random_nd = libest_raw.est_random_nd
est_random_nd.__doc__ = \
    "Get the random number in normal distribution.\n"\
    "The return value is the random number in normal distribution between 0.0 and 1.0."
est_random_nd.restype = c_double
est_random_nd.argtypes = []

# char *est_make_crypt(const char *key);
est_make_crypt = libest_raw.est_make_crypt
est_make_crypt.__doc__ = \
    "Get an MD5 hash string of a key string.\n"\
    "`key' specifies a string to be encrypted.\n"\
    "The return value is an MD5 hash string of the key string.  Because the region of the return\n"\
    "value is allocated with the `malloc' call, it should be released with the `free' call if it\n"\
    "is no longer in use."
est_make_crypt.restype = c_char_p
est_make_crypt.argtypes = [c_char_p]

# int est_match_crypt(const char *key, const char *hash);
est_match_crypt = libest_raw.est_match_crypt
est_match_crypt.__doc__ = \
    "Check whether a key matches an MD5 hash string.\n"\
    "`key' specifies a string to be checked.\n"\
    "`hash' specifies an MD5 hash string.\n"\
    "The return value is true if the key matches the hash string, else it is false."
est_match_crypt.restype = c_int
est_match_crypt.argtypes = [c_char_p, c_char_p]

# void *est_regex_new(const char *str);
est_regex_new = libest_raw.est_regex_new
est_regex_new.__doc__ = \
    "Create a regular expression object.\n"\
    "`str' specifies a string of regular expressions.\n"\
    "The return value is a regular expression object or `NULL' if failure.\n"\
    "If the expression is leaded by \"*I:\", the pattern is case insensitive."
est_regex_new.restype = c_void_p
est_regex_new.argtypes = [c_char_p]

# void est_regex_delete(void *regex);
est_regex_delete = libest_raw.est_regex_delete
est_regex_delete.__doc__ = \
    "Delete a regular expression object.\n"\
    "`regex' specifies a regular expression object."
est_regex_delete.restype = None
est_regex_delete.argtypes = [c_void_p]

# int est_regex_match(const void *regex, const char *str);
est_regex_match = libest_raw.est_regex_match
est_regex_match.__doc__ = \
    "Check whether a regular expression matches a string.\n"\
    "`regex' specifies a regular expression object.\n"\
    "`str' specifies a string.\n"\
    "The return value is true if the regular expression object matchs the string."
est_regex_match.restype = c_int
est_regex_match.argtypes = [c_void_p, c_char_p]

# int est_regex_match_str(const char *rstr, const char *tstr);
est_regex_match_str = libest_raw.est_regex_match_str
est_regex_match_str.__doc__ = \
    "Check whether a regular expression matches a string.\n"\
    "`rstr' specifies a regular expression string.\n"\
    "`tstr' specifies a target string.\n"\
    "The return value is true if the regular expression string matchs the target string."
est_regex_match_str.restype = c_int
est_regex_match_str.argtypes = [c_char_p, c_char_p]

# char *est_regex_replace(const char *str, const char *bef, const char *aft);
est_regex_replace = libest_raw.est_regex_replace
est_regex_replace.__doc__ = \
    "Replace each substring matching a regular expression string.\n"\
    "`str' specifies a target string.\n"\
    "`bef' specifies a string of regular expressions for substrings.\n"\
    "`aft' specifies a string with which each substrings are replaced.  Each \"&\" in the string is\n"\
    "replaced with the matched substring.  Each \"\\\" in the string escapes the following character.\n"\
    "Special escapes \"\\1\" through \"\\9\" referring to the corresponding matching sub-expressions in\n"\
    "the regular expression string are supported.\n"\
    "The return value is a new converted string.  Even if the regular expression is invalid, a copy\n"\
    "of the original string is returned.  Because the region of the return value is allocated with\n"\
    "the `malloc' call, it should be released with the `free' call if it is no longer in use."
est_regex_replace.restype = c_char_p
est_regex_replace.argtypes = [c_char_p, c_char_p, c_char_p]

# ESTDOC *est_doc_dup(ESTDOC *doc);
est_doc_dup = libest_raw.est_doc_dup
est_doc_dup.__doc__ = \
    "Duplicate a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is a duplicated document object."
est_doc_dup.restype = c_void_p
est_doc_dup.argtypes = [c_void_p]

# void est_doc_set_id(ESTDOC *doc, int id);
est_doc_set_id = libest_raw.est_doc_set_id
est_doc_set_id.__doc__ = \
    "Set the ID number of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "`id' specifies the ID number to set."
est_doc_set_id.restype = None
est_doc_set_id.argtypes = [c_void_p, c_int]

# const char *est_doc_hidden_texts(ESTDOC *doc);
est_doc_hidden_texts = libest_raw.est_doc_hidden_texts
est_doc_hidden_texts.__doc__ = \
    "Get the hidden texts of a document object.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is concatenated sentences of the hidden text of the document object.  The\n"\
    "life duration of the returned string is synchronous with the one of the document object."
est_doc_hidden_texts.restype = c_char_p
est_doc_hidden_texts.argtypes = [c_void_p]

# void est_doc_slim(ESTDOC *doc, int size);
est_doc_slim = libest_raw.est_doc_slim
est_doc_slim.__doc__ = \
    "Reduce the texts to fit to the specified size.\n"\
    "`doc' specifies a document object.\n"\
    "`len' specifies the total size of the texts."
est_doc_slim.restype = None
est_doc_slim.argtypes = [c_void_p, c_int]

# int est_doc_is_empty(ESTDOC *doc);
est_doc_is_empty = libest_raw.est_doc_is_empty
est_doc_is_empty.__doc__ = \
    "Check whether a docuemnt object is empty.\n"\
    "`doc' specifies a document object.\n"\
    "The return value is true the document is empty, else it is false."
est_doc_is_empty.restype = c_int
est_doc_is_empty.argtypes = [c_void_p]

# ESTCOND *est_cond_dup(ESTCOND *cond);
est_cond_dup = libest_raw.est_cond_dup
est_cond_dup.__doc__ = \
    "Duplicate a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is a duplicated condition object."
est_cond_dup.restype = c_void_p
est_cond_dup.argtypes = [c_void_p]

# const char *est_cond_phrase(ESTCOND *cond);
est_cond_phrase = libest_raw.est_cond_phrase
est_cond_phrase.__doc__ = \
    "Get the phrase of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the phrase of the condition object or `NULL' if it is not specified.  The\n"\
    "life duration of the returned string is synchronous with the one of the condition object."
est_cond_phrase.restype = c_char_p
est_cond_phrase.argtypes = [c_void_p]

# const CBLIST *est_cond_attrs(ESTCOND *cond);
est_cond_attrs = libest_raw.est_cond_attrs
est_cond_attrs.__doc__ = \
    "Get a list object of attribute expressions of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is a list object of attribute expressions of the condition object or `NULL' if\n"\
    "it is not specified.  The life duration of the returned object is synchronous with the one of\n"\
    "the condition object."
est_cond_attrs.restype = c_void_p
est_cond_attrs.argtypes = [c_void_p]

# const char *est_cond_order(ESTCOND *cond);
est_cond_order = libest_raw.est_cond_order
est_cond_order.__doc__ = \
    "Get the order expression of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the order expression of the condition object or `NULL' if it is not\n"\
    "specified.  The life duration of the returned string is synchronous with the one of the\n"\
    "condition object."
est_cond_order.restype = c_char_p
est_cond_order.argtypes = [c_void_p]

# int est_cond_max(ESTCOND *cond);
est_cond_max = libest_raw.est_cond_max
est_cond_max.__doc__ = \
    "Get the maximum number of retrieval of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the maximum number of retrieval of the condition object or -1 if it is not\n"\
    "specified."
est_cond_max.restype = c_int
est_cond_max.argtypes = [c_void_p]

# int est_cond_skip(ESTCOND *cond);
est_cond_skip = libest_raw.est_cond_skip
est_cond_skip.__doc__ = \
    "Get the number of skipped documents of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the number of documents to be skipped in the search result."
est_cond_skip.restype = c_int
est_cond_skip.argtypes = [c_void_p]

# int est_cond_options(ESTCOND *cond);
est_cond_options = libest_raw.est_cond_options
est_cond_options.__doc__ = \
    "Get the options of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the options of the condition object."
est_cond_options.restype = c_int
est_cond_options.argtypes = [c_void_p]

# int est_cond_auxiliary(ESTCOND *cond);
est_cond_auxiliary = libest_raw.est_cond_auxiliary
est_cond_auxiliary.__doc__ = \
    "Get permission to adopt result of the auxiliary index.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is permission to adopt result of the auxiliary index."
est_cond_auxiliary.restype = c_int
est_cond_auxiliary.argtypes = [c_void_p]

# const char *est_cond_distinct(ESTCOND *cond);
est_cond_distinct = libest_raw.est_cond_distinct
est_cond_distinct.__doc__ = \
    "Get the attribute distinction filter.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the name of the distinct attribute or `NULL' if it is not specified.  The\n"\
    "life duration of the returned string is synchronous with the one of the condition object."
est_cond_distinct.restype = c_char_p
est_cond_distinct.argtypes = [c_void_p]

# int est_cond_mask(ESTCOND *cond);
est_cond_mask = libest_raw.est_cond_mask
est_cond_mask.__doc__ = \
    "Get the mask of targets of meta search.\n"\
    "`cond' specifies a condition object.\n"\
    "The return value is the mask of targets of meta search."
est_cond_mask.restype = c_int
est_cond_mask.argtypes = [c_void_p]

# int est_cond_score(ESTCOND *cond, int index);
est_cond_score = libest_raw.est_cond_score
est_cond_score.__doc__ = \
    "Get the score of a document corresponding to a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`index' specifies the index of an element of the result array of `est_db_search'.\n"\
    "The return value is the score of the element or -1 if the index is out of bounds."
est_cond_score.restype = c_int
est_cond_score.argtypes = [c_void_p, c_int]

# const int *est_cond_scores(ESTCOND *cond, int *nump);
est_cond_scores = libest_raw.est_cond_scores
est_cond_scores.__doc__ = \
    "Get the score array of corresponding documents of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`nump' specifies the pointer to a variable to which the number of elements in the score array\n"\
    "is assigned.\n"\
    "The return value is the score array of corresponding documents."
est_cond_scores.restype = POINTER(c_int)
est_cond_scores.argtypes = [c_void_p, POINTER(c_int)]

# void est_cond_set_narrowing_scores(ESTCOND *cond, const int *scores, int num);
est_cond_set_narrowing_scores = libest_raw.est_cond_set_narrowing_scores
est_cond_set_narrowing_scores.__doc__ = \
    "Set the narrowing scores of a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`scores' specifies the pointer to an array of narrowing scores.  The life duration of the\n"\
    "array should be equal to or longer than the condition object itself.\n"\
    "`num' specifies the number of the array."
est_cond_set_narrowing_scores.restype = None
est_cond_set_narrowing_scores.argtypes = [c_void_p, POINTER(c_int), c_int]

# int est_cond_auxiliary_word(ESTCOND *cond, const char *word);
est_cond_auxiliary_word = libest_raw.est_cond_auxiliary_word
est_cond_auxiliary_word.__doc__ = \
    "Check whether a condition object has used the auxiliary index.\n"\
    "`cond' specifies a condition object.\n"\
    "`word' specifies a keyword to be checked.  If it is an empty string, whether at least one\n"\
    "keyword is used is checked.\n"\
    "The return value is true if the condition object has used the auxiliary index, else it is\n"\
    "false"
est_cond_auxiliary_word.restype = c_int
est_cond_auxiliary_word.argtypes = [c_void_p, c_char_p]

# const int *est_cond_shadows(ESTCOND *cond, int id, int *np);
est_cond_shadows = libest_raw.est_cond_shadows
est_cond_shadows.__doc__ = \
    "Get an array of ID numbers of eclipsed docuemnts of a document in a condition object.\n"\
    "`cond' specifies a condition object.\n"\
    "`id' specifies the ID number of a parent document.\n"\
    "`np' specifies the pointer to a variable to which the number of elements of the return value\n"\
    "is assigned.\n"\
    "The return value is an array whose elements expresse the ID numbers and their scores\n"\
    "alternately."
est_cond_shadows.restype = POINTER(c_int)
est_cond_shadows.argtypes = [c_void_p, c_int, POINTER(c_int)]

# void est_cond_set_expander(ESTCOND *cond, void (*func)(const char *, CBLIST *));
est_cond_set_expander = libest_raw.est_cond_set_expander
est_cond_set_expander.__doc__ = \
    "Set the callback function for query expansion.\n"\
    "`cond' specifies a condition object.\n"\
    "`func' specifies the pointer to a function.  The first argument of the callback specifies a\n"\
    "word to be expand.  The second argument speciifes a list object into which renewed words to\n"\
    "be stored."
est_cond_set_expander.restype = None
est_cond_set_expander.argtypes = [c_void_p, c_void_p]

# void est_db_set_ecode(ESTDB *db, int ecode);
est_db_set_ecode = libest_raw.est_db_set_ecode
est_db_set_ecode.__doc__ = \
    "Set the error code of a database.\n"\
    "`db' specifies a database object.\n"\
    "`ecode' specifies a error code to set."
est_db_set_ecode.restype = None
est_db_set_ecode.argtypes = [c_void_p, c_int]

# int est_db_check_option(ESTDB *db, int option);
est_db_check_option = libest_raw.est_db_check_option
est_db_check_option.__doc__ = \
    "Check whether an option is set.\n"\
    "`db' specifies a database object.\n"\
    "`option' specifies an option used when opening the database.\n"\
    "The return value is 1 if the option is set, 0 if the option is not set, or -1 if it is\n"\
    "unknown."
est_db_check_option.restype = c_int
est_db_check_option.argtypes = [c_void_p, c_int]

# int est_db_inode(ESTDB *db);
est_db_inode = libest_raw.est_db_inode
est_db_inode.__doc__ = \
    "Get the inode number of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the inode number of the database."
est_db_inode.restype = c_int
est_db_inode.argtypes = [c_void_p]

# int est_db_set_doc_entity(ESTDB *db, int id, const char *ptr, int size);
est_db_set_doc_entity = libest_raw.est_db_set_doc_entity
est_db_set_doc_entity.__doc__ = \
    "Set the entity data of a document in a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`id' specifies the ID number of a registered document.\n"\
    "`ptr' specifies the pointer to a region of entity data.  If it is `NULL', the entity data is\n"\
    "removed.\n"\
    "`size' specifies the size of the region.\n"\
    "The return value is true if success, else it is false."
est_db_set_doc_entity.restype = c_int
est_db_set_doc_entity.argtypes = [c_void_p, c_int, c_char_p, c_int]

# char *est_db_get_doc_entity(ESTDB *db, int id, int *sp);
est_db_get_doc_entity = libest_raw.est_db_get_doc_entity
est_db_get_doc_entity.__doc__ = \
    "Get the entity data of a document in a database.\n"\
    "`db' specifies a database object.\n"\
    "`id' specifies the ID number of a registered document.\n"\
    "`sp' specifies the pointer to a variable to which the size of the region of the return value\n"\
    "is assigned.\n"\
    "The return value is the value of the entity data or `NULL' if it does not exist.  Because the\n"\
    "region of the return value is allocated with the `malloc' call, it should be released with\n"\
    "the `free' call if it is no longer in use."
est_db_get_doc_entity.restype = c_char_p
est_db_get_doc_entity.argtypes = [c_void_p, c_int, POINTER(c_int)]

# void est_db_set_wildmax(ESTDB *db, int num);
est_db_set_wildmax = libest_raw.est_db_set_wildmax
est_db_set_wildmax.__doc__ = \
    "Set the maximum number of expansion of wild cards.\n"\
    "`db' specifies a database object.\n"\
    "`num' specifies the maximum number of expansion of wild cards."
est_db_set_wildmax.restype = None
est_db_set_wildmax.argtypes = [c_void_p, c_int]

# void est_db_add_meta(ESTDB *db, const char *name, const char *value);
est_db_add_meta = libest_raw.est_db_add_meta
est_db_add_meta.__doc__ = \
    "Add a piece of meta data to a database.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`name' specifies the name of a piece of meta data.\n"\
    "`value' specifies the value of the meta data.  If it is `NULL', the meta data is removed."
est_db_add_meta.restype = None
est_db_add_meta.argtypes = [c_void_p, c_char_p, c_char_p]

# CBLIST *est_db_meta_names(ESTDB *db);
est_db_meta_names = libest_raw.est_db_meta_names
est_db_meta_names.__doc__ = \
    "Get a list of names of meta data of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is a new list object of meta data names of the document object.  Because the\n"\
    "object of the return value is opened with the function `cblistopen', it should be closed with\n"\
    "the function `cblistclose' if it is no longer in use."
est_db_meta_names.restype = c_void_p
est_db_meta_names.argtypes = [c_void_p]

# char *est_db_meta(ESTDB *db, const char *name);
est_db_meta = libest_raw.est_db_meta
est_db_meta.__doc__ = \
    "Get the value of a piece of meta data of a database.\n"\
    "`db' specifies a database object.\n"\
    "`name' specifies the name of a piece of meta data.\n"\
    "The return value is the value of the meta data or `NULL' if it does not exist.  Because the\n"\
    "region of the return value is allocated with the `malloc' call, it should be released with\n"\
    "the `free' call if it is no longer in use."
est_db_meta.restype = c_char_p
est_db_meta.argtypes = [c_void_p, c_char_p]

# CBMAP *est_db_etch_doc(ESTDB *db, ESTDOC *doc, int max);
est_db_etch_doc = libest_raw.est_db_etch_doc
est_db_etch_doc.__doc__ = \
    "Extract keywords of a document object.\n"\
    "`db' specifies a database object for TF-IDF tuning.  If it is `NULL', it is not used.\n"\
    "`doc' specifies a document object.\n"\
    "`max' specifies the maximum number of keywords to be extracted.\n"\
    "The return value is a new map object of keywords and their scores in decimal string.  Because\n"\
    "the object of the return value is opened with the function `cbmapopen', it should be closed\n"\
    "with the function `cbmapclose' if it is no longer in use."
est_db_etch_doc.restype = c_void_p
est_db_etch_doc.argtypes = [c_void_p, c_void_p, c_int]

# int est_db_put_keywords(ESTDB *db, int id, CBMAP *kwords, double weight);
est_db_put_keywords = libest_raw.est_db_put_keywords
est_db_put_keywords.__doc__ = \
    "Store a map object of keywords.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`id' specifies the ID number of a document.\n"\
    "`kwords' specifies a map object of keywords of the document.\n"\
    "`weight' specifies weighting bias of scores.\n"\
    "The return value is true if success, else it is false."
est_db_put_keywords.restype = c_int
est_db_put_keywords.argtypes = [c_void_p, c_int, c_void_p, c_double]

# int est_db_out_keywords(ESTDB *db, int id);
est_db_out_keywords = libest_raw.est_db_out_keywords
est_db_out_keywords.__doc__ = \
    "Remove keywords of a document.\n"\
    "`db' specifies a database object connected as a writer.\n"\
    "`id' specifies the ID number of a document.\n"\
    "The return value is true if success, else it is false."
est_db_out_keywords.restype = c_int
est_db_out_keywords.argtypes = [c_void_p, c_int]

# CBMAP *est_db_get_keywords(ESTDB *db, int id);
est_db_get_keywords = libest_raw.est_db_get_keywords
est_db_get_keywords.__doc__ = \
    "Retrieve a map object of keywords.\n"\
    "`db' specifies a database object.\n"\
    "`id' specifies the ID number of a document.\n"\
    "The return value is a new map object of keywords and their scores in decimal string.  If\n"\
    "keywords of the document is not stored, `NULL' is returned.  Because the object of the return\n"\
    "value is opened with the function `cbmapopen', it should be closed with the function\n"\
    "`cbmapclose' if it is no longer in use."
est_db_get_keywords.restype = c_void_p
est_db_get_keywords.argtypes = [c_void_p, c_int]

# int est_db_measure_doc(ESTDB *db, int id, int parts);
est_db_measure_doc = libest_raw.est_db_measure_doc
est_db_measure_doc.__doc__ = \
    "Mesure the total size of each inner records of a stored document.\n"\
    "`db' specifies a database object.\n"\
    "`id' specifies the ID number of a document.\n"\
    "`parts' specifies document parts: `ESTMDATTR' for attributes, `ESTMDTEXT' for texts, and\n"\
    "`ESTMDKWD' for keywords.  They can be specified at the same time by bitwise or.\n"\
    "The return value is the total size of each inner records of a stored document."
est_db_measure_doc.restype = c_int
est_db_measure_doc.argtypes = [c_void_p, c_int, c_int]

# int est_db_iter_init(ESTDB *db, const char *prev);
est_db_iter_init = libest_raw.est_db_iter_init
est_db_iter_init.__doc__ = \
    "Initialize the document iterator of a database.\n"\
    "`db' specifies a database object.\n"\
    "`prev' specifies the URI of the previous element of iteration.  If it is `NULL', it is not used.\n"\
    "The return value is true if success, else it is false."
est_db_iter_init.restype = c_int
est_db_iter_init.argtypes = [c_void_p, c_char_p]

# int est_db_iter_next(ESTDB *db);
est_db_iter_next = libest_raw.est_db_iter_next
est_db_iter_next.__doc__ = \
    "Get the next ID of the document iterator of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the next ID.  If there is no more document, 0 is returned.  On error,\n"\
    "-1 is returned."
est_db_iter_next.restype = c_int
est_db_iter_next.argtypes = [c_void_p]

# int est_db_word_iter_init(ESTDB *db);
est_db_word_iter_init = libest_raw.est_db_word_iter_init
est_db_word_iter_init.__doc__ = \
    "Initialize the word iterator of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is true if success, else it is false."
est_db_word_iter_init.restype = c_int
est_db_word_iter_init.argtypes = [c_void_p]

# char *est_db_word_iter_next(ESTDB *db);
est_db_word_iter_next = libest_raw.est_db_word_iter_next
est_db_word_iter_next.__doc__ = \
    "Get the next word of the word iterator of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the next word.  If there is no more word, `NULL' is returned.  Because\n"\
    "the region of the return value is allocated with the `malloc' call, it should be released\n"\
    "with the `free' call if it is no longer in use."
est_db_word_iter_next.restype = c_char_p
est_db_word_iter_next.argtypes = [c_void_p]

# int est_db_word_rec_size(ESTDB *db, const char *word);
est_db_word_rec_size = libest_raw.est_db_word_rec_size
est_db_word_rec_size.__doc__ = \
    "Get the size of the record of a word.\n"\
    "`db' specifies a database object.\n"\
    "`word' specifies a word.\n"\
    "The return value is the size of the record of the word.  If there is no corresponding record,\n"\
    "0 is returned."
est_db_word_rec_size.restype = c_int
est_db_word_rec_size.argtypes = [c_void_p, c_char_p]

# int est_db_keyword_num(ESTDB *db);
est_db_keyword_num = libest_raw.est_db_keyword_num
est_db_keyword_num.__doc__ = \
    "Get the number of unique keywords in a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the number of unique keywords in the database."
est_db_keyword_num.restype = c_int
est_db_keyword_num.argtypes = [c_void_p]

# int est_db_keyword_iter_init(ESTDB *db);
est_db_keyword_iter_init = libest_raw.est_db_keyword_iter_init
est_db_keyword_iter_init.__doc__ = \
    "Initialize the keyword iterator of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is true if success, else it is false."
est_db_keyword_iter_init.restype = c_int
est_db_keyword_iter_init.argtypes = [c_void_p]

# char *est_db_keyword_iter_next(ESTDB *db);
est_db_keyword_iter_next = libest_raw.est_db_keyword_iter_next
est_db_keyword_iter_next.__doc__ = \
    "Get the next keyword of the word iterator of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the next word.  If there is no more keyword, `NULL' is returned.  Because\n"\
    "the region of the return value is allocated with the `malloc' call, it should be released\n"\
    "with the `free' call if it is no longer in use."
est_db_keyword_iter_next.restype = c_char_p
est_db_keyword_iter_next.argtypes = [c_void_p]

# int est_db_keyword_rec_size(ESTDB *db, const char *word);
est_db_keyword_rec_size = libest_raw.est_db_keyword_rec_size
est_db_keyword_rec_size.__doc__ = \
    "Get the size of the record of a keyword.\n"\
    "`db' specifies a database object.\n"\
    "`word' specifies a keyword.\n"\
    "The return value is the size of the record of the keyword.  If there is no corresponding\n"\
    "record, 0 is returned."
est_db_keyword_rec_size.restype = c_int
est_db_keyword_rec_size.argtypes = [c_void_p, c_char_p]

# int *est_db_keyword_search(ESTDB *db, const char *word, int *nump);
est_db_keyword_search = libest_raw.est_db_keyword_search
est_db_keyword_search.__doc__ = \
    "Search documents corresponding a keyword for a database.\n"\
    "`db' specifies a database object.\n"\
    "`word' specifies a keyword.\n"\
    "`nump' specifies the pointer to a variable to which the number of elements in the result is\n"\
    "assigned.\n"\
    "The return value is an array whose elements are ID numbers of corresponding documents.\n"\
    "This function does never fail.  Even if no document corresponds or an error occurs, an empty\n"\
    "array is returned.  Because the region of the return value is allocated with the `malloc'\n"\
    "call, it should be released with the `free' call if it is no longer in use."
est_db_keyword_search.restype = POINTER(c_int)
est_db_keyword_search.argtypes = [c_void_p, c_char_p, POINTER(c_int)]

# int est_db_cache_num(ESTDB *db);
est_db_cache_num = libest_raw.est_db_cache_num
est_db_cache_num.__doc__ = \
    "Get the number of records in the cache memory of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the cache memory of a database."
est_db_cache_num.restype = c_int
est_db_cache_num.argtypes = [c_void_p]

# int est_db_used_cache_size(ESTDB *db);
est_db_used_cache_size = libest_raw.est_db_used_cache_size
est_db_used_cache_size.__doc__ = \
    "Get the size of used cache region.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the size of used cache region."
est_db_used_cache_size.restype = c_int
est_db_used_cache_size.argtypes = [c_void_p]

# void est_db_set_special_cache(ESTDB *db, const char *name, int num);
est_db_set_special_cache = libest_raw.est_db_set_special_cache
est_db_set_special_cache.__doc__ = \
    "Set the special cache for narrowing and sorting with document attributes.\n"\
    "`db' specifies a database object.\n"\
    "`name' specifies the name of a document.\n"\
    "`num' specifies the maximum number of cached records."
est_db_set_special_cache.restype = None
est_db_set_special_cache.argtypes = [c_void_p, c_char_p, c_int]

# void est_db_set_informer(ESTDB *db, void (*func)(const char *, void *), void *opaque);
est_db_set_informer = libest_raw.est_db_set_informer
est_db_set_informer.__doc__ = \
    "Set the callback function to inform of database events.\n"\
    "`db' specifies a database object.\n"\
    "`func' specifies the pointer to a function.  The first argument of the callback specifies a\n"\
    "message of each event.  The second argument specifies an arbitrary pointer of a opaque data.\n"\
    "`opaque' specifies the pointer of the second argument of the callback."
est_db_set_informer.restype = None
est_db_set_informer.argtypes = [c_void_p, c_void_p, c_void_p]

# void est_db_fill_key_cache(ESTDB *db);
est_db_fill_key_cache = libest_raw.est_db_fill_key_cache
est_db_fill_key_cache.__doc__ = \
    "Fill the cache for keys for TF-IDF.\n"\
    "`db' specifies a database object."
est_db_fill_key_cache.restype = None
est_db_fill_key_cache.argtypes = [c_void_p]

# void est_db_set_dfdb(ESTDB *db, DEPOT *dfdb);
est_db_set_dfdb = libest_raw.est_db_set_dfdb
est_db_set_dfdb.__doc__ = \
    "Set the database of document frequency.\n"\
    "`db' specifies a database object.\n"\
    "`dfdb' specifies a database object of `DEPOT'.  If it is `NULL', the setting is cleared."
est_db_set_dfdb.restype = None
est_db_set_dfdb.argtypes = [c_void_p, c_void_p]

# void est_db_refresh_rescc(ESTDB *db);
est_db_refresh_rescc = libest_raw.est_db_refresh_rescc
est_db_refresh_rescc.__doc__ = \
    "Clear the result cache.\n"\
    "`db' specifies a database object."
est_db_refresh_rescc.restype = None
est_db_refresh_rescc.argtypes = [c_void_p]

# void est_db_charge_rescc(ESTDB *db, int max);
est_db_charge_rescc = libest_raw.est_db_charge_rescc
est_db_charge_rescc.__doc__ = \
    "Charge the result cache.\n"\
    "`db' specifies a database object.\n"\
    "`max' specifies the maximum number of words to be charged.  If it not more than zero, all\n"\
    "words are charged."
est_db_charge_rescc.restype = None
est_db_charge_rescc.argtypes = [c_void_p, c_int]

# CBLIST *est_db_list_rescc(ESTDB *db);
est_db_list_rescc = libest_raw.est_db_list_rescc
est_db_list_rescc.__doc__ = \
    "Get a list of words in the result cache.\n"\
    "`db' specifies a database object.\n"\
    "The return value is a new list object of words in the result cache.  Because the object of the\n"\
    "return value is opened with the function `cblistopen', it should be closed with the function\n"\
    "`cblistclose' if it is no longer in use."
est_db_list_rescc.restype = c_void_p
est_db_list_rescc.argtypes = [c_void_p]

# int est_db_pseudo_doc_num(ESTDB *db);
est_db_pseudo_doc_num = libest_raw.est_db_pseudo_doc_num
est_db_pseudo_doc_num.__doc__ = \
    "Get the number of pseudo documents in a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is the number of pseudo documents in the database."
est_db_pseudo_doc_num.restype = c_int
est_db_pseudo_doc_num.argtypes = [c_void_p]

# CBLIST *est_db_attr_index_exprs(ESTDB *db);
est_db_attr_index_exprs = libest_raw.est_db_attr_index_exprs
est_db_attr_index_exprs.__doc__ = \
    "Get a list of expressions of attribute indexes of a database.\n"\
    "`db' specifies a database object.\n"\
    "The return value is a new list object of expressions of attribute indexes.  Because the object\n"\
    "of the return value is opened with the function `cblistopen', it should be closed with the\n"\
    "function `cblistclose' if it is no longer in use."
est_db_attr_index_exprs.restype = c_void_p
est_db_attr_index_exprs.argtypes = [c_void_p]

# void est_db_interrupt(ESTDB *db);
est_db_interrupt = libest_raw.est_db_interrupt
est_db_interrupt.__doc__ = \
    "Interrupt long time processing.\n"\
    "`db' specifies a database object."
est_db_interrupt.restype = None
est_db_interrupt.argtypes = [c_void_p]

# int est_db_repair(const char *name, int options, int *ecp);
est_db_repair = libest_raw.est_db_repair
est_db_repair.__doc__ = \
    "Repair a broken database directory.\n"\
    "`name' specifies the name of a database directory.\n"\
    "`options' specifies options: `ESTRPSTRICT' to perform strict consistency check, `ESTRPSHODDY'\n"\
    "to omit consistency check.\n"\
    "`ecp' specifies the pointer to a variable to which the error code is assigned.\n"\
    "The return value is true if success, else it is false."
est_db_repair.restype = c_int
est_db_repair.argtypes = [c_char_p, c_int, POINTER(c_int)]

# CBLIST *est_hints_to_words(CBMAP *hints);
est_hints_to_words = libest_raw.est_hints_to_words
est_hints_to_words.__doc__ = \
    "Extract words for snippet from hints of search.\n"\
    "`hints' specifies a map object whose records were set by `est_db_search'.\n"\
    "The return value is a new list object of words to be highlighted.  Because the object of the\n"\
    "return value is opened with the function `cblistopen', it should be closed with the function\n"\
    "`cblistclose' if it is no longer in use."
est_hints_to_words.restype = c_void_p
est_hints_to_words.argtypes = [c_void_p]

# void est_resmap_add(CBMAP *map, const char *key, int score, int method);
est_resmap_add = libest_raw.est_resmap_add
est_resmap_add.__doc__ = \
    "Add a record into a result map for logical operation.\n"\
    "`map' specifies a map object.\n"\
    "`key' specifies the key of a record.\n"\
    "`score' specifies the score of the record.\n"\
    "`method' specifies a scoring method when logical operation.  As for now, `ESTRMLOSUM',\n"\
    "`ESTRMLOMAX', `ESTRMLOMIN', and `ESTRMLOAVG'."
est_resmap_add.restype = None
est_resmap_add.argtypes = [c_void_p, c_char_p, c_int, c_int]

# ESTRESMAPELEM *est_resmap_dump(CBMAP *map, int min, int *nump);
est_resmap_dump = libest_raw.est_resmap_dump
est_resmap_dump.__doc__ = \
    "Dump a result list of a result map for logical operation.\n"\
    "`map' specifies a map object.\n"\
    "`min' specifies the minimum number of times for which each element of the result occurs.\n"\
    "`nump' specifies the pointer to a variable to which the number of elements in the result is\n"\
    "assigned.\n"\
    "The return value is an array whose elements are structures of keys and scores.  Because the\n"\
    "region of the return value is allocated with the `malloc' call, it should be released with the\n"\
    "`free' call if it is no longer in use."
est_resmap_dump.restype = c_void_p
est_resmap_dump.argtypes = [c_void_p, c_int, POINTER(c_int)]

# void est_proc_env_reset(void);
est_proc_env_reset = libest_raw.est_proc_env_reset
est_proc_env_reset.__doc__ = \
    "Reset the environment of the process.\n"\
    "This function sets the standard streams as binary mode and resets environment variables for\n"\
    "locale."
est_proc_env_reset.restype = None
est_proc_env_reset.argtypes = []

# int est_mkdir(const char *path);
est_mkdir = libest_raw.est_mkdir
est_mkdir.__doc__ = \
    "Make a directory.\n"\
    "`path' specifies the path of a new directory.\n"\
    "The return value is true if success, else it is false."
est_mkdir.restype = c_int
est_mkdir.argtypes = [c_char_p]

# int est_rmdir_rec(const char *path);
est_rmdir_rec = libest_raw.est_rmdir_rec
est_rmdir_rec.__doc__ = \
    "Remove a directory and its contents recursively.\n"\
    "`path' specifies the path of a directory.\n"\
    "The return value is true if success, else it is false."
est_rmdir_rec.restype = c_int
est_rmdir_rec.argtypes = [c_char_p]

# char *est_realpath(const char *path);
est_realpath = libest_raw.est_realpath
est_realpath.__doc__ = \
    "Get the canonicalized absolute pathname of a file.\n"\
    "`path' specifies the path of a file.\n"\
    "The return value is the canonicalized absolute pathname of a file.  Because the region of the\n"\
    "return value is allocated with the `malloc' call, it should be released with the `free' call\n"\
    "if it is no longer in use."
est_realpath.restype = c_char_p
est_realpath.argtypes = [c_char_p]

# int est_inode(const char *path);
est_inode = libest_raw.est_inode
est_inode.__doc__ = \
    "Get the inode number of a file.\n"\
    "`path' specifies the path of a file.\n"\
    "The return value is the inode number of a file or -1 on error."
est_inode.restype = c_int
est_inode.argtypes = [c_char_p]

# int est_utime(const char *path, time_t mtime);
est_utime = libest_raw.est_utime
est_utime.__doc__ = \
    "Change modification time of a file.\n"\
    "`path' specifies the path of a file.\n"\
    "`mtime' specifies modification time.  If it is negative, the current time is set.\n"\
    "The return value is true if success, else it is false."
est_utime.restype = c_int
est_utime.argtypes = [c_char_p, c_long] # TODO: 2nd arg is time_t

# double est_gettimeofday(void);
est_gettimeofday = libest_raw.est_gettimeofday
est_gettimeofday.__doc__ = \
    "Get the time of day in milliseconds.\n"\
    "The return value is the time of day in milliseconds."
est_gettimeofday.restype = c_double
est_gettimeofday.argtypes = []

# void est_usleep(unsigned long usec);
est_usleep = libest_raw.est_usleep
est_usleep.__doc__ = \
    "Suspend execution for microsecond intervals.\n"\
    "`usec' specifies microseconds to sleep for."
est_usleep.restype = None
est_usleep.argtypes = [c_ulong]

# void est_signal(int signum, void (*sighandler)(int));
est_signal = libest_raw.est_signal
est_signal.__doc__ = \
    "Set a signal handler.\n"\
    "`signum' specifies the number of a target signal.\n"\
    "`sighandler' specifies the pointer to a function.  The argument of the handler specifies the\n"\
    "number of the catched signal.  If it is `SIG_IGN', the signal is ignored."
est_signal.restype = None
est_signal.argtypes = [c_int, c_void_p]

# int est_kill(int pid, int sig);
est_kill = libest_raw.est_kill
est_kill.__doc__ = \
    "Send a signal to a process.\n"\
    "`pid' specifies the PID of a target process.\n"\
    "`sig' specifies a signal code.\n"\
    "The return value is true if success, else it is false."
est_kill.restype = c_int
est_kill.argtypes = [c_int, c_int]

# double est_memory_usage(void);
est_memory_usage = libest_raw.est_memory_usage
est_memory_usage.__doc__ = \
    "Get the load ratio of the physical memory.\n"\
    "The return value is the load ratio of the physical memory.\n"\
    "As for now, this function returns 0.0 on platforms except for Windows."
est_memory_usage.restype = c_double
est_memory_usage.argtypes = []

# const char *est_ext_type(const char *ext);
est_ext_type = libest_raw.est_ext_type
est_ext_type.__doc__ = \
    "Get the media type of an extention.\n"\
    "`ext' specifies the extension of a file path.\n"\
    "The return value is the media time of the extension."
est_ext_type.restype = c_char_p
est_ext_type.argtypes = [c_char_p]

# void est_vector_set_seed(CBMAP *svmap, int *svec, int vnum);
est_vector_set_seed = libest_raw.est_vector_set_seed
est_vector_set_seed.__doc__ = \
    "Set a seed vector from a map object.\n"\
    "`svmap' specifies a map object of a seed vector.\n"\
    "`svec' specifies a vector object.\n"\
    "`vnum' specifies the number of dimensions of the vector."
est_vector_set_seed.restype = None
est_vector_set_seed.argtypes = [c_void_p, POINTER(c_int), c_int]

# void est_vector_set_target(CBMAP *svmap, CBMAP *tvmap, int *tvec, int vnum);
est_vector_set_target = libest_raw.est_vector_set_target
est_vector_set_target.__doc__ = \
    "Set a target vector from a map object.\n"\
    "`svmap' specifies a map object of a seed vector.\n"\
    "`tvmap' specifies a map object of a target vector.\n"\
    "`tvec' specifies a vector object.\n"\
    "`vnum' specifies the number of dimensions of the vector."
est_vector_set_target.restype = None
est_vector_set_target.argtypes = [c_void_p, c_void_p, POINTER(c_int), c_int]

# double est_vector_cosine(const int *avec, const int *bvec, int vnum);
est_vector_cosine = libest_raw.est_vector_cosine
est_vector_cosine.__doc__ = \
    "Get the cosine of the angle of two vectors.\n"\
    "`avec' specifies a vector object.\n"\
    "`bvec' specifies the other vector object.\n"\
    "`vnum' specifies the number of dimensions of the vector.\n"\
    "The return value is the cosine of the angle of two vectors."
est_vector_cosine.restype = c_double
est_vector_cosine.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
