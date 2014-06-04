"""
Script to automatically launch all doctests from working directory and below
(in sub-directories). All files with ".py" and ".dt" extensions are found and
are used as argument to the doctest command doctest.testfile(). When writing
the doctests it must be remembered that each doctest containing file must
import the function being tested. As as example we have a file named "test.py"
in the directory "cold" located in the root of the installation (in the same
folder as the master file "run_full_doctest.py") - we wish to test the
function "wild". In this case we must ensure the following line
'>>> from cold.test import wild' is present before any doctest.

It is recommended to only include examples (thus doctests) in the ".py" file
which makes sense to demonstrate the capabilities of that given function. If a
more comprehensive test is desired besides that it is better placed in a file
of the same name but with extension ".dt" (for "DocTest"). If a test should
appear in both files it does not hurt as such - it is obviously not necessary
but it does not give any problems.

The script is executed as:

.. code-block:: python

   $ python run_full_doctest      # quiet test if all is ok
   $ python run_full_doctest -v   # to print all intermediate results

"""

import os
import doctest


# Files not included in the test
OMIT_FILES = ('run_full_doctest.py', 'run_single_doctest.py', '__init__.py')

# Perform test
PATH = './'
print('{0}'.format(78*'='))
for (dirpath, dirnames, filenames) in os.walk(PATH):
    for filename in filenames:
        # Extract filename extension
        ext_name = os.path.splitext(filename)[1][1:].strip().lower()

        # Perform doctest for all relevant .py and .dt files
        go = filename not in OMIT_FILES
        if ext_name in ('py', 'dt') and go:
            full_filename = os.sep.join([dirpath, filename])
            disp_str = "File under doctest:   {0}".format(filename)
            print("{0}\n{1}".format(disp_str, len(disp_str)*'-'))
            doctest.testfile(full_filename)
            print('{0}'.format(78*'='))
