"""
Script to doctests of a specific module.  Input to the script
is full relative directory and main filename (without ".py" or
".dtst" extension).  The script tests for both a matching ".py"
and ".dtst" files.

It is recommended to only include examples (thus doctests) in the
".py" file which makes sense to demonstrate the capabilities of that
given function.  If a more comprehensive test is desired besides that
it is better placed in a file of the same name but with extension
".dt" (for "DocTest").  If a test should appear in both files it
does not hurt as such - it is obviously not necessary but it does
not give any problems.

If we have a file structure as e.g.:

    run_single_doctest.py
    warm/tvt.py
        /tvt.dt
        /...
        /...

The script is executed for test of "tvt" as:

    $ python run_single_doctest warm/tvt       # quiet test
    $ python run_single_doctest warm/tvt -v    # verbose test

"""

import sys
import os
import doctest

# Read filename from input arg
full_module_name = sys.argv[1]

# Perform doctest of .py file if it exists
print('{0}'.format(78*'='))
full_file_name = "{0}.{1}".format(full_module_name, 'py')
if os.path.isfile(full_file_name):
    print('File under doctest:   {0}'.format(full_file_name))
    doctest.testfile(full_file_name)

# Perform doctest of .dt file if it exists
full_file_name = "{0}.{1}".format(full_module_name, 'dt')
if os.path.isfile(full_file_name):
    print('{0}'.format(78*'-'))
    print('File under doctest:   {0}'.format(full_file_name))
    doctest.testfile(full_file_name)
print('{0}'.format(78*'='))
