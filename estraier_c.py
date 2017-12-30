import ctypes

from estraier_raw import *
from cabin_raw import *

libc = ctypes.CDLL("libc.so")

class Document(object):
    """Document class for hyperestraier.
    """
    def __init__(self):
        self._id = -1
        self._attr = {}
        self._texts = []
        self._hidden_texts = []
        self._keywords = {}
        self._score = None

    def add_attr(self, name, value):
        """Add an attribute.
        `name' specifies the name of an attribute.
        `value' specifies the value of the attribute.  If it is `None', the attribute is removed.
        """
        self._attr[name] = value
    
    def add_text(self, text):
        """Add a sentence of text.
        `text' specifies a sentence of text.
        """
        self._texts.append(text)
    
    def add_hidden_text(self, text):
        """Add a hidden sentence.
        `text' specifies a hidden sentence.
        """
        self._hidden_texts.append(text)
    
    def set_keywords(self, kwords):
        """Attach keywords.
        `kwords' specifies a hash object of keywords.  Keys of the hash should be keywords of the
        document and values should be their scores in decimal string.
        """
        self._keywords = kwords
    
    def set_score(self, score):
        """Set the substitute score.
        `score' specifies the substitute score.  It it is negative, the substitute score setting is
        nullified.
        """
        self._score = score
    
    def id(self):
        """Get the ID number.
        The return value is the ID number of the document object.  If the object has never been
        registered, -1 is returned.
        """
        return self._id
    
    def attr_names(self):
        """Get an array of attribute names of a document object.
        The return value is an array object of attribute names.
        """
        return self._attr.keys()
    
    def attr(self, name):
        """Get the value of an attribute.
        `name' specifies the name of an attribute.
        The return value is the value of the attribute or `None' if it does not exist.
        """
        if name in self._attr:
            return self._attr[name]
        else:
            return None
    
    def texts(self):
        """Get an array of sentences of the text.
        The return value is an array object of sentences of the text.
        """
        return self._texts
    
    def cat_texts(self):
        """Concatenate sentences of the text of a document object.
        The return value is concatenated sentences.
        """
        pass

    def fromNative(self, docNative):
        self._id = est_doc_id(docNative)
        attrnames = est_doc_attr_names(docNative)
        for i in range(cblistnum(attrnames)):
            a = cblistval(attrnames, i, None)
            self._attr[a.decode("utf-8")] = est_doc_attr(docNative, a)
        cblistclose(attrnames)
        textsNative = est_doc_texts(docNative)
        textsNum = cblistnum(textsNative)
        self._texts = [ cblistval(textsNative, i, None).decode("utf8") for i in range(textsNum) ]
        self._hidden_texts = [est_doc_hidden_texts(docNative).decode("utf-8")]
        self._score = est_doc_score(docNative)
    
    def toNative(self):
        docNative = est_doc_new()
        for key in self._attr:
            est_doc_add_attr(docNative,
                             key.encode("utf-8"),
                             self._attr[key].encode("utf-8"))
        for text1 in self._texts:
            est_doc_add_text(docNative, text1.encode("utf-8"))
        for text1 in self._hidden_texts:
            est_doc_add_hidden_text(docNative, text1.encode("utf-8"))
        if self._keywords:
            cbmapkw = cbmapopen()
            for key in self._keywords:
                cbmapput(cbmapkw, key.encode("utf-8"), -1,
                         value.encode("utf-8"), -1, 1)
            est_doc_set_keywords(docNative, cbmapkw)
            cbmapclose(cbmapkw)
        if self._score:
            est_doc_set_score(docNative, self.score)
        return docNative
    
    def deleteNative(self, docNative):
        est_doc_delete(docNative)

