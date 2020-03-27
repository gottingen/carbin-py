=============
Using recipes
=============

Many times a package doesn't list its dependencies in a requirements.txt file, or it requires special defines or custom cmake(see :ref:`custom-cmake`). A recipe helps simplify this, by allowing a package to be installed with a simple recipe name without needing to update the original package source. 

---------------------
Structure of a recipe
---------------------

A recipe is a directoy which contains a 'package.txt' file and an optional 'requirements.txt' file. If a 'requirements.txt' is not provided, then the requirements file in the package will be used otherwise the requirements file in the recipe will be used and the package's requirements.txt will be ignored.

Both files follow the format describe in :any:`requirements`. The 'package.txt' file list only one package, which is the package to be installed. The 'requirements.txt' list packages to be installed as dependecies, which can also reference other recipes. 

All recipe directories are searched under the ``$CARBIN_PREFIX/etc/carbin/recipes/`` directory. A cmake package can install additional recipes through carbin. 

For example, we could build a simple recipe for zlib so we don't have to remember the url everytime. By adding the file ``$CARBIN_PREFIX/etc/carbin/recipes/zlib/package.txt`` with the url like this::

    http://zlib.net/zlib-1.2.11.tar.gz

We can now install zlib with just ``carbin install zlib``. Additionally, we can set additional options as well. For example, if we want to install boost, we can write ``$CARBIN_PREFIX/etc/carbin/recipes/boost/package.txt`` to use the boost cmake(see :ref:`boost-cmake`)::

    http://downloads.sourceforge.net/project/boost/boost/1.62.0/boost_1_62_0.tar.bz2 --cmake boost   

We can also make zlib a dependency of boost by writing a ``$CARBIN_PREFIX/etc/carbin/recipes/boost/requirements.txt`` file listing zlib::

    zlib

So, now we can easily install boost with ``carbin install boost`` and it will install zlib automatically as well.

---------------
Getting recipes
---------------

The `carbin-recipes <https://github.com/pfultz2/carbin-recipes>`_ repository maintains a set of recipes for many packages. It can be easily installed with::

    carbin install pfultz2/carbin-recipes


