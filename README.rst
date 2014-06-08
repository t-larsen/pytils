======
README
======

:Developer:
    Torben Larsen

:Institution:
   Aalborg University,
   Department of Electronic Systems,
   Signal and Information Processing

:Version:
    0.0.1


Introduction
------------
**pytils** is a collection of Python utilities implemented as scripts
and modules, which can be used in various applications of Python code
development.


Installation
------------
The **pytils** package is normally distributed in a zip-file with all
computation, documentation, test files etc. included. Say the name
of the folder you extract the zip-file is **PACKAGE_ROOT** then
extracting **pytils** provides you with a structure like:

.. code-block:: python

   PACKAGE_ROOT/__init__.py
                doc/
                LICENSE.rst
                pytils/
                MANIFEST.in
                README.rst
                run_all_tests.py
                test/

You must then set the PYTHONPATH to include 'PACKAGE_ROOT', which
in a BASH-shell can be done as:

.. code-block:: python

   export PYTHONPATH=PACKAGE_ROOT

This ensures that the **pytils** package can be imported as expected and thus
be used from any place in the directory structure. Note that when you extract
the 'pytils.zip' file it results in a folder (among others) named
'pytils/pytils'. When you set PYTHONPATH the first of these 'pytils'
directories (the root mandel directory) must be contained in the PYTHONPATH
name as the last directory.


Documentation
-------------
The package is documented using **Sphinx** by use of a combination of two
elements:

1. Static ReStrucTured (.rst) text files describing the problem,
   theory etc. which is located in the directory
   'PACKAGE_ROOT/doc/source'.

2. Dynamic ReStrucTured (.rst) text files extracted from the
   docstrings in the developed functions.

The documentation can be found as a html file at:

.. code-block:: python

   PACKAGE_ROOT/doc/build/html/index.html


Testing
-------
The **pytils** package implements a few number of doctests to test against
PEP8, input type and value check for functions, i/o tests etc. The
tests performed are either part of the examples in function
docstrings or part of the 'pytils/test/' folder with '.dt' doctests.
A full test of all relevant '.py' and '.dt' files are done as either
of the following:

.. code-block:: python

   $ cd PACKAGE_ROOT
   $ python run_all_tests.py     # quiet
   $ python run_all_tests.py -v  # verbose

In quiet mode a list is provided of all files containing test scenarios.
If a test is completed without errors nothing is done and if an error
occurs the detailed information is provided. In verbose mode, all the
tests are provided as well as the result. This leads to substantial 
information and should only be done to analyse the details of the tests 
(although it is better to inspect all '.py' and '.dt' files).


Changelog
---------

.. include:: ../../../CHANGELOG.rst


License
-------

.. include:: ../../../LICENSE.rst



