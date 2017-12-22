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

from ctypes import CDLL, POINTER, c_int, c_double, c_char_p, c_void_p, c_size_t

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
# API for document
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
