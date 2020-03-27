==========
Using carbin
==========

-------------------------
Installing cmake packages
-------------------------

When package is installed from one of the package sources(see :ref:`pkg-src`) using the :ref:`install` command, ``carbin`` will run the equivalent cmake commands to install it::

    mkdir build
    cd build
    cmake -DCMAKE_TOOLCHAIN_FILE=$CARBIN_PREFIX/carbin/carbin.cmake -DCMAKE_INSTALL_PREFIX=$CARBIN_PREFIX ..
    cmake --build .
    cmake --build . --target install

However, ``carbin`` will always create the build directory out of source. The ``carbin.cmake`` is a toolchain file that is setup by ``carbin``, so that cmake can find the installed packages. Other settings can be added about the toolchain as well(see :ref:`init`).

The ``carbin.cmake`` toolchain file can be useful for cmake projects to use. This will enable cmake to find the dependencies installed by ``carbin`` as well::

    cmake -DCMAKE_TOOLCHAIN_FILE=$CARBIN_PREFIX/carbin/carbin.cmake ..

Instead of passing in the toolchain, ``carbin`` provides a build command to take of this already(see :ref:`build`). This will configure cmake with ``carbin.cmake`` toolchain file and build the project::

    carbin build

By default, it will build the ``all`` target, but a target can be specified as well::

    carbin build --target some_target

For projects that don't use cmake, then its matter of searching for the dependencies in ``CARBIN_PREFIX``. Also, it is quite common for packages to provide ``pkg-config`` files for managing dependencies. So, ``carbin`` provides a ``pkg-config`` command that will search for the dependencies that ``carbin`` has installed. For example, ``carbin pkg-config`` can be used to link in the dependencies for zlib without needing cmake::

    carbin install zlib,http://zlib.net/zlib-1.2.11.tar.gz
    g++ src.cpp `carbin pkg-config zlib --cflags --libs`


-----------------------------
Installing non-cmake packages
-----------------------------


Carbin can install non-cmake packages as well. Due note that non-cmake build systems do not have a way to tell the build where the dependencies are installed. Carbin will set environmnet variables such as ``PKG_CONFIG_PATH`` and ``PATH``, but if the dependencies are not found using pkg-config or these standard environmnet variables then you will need to consult the build scripts as to what protocol is needed to resolve the dependencies.

.. _custom-cmake:

""""""""""""""""""
Using custom cmake
""""""""""""""""""

For packages that don't support building with cmake. A cmake file can be provided to build the package. This can either build the sources or bootstrap the build system for the package::

    carbin install SomePackage --cmake mycmake.cmake

"""""""""""""""""""""
Header-only libraries
"""""""""""""""""""""

For libraries that are header-only, ``carbin`` provides a cmake file ``header`` to install the headers. For example, Boost.Preprocessor library can be installed like this::

    carbin install boostorg/preprocessor --cmake header

By default, it installs the headers in the 'include' directory, but this can be changed by setting the ``INCLUDE_DIR`` cmake variable::

    carbin install boostorg/preprocessor --cmake header -DINCLUDE_DIR=include

""""""""
Binaries
""""""""

For binaries, ``carbin`` provides a cmake file ``binary`` which will install all the files in the package without building any source files. For example, the clang binaries for ubuntu can be installed like this::

    carbin install clang,http://llvm.org/releases/3.9.0/clang+llvm-3.9.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz  --cmake binary


""""""""""""""""""
CMake Subdirectory
""""""""""""""""""

If cmake is not in the top-level directory this will use the cmake in a subdirectory::

    carbin install google/protobuf --cmake subdir

By default, it uses a directory named ``cmake``, but this can be changed by setting the ``CMAKE_DIR`` variable::

    carbin install sandstorm-io/capnproto --cmake subdir -DCMAKE_DIR=c++

.. _boost-cmake:

"""""
Boost
"""""

A cmake ``boost`` is provided to install boost libraries as well::

    carbin install boost,http://downloads.sourceforge.net/project/boost/boost/1.62.0/boost_1_62_0.tar.bz2 --cmake boost

Libraries can be selected with cmake variables ``BOOST_WITH_`` and ``BOOST_WITHOUT_``. For example, just Boost.Filesystem(and it dependencies) can be built as::

    carbin install boost,http://downloads.sourceforge.net/project/boost/boost/1.62.0/boost_1_62_0.tar.bz2 --cmake boost -DBOOST_WITH_FILESYSTEM=1

Also, everthing can be built except Boost.Python like the following::

    carbin install boost,http://downloads.sourceforge.net/project/boost/boost/1.62.0/boost_1_62_0.tar.bz2 --cmake boost -DBOOST_WITHOUT_PYTHON=1

"""""
Meson
"""""

A cmake ``meson`` is provided to build packages that use the meson build system. CMake variables of the form ``MESON_SOME_VAR`` are passed to meson as a variable ``some-var``.

To use meson you will need python 3.5 or later, with meson and ninja installed. It can be installed with ``pip3 install meson ninja``. Carbin does not provide an installation of meson.

"""""""""
Autotools
"""""""""

A cmake ``autotools`` is provided to build autotools-based libraries. Autotools is not a portable build system and may not work on all platforms.

""""
Make
""""

A cmake ``make`` is provided to build makefile-based libraries. This will invoke ``make`` and then ``make install``. It will set the ``PREFIX`` variable to the installation location. Makefile is not a portable build system and may not work on all platforms.