class Condition(object):
    SURE   = ESTCONDSURE           # check every N-gram key
    USUAL  = ESTCONDUSUAL          # check N-gram keys skipping by one
    FAST   = ESTCONDFAST           # check N-gram keys skipping by two
    AGITO  = ESTCONDAGITO          # check N-gram keys skipping by three
    NOIDF  = ESTCONDNOIDF          # without TF-IDF tuning
    SIMPLE = ESTCONDSIMPLE         # with the simplified phrase
    ROUGH  = ESTCONDROUGH          # with the rough phrase
    UNION  = ESTCONDUNION          # with the union phrase
    ISECT  = ESTCONDISECT          # with the intersection phrase
    SCFB   = ESTCONDSCFB           # feed back scores (for debug)
    
    def __init__(self):
        self.phrase = None
        self.attr = []
        self.order = None
        self.max = 0
        self.skip = 0
        self.options = 0
        self.auxiliary = 0
        self.eclipse = 0.0
        self.distinct = None
        self.mask = 0
    
    def set_phrase(self, phrase):
        """Set the search phrase.
        `phrase' specifies a search phrase.
        """
        self.phrase = phrase
    
    def add_attr(self, expr):
        """Add an expression for an attribute.
        `expr' specifies an expression for an attribute.
        """
        self.attr.append(expr)
    
    def set_order(self, expr):
        """Set the order of a condition object.
        `expr' specifies an expression for the order.  By default, the order is by score descending.
        """
        self.order = expr
    
    def set_max(self, max):
        """Set the maximum number of retrieval.
        `max' specifies the maximum number of retrieval.  By default, the number of retrieval is
        not limited.
        """
        self.max = max
    
    def set_skip(self, skip):
        """Set the number of skipped documents.
        `skip' specifies the number of documents to be skipped in the search result.
        """
        self.skip = skip
    
    def set_eclipse(self, limit):
        """Set the lower limit of similarity eclipse.
        `limit' specifies the lower limit of similarity for documents to be eclipsed.  Similarity is
        between 0.0 and 1.0.  If the limit is added by `Condition.ECLSIMURL', similarity is
        weighted by URL.  If the limit is `Condition.ECLSERV', similarity is ignored and documents
        in the same server are eclipsed.  If the limit is `Condition.ECLDIR', similarity is ignored
        and documents in the same directory are eclipsed.  If the limit is `Condition.ECLFILE',
        similarity is ignored and documents of the same file are eclipsed.
        """
        self.eclipse = limit
    
    def set_options(self, options):
        """Set options of retrieval.
        `options' specifies options: `Condition.SURE' specifies that it checks every N-gram
        key, `Condition.USUAL', which is the default, specifies that it checks N-gram keys
        with skipping one key, `Condition.FAST' skips two keys, `Condition.AGITO'
        skips three keys, `Condition.NOIDF' specifies not to perform TF-IDF tuning,
        `Condition.SIMPLE' specifies to use simplified phrase, `Condition.ROUGH' specifies to use
        rough phrase, `Condition.UNION' specifies to use union phrase, `Condition.ISECT' specifies
        to use intersection phrase.  Each option can be specified at the same time by bitwise or.
        If keys are skipped, though search speed is improved, the relevance ratio grows less.
        """
        self.options = options

    def set_auxiliary(self, min):
        """Set permission to adopt result of the auxiliary index.
        `min' specifies the minimum hits to adopt result of the auxiliary index.  If it is not more
        than 0, the auxiliary index is not used.  By default, it is 32.
        """
        self.auxiliary = min
    
    def set_distinct(self, name):
        """Set the attribute distinction filter.
        `name' specifies the name of an attribute to be distinct.
        """
        self.distinct = name
    
    def set_mask(self, mask):
        """Set the mask of targets of meta search.
        `mask' specifies a masking number.  1 means the first target, 2 means the second target, 4
        means the third target, and power values of 2 and their summation compose the mask.
        """
        self.mask = mask
    
    def toNative(self):
        condNative = est_cond_new()
        if self.phrase:
            est_cond_set_phrase(condNative, self.phrase.encode("utf-8"))
        for attr1 in self.attr:
            est_cond_add_attr(condNative, attr1.encode("utf-8"))
        if self.order:
            est_cond_set_order(condNative, self.order.encode("utf-8"))
        if self.max:
            est_cond_set_max(condNative, self.max)
        if self.skip:
            est_cond_set_skip(condNative, self.skip)
        if self.options:
            est_cond_set_options(condNative, self.options)
        if self.auxiliary:
            est_cond_set_auxiliary(condNatie, self.auxiliary)
        if self.eclipse:
            est_cond_set_eclipse(condNative, self.eclipse)
        if self.distinct:
            est_cond_set_distinct(condNative, self.distinct.encode("utf-8"))
        if self.mask:
            est_cond_set_mask(condNative, self.mask)
        return condNative

    def deleteNative(self, condNative):
        est_cond_delete(condNative)

class Result(object):
    def doc_num(self):
        """Get the number of documents.
        The return value is the number of documents in the result.
        """
        return len(self.doc_ids)
    
    def get_doc_id(self, index):
        """Get the ID number of a document.
        `index' specifies the index of a document.
        The return value is the ID number of the document or -1 if the index is out of bounds.
        """
        if len(self.doc_ids) <= index:
            return -1
        return self.doc_ids[index]
    
    def get_dbidx(self, index):
        """Get the index of the container database of a document.
        `index' specifies the index of a document.
        The return value is the index of the container database of the document or -1 if the index
        is out of bounds.
        """
        pass
        

