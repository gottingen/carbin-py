============
Introduction
============

Cmake package retrieval. This can be used to download and install cmake packages. The advantages of using ``carbin`` are:

* Non-intrusive: There is no need to write special hooks in cmake to use ``carbin``. One cmake file is written and can be used to install a package with ``carbin`` or standalone.
* Works out of the box: Since it uses the standard build and install of cmake, it already works with almost all cmake packages. There is no need to wait for packages to convert over to support ``carbin``. Standard cmake packages can be already installed immediately.
* Decentralized: Packages can be installed from anywhere, from github, urls, or local files.


---------------
Installing carbin
---------------

``carbin`` can be simply installed using ``pip`` (you can get pip from `here <https://pip.pypa.io/en/stable/installing/>`_)::

    pip install carbin

Or installed directly with python::

    python setup.py install

On windows, you may want to install pkgconfig-lite to support packages that use pkgconfig. This can be installed with ``carbin`` as well::

    carbin install pfultz2/pkgconfig

----------
Quickstart
----------

We can also install cmake packages directly from source files, for example zlib::

    carbin install http://zlib.net/zlib-1.2.11.tar.gz

However, its much easier to install recipes so we don't have to remember urls::

    carbin install pfultz2/carbin-recipes

Then we can install packages such as boost::

    carbin install boost

Or curl::

    carbin install curl

-----
Usage
-----

""""""""""""""""""""
Installing a package
""""""""""""""""""""

Any library that uses cmake to build can be built and installed as a package with ``carbin``. A source for package can be from many areas (see :ref:`pkg-src`). We can simply install ``zlib`` with its URL::

    carbin install http://zlib.net/zlib-1.2.11.tar.gz

We can install the package from github as well, using a shorten form. For example, installing John MacFarlane's implementation of CommonMark in C called `cmark <https://github.com/jgm/cmark>`_::

    carbin install jgm/cmark


""""""""""""""""""
Removing a package
""""""""""""""""""

A package can be removed by using the same source name that was used to install the package::

    carbin install http://zlib.net/zlib-1.2.11.tar.gz
    carbin remove http://zlib.net/zlib-1.2.11.tar.gz

If an alias was specified, then the name of the alias must be used instead::

    carbin install zlib,http://zlib.net/zlib-1.2.11.tar.gz
    carbin remove zlib

""""""""""""""""
Testing packages
""""""""""""""""

The test suite for a package can be ran before installing it, by using the ``--test`` flag. This will either build the ``check`` target or run ``ctest``. So if we want to run the tests for zlib we can do this::

    carbin install --test http://zlib.net/zlib-1.2.11.tar.gz


""""""""""""""""""
Setting the prefix
""""""""""""""""""

By default, the packages are installed in the local directory ``carbin``. This can be changed by using the ``--prefix`` flag::

    carbin install --prefix /usr/local zlib:http://zlib.net/zlib-1.2.11.tar.gz

The prefix can also be set with the ``CARBIN_PREFIX`` environment variable.

""""""""""""""""""""""
Integration with cmake
""""""""""""""""""""""

By default, carbin creates a cmake toolchain file with the settings necessary to build and find the libraries in the carbin prefix. The toolchain file is at ``$CARBIN_PREFIX/carbin.cmake``. If another toolchain needs to be used, it can be specified with the ``init`` command::

    carbin init --toolchain my_cmake_toolchain.cmake

Also, the C++ version can be set for the toolchain as well::

    carbin init --std=c++14

Which is necessary to use modern C++ on many compilers.

