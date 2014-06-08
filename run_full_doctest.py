"""
When running this file as a script it can be done in the following
ways:

.. code-block:: python

   $ python run_full_doctest.py
   $ python run_full_doctest.py -q
   $ python run_full_doctest.py -v
   $ python run_full_doctest.py DIRECTORY -q
   $ python run_full_doctest.py DIRECTORY -v

where DIRECTORY is the directory from where a full test is conducted
including all sub-directories and files with extensions '.py' and '.dt'.
DIRECTORY must not be absolute (i.e. not begin with '/') and it must
separate segments by '/' (such as './subdir1/subdir2').

"""

import sys


import pytils


if __name__ == "__main__":
    (path, verbose) = ('./', '-q')
    if len(sys.argv) > 2:
        path = sys.argv[1]
    if len(sys.argv) > 1:
        verbose = sys.argv[-1]
    pytils.launchers.doctests.run(path, verbose)