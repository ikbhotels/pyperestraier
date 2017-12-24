# pyperestraier
**pyperestraier** is a Python API for [Hyperestraier](http://fallabs.com/hyperestraier/).
This package contains several levels API.

## Raw level API for native library
estraier_raw.py and cabin_raw.py are simple [ctypes](https://docs.python.org/2.7/library/ctypes.html) porting
from original Hyperestraier's estraier.h and cabin.h.
They depends on original Hyperestraier's libestraier.so.
Sample programs gatherer_raw.py and searcher_raw.py,
ported from [Hyperestraier's Programming Guide](http://fallabs.com/hyperestraier/pguide-en.html),
are also available.
