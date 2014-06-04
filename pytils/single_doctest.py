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

.. code-block:: python

   run_single_doctest.py
   warm/tvt.py
       /tvt.dt
       /...
       /...

The script is executed for test of "tvt" as:

.. code-block:: python

   $ python run_single_doctest warm/tvt       # quiet test
   $ python run_single_doctest warm/tvt -v    # verbose test

"""

import sys
import os
import doctest


def single_test(*args):
    """Perform full doctest of all relevant .py and .dt files.

    Args:
        *path* (str): Path of the source directory for which to search
        for doctest containing .py and .dt files. All directories
        below *path* is also searched.

        *verbose* (str): Verbose level where '-v' indicates detailed
        test information is printed. Any other setting provides a
        'quiet' mode where only the tested filename is provided when
        a test passes - and detailed information is provided if the
        test fails.

    Returns:
        Nothing.

    Raises:
        Nothing.

    """
    # Validate inputs and set default verbose if necessary
    if not len(args) > 0:
        raise ValueError('No filename specified.')
    if not os.path.isfile(args[0]):
        raise ValueError('File does not exist.')
    (full_module_name, verbose) = (args[0], 'quiet')
    if len(args) > 1:
        verbose = args[1]

    print full_module_name, verbose
    
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


if __name__ == "__main__":
    single_test(*sys.argv[1:])