class Database(object):
    DBREADER = ESTDBREADER         # open mode: open as a reader
    DBWRITER = ESTDBWRITER         # open mode: open as a writer
    DBCREAT  = ESTDBCREAT          # open mode: a writer creating
    DBTRUNC  = ESTDBTRUNC          # open mode: a writer truncating
    DBNOLCK  = ESTDBNOLCK          # open mode: open without locking
    DBLCKNB  = ESTDBLCKNB          # open mode: lock without blocking
    DBPERFNG = ESTDBPERFNG         # open mode: use perfect N-gram analyzer
    DBCHRCAT = ESTDBCHRCAT         # open mode: use character category analyzer
    DBSMALL  = ESTDBSMALL          # open mode: small tuning
    DBLARGE  = ESTDBLARGE          # open mode: large tuning
    DBHUGE   = ESTDBHUGE           # open mode: huge tuning
    DBHUGE2  = ESTDBHUGE2          # open mode: huge tuning second
    DBHUGE3  = ESTDBHUGE3          # open mode: huge tuning third
    DBSCVOID = ESTDBSCVOID         # open mode: store scores as void
    DBSCINT  = ESTDBSCINT          # open mode: store scores as integer
    DBSCASIS = ESTDBSCASIS         # open mode: refrain from adjustment of scores
    
    PDCLEAN  = ESTPDCLEAN          # put_doc option: clean up dispensable regions
    PDWEIGHT = ESTPDWEIGHT         # put_doc option: weight scores statically when indexing
    
    ODCLEAN  = ESTODCLEAN          # out_doc option: clean up dispensable regions
    
    GDNOATTR = ESTGDNOATTR         # get_doc option: no attributes
    GDNOTEXT = ESTGDNOTEXT         # get_doc option: no text
    GDNOKWD  = ESTGDNOKWD          # get_doc option: no keywords
    
    def search_meta(self, dbs, cond):
        """Search plural databases for documents corresponding a condition.
        `dbs' specifies an array whose elements are database objects.
        `cond' specifies a condition object.
        The return value is a result object.  On error, `nil' is returned.
        """
        # TODO
        pass
    
    def err_msg(self, ecode):
        """Get the string of an error code.
        `ecode' specifies an error code.
        The return value is the string of the error code.
        """
        return est_err_msg(ecode)
    
    def open(self, name, omode):
        """Open a database.
        `name' specifies the name of a database directory.
        `omode' specifies open modes: `Database.DBWRITER' as a writer, `Database.DBREADER' as a
        reader.  If the mode is `Database.DBWRITER', the following may be added by bitwise or:
        `Database.DBCREAT', which means it creates a new database if not exist,
        `Database.DBTRUNC', which means it creates a new database regardless if one exists.  Both
        of `Database.DBREADER' and  `Database.DBWRITER' can be added to by bitwise or:
        `Database.DBNOLCK', which means it opens a database file without file locking, or
        `Database.DBLCKNB', which means locking is performed without blocking.  If
        `Database.DBNOLCK' is used, the application is responsible for exclusion control.
        `Database.DBCREAT' can be added to by bitwise or: `Database.DBPERFNG', which means N-gram
        analysis is performed against European text also, `Database.DBCHACAT', which means
        character category analysis is performed instead of N-gram analysis, `Database.DBSMALL',
        which means the index is tuned to register less than 50000 documents, `Database.DBLARGE',
        which means the index is tuned to register more than 300000 documents, `Database.DBHUGE',
        which means the index is tuned to register more than 1000000 documents, `Database.DBHUGE2',
        which means the index is tuned to register more than 5000000 documents, `Database.DBHUGE3',
        which means the index is tuned to register more than 10000000 documents,
        `Database.DBSCVOID', which means scores are stored as void, `Database.DBSCINT', which
        means scores are stored as 32-bit integer, `Database.DBSCASIS', which means scores are
        stored as-is and marked not to be tuned when search.
        The return value is true if success, else it is false.
        """
        ecode = ctypes.c_int()
        self.estdb = est_db_open(name.encode("utf-8"), omode, ctypes.byref(ecode))
        if not self.estdb:
            return False
        return True

    def close(self):
        """Close the database.
        The return value is true if success, else it is false.
        """
        ecode = ctypes.c_int()
        self.estdb = est_db_close(self.estdb, ctypes.byref(ecode))
        if not self.estdb:
            return False
        return True
    
    def error(self):
        """Get the last happened error code.
        The return value is the last happened error code.
        """
        return est_db_error(self.estdb)
    
    def fatal(self):
        """Check whether the database has a fatal error.
        The return value is true if the database has fatal erroor, else it is false.
        """
        return est_db_fatal(self.estdb)
    
    def add_attr_index(self, name, type):
        """Add an index for narrowing or sorting with document attributes.
        `name' specifies the name of an attribute.
        `type' specifies the data type of attribute index; `Database.IDXATTRSEQ' for multipurpose
        sequencial access method, `Database.IDXATTRSTR' for narrowing with attributes as strings,
        `Database.IDXATTRNUM' for narrowing with attributes as numbers.
        The return value is true if success, else it is false.
        """
        pass
    
    def flush(self, max):
        """Flush index words in the cache.
        `max' specifies the maximum number of words to be flushed.  If it not more than zero, all
        words are flushed.
        The return value is true if success, else it is false.
        """
        rv = est_db_flush(self.estdb, max)
        if rv:
            return True
        else:
            return False
    
    def sync(self):
        """Synchronize updating contents.
        The return value is true if success, else it is false.
        """
        rv = est_db_sync(self.estdb)
        if rv:
            return True
        else:
            return False
    
    def optimize(self, options):
        """Optimize the database.
        `options' specifies options: `Database.OPTNOPURGE' to omit purging dispensable region of
        deleted documents, `Database.OPTNODBOPT' to omit optimization of the database files.  The
        two can be specified at the same time by bitwise or.
        The return value is true if success, else it is false.
        """
        rv = est_db_optimize(self.estdb, options)
        if rv:
            return True
        else:
            return False
    
    def merge(self, name, options):
        """Merge another database.
        `name' specifies the name of another database directory.
        `options' specifies options: `Database.MGCLEAN' to clean up dispensable regions of the
        deleted document.
        The return value is true if success, else it is false.
        """
        rv = est_db_merge(self.estdb, name.encode("utf-8"), options)
        if rv:
            return True
        else:
            return False
    
    def put_doc(self, doc, options):
        """Add a document.
        `doc' specifies a document object.  The document object should have the URI attribute.
        `options' specifies options: `Database.PDCLEAN' to clean up dispensable regions of the
        overwritten document.
        The return value is true if success, else it is false.
        """
        docNative = doc.toNative()
        rv = est_db_put_doc(self.estdb, docNative, options)
        doc.deleteNative(docNative)
        if rv:
            return True
        else:
            return False
    
    def out_doc(self, id, options):
        """Remove a document.
        `id' specifies the ID number of a registered document.
        `options' specifies options: `Database::ODCLEAN' to clean up dispensable regions of the
        deleted document.
        The return value is true if success, else it is false.
        """
        rv = est_db_out_doc(self.estdb, id, options)
        if rv:
            return True
        else:
            return False
    
    def edit_doc(self, doc):
        """Edit attributes of a document.
        `doc' specifies a document object.
        The return value is true if success, else it is false.
        """
        pass
    
    def get_doc(self, id, options):
        """Retrieve a document.
        `id' specifies the ID number of a registered document.
        `options' specifies options: `Database.GDNOATTR' to ignore attributes, `Database.GDNOTEXT'
        to ignore the body text, `Database.GDNOKWD' to ignore keywords.  The three can be
        specified at the same time by bitwise or.
        The return value is a document object.  On error, `nil' is returned.
        """
        doc = Document()
        options = 0
        docNative = est_db_get_doc(self.estdb, id, options)
        doc.fromNative(docNative)
        doc.deleteNative(docNative)
        return doc
    
    def get_doc_attr(self, id, name):
        """Retrieve the value of an attribute of a document.
        `id' specifies the ID number of a registered document.
        `name' specifies the name of an attribute.
        The return value is the value of the attribute or `nil' if it does not exist.
        """
        pass
    
    def uri_to_id(self, uri):
        """Get the ID of a document specified by URI.
        `uri' specifies the URI of a registered document.
        The return value is the ID of the document.  On error, -1 is returned.
        """
        return est_db_uri_to_id(self.estdb, uri.encode("utf-8"))
    
    def search(self, cond):
        num = ctypes.c_int()
        condNative = cond.toNative()
        hints = cbmapopenex(31) # MINIBNUM
        idsNative = est_db_search(self.estdb, condNative,
                                  ctypes.byref(num), hints)
        cond.deleteNative(condNative)
        
        result = Result()
        result.doc_ids = [idsNative[i] for i in range(num.value)]
        libc.free(idsNative)
        result.hitnum = int(cbmapget(hints, "", 0, None))
        cbmapclose(hints)
        return result
    
    def getDoc(self, id, options):
        doc = Document()
        options = 0
        docNative = est_db_get_doc(self.estdb, id, options)
        doc.fromNative(docNative)
        doc.deleteNative(docNative)
        return doc
