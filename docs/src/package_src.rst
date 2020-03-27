.. _pkg-src:

==============
Package source
==============

"""""""""
Directory
"""""""""

This will install the package that is located at the directory::

    carbin install ~/mylibrary/

There must be a ``CMakeLists.txt`` in the directory.

""""
File
""""

An archived file of the package::

    carbin install zlib-1.2.11.tar.gz

The archive will be unpacked and installed.

"""
URL
"""

A url to the package::

    carbin install http://zlib.net/zlib-1.2.11.tar.gz

The file will be downloaded, unpacked, and installed.

""""""
Github
""""""

A package can be installed directly from github using just the namespace and repo name. For example, John MacFarlane's implementation of CommonMark in C called `cmark <https://github.com/jgm/cmark>`_ can be installed like this::

    carbin install jgm/cmark

A tag or branch can specified using the ``@`` symbol::

    carbin install jgm/cmark@0.24.1

""""""
Recipe
""""""

A recipe name can also be installed. See :doc:`recipe` for more info.

""""""""
Aliasing
""""""""

Aliasing lets you pick a different name for the package. So when we are installing ``zlib``, we could alias it as ``zlib``::

    carbin install zlib,http://zlib.net/zlib-1.2.11.tar.gz

This way the package can be referred to as ``zlib`` instead of ``http://zlib.net/zlib-1.2.11.tar.gz``.
