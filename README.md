# pyperestraier
**pyperestraier** is a Python API for [Hyper Estraier](http://fallabs.com/hyperestraier/).
This package contains several levels API.

## Raw level API for native library
estraier_raw.py and cabin_raw.py are simple [ctypes](https://docs.python.org/2.7/library/ctypes.html) porting
from original Hyper Estraier's estraier.h and cabin.h.
They depends on original Hyper Estraier's libestraier.so.
Sample programs gatherer_raw.py and searcher_raw.py,
ported from [Hyper Estraier's Programming Guide](http://fallabs.com/hyperestraier/pguide-en.html),
are also available.

## Class level API for native library
estraier_c.py is a class library which wraps estaier_raw.py.
It depends on original Hyper Estaier's libestraier.so.
API is intended to be compatible with [Java native API](http://fallabs.com/hyperestraier/javanativeapi/) and [Ruby native API](http://fallabs.com/hyperestraier/rubynativeapi/).
gatherer.py and searcher.py are samples for this layer.
