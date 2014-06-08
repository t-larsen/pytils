"""
When running this file as a script it can be done in the following
ways:

.. code-block:: python

   $ python full.py
   $ python full.py -q
   $ python full.py -v
   $ python full.py DIRECTORY -q
   $ python full.py DIRECTORY -v

where DIRECTORY is the directory from where a full test is conducted
including all sub-directories and files with extensions '.py' and '.dt'.
DIRECTORY must not be absolute (i.e. not begin with '/') and it must
separate segments by '/' (such as './subdir1/subdir2').

"""

import doctest
import os
import sys


def run(path='./', verbose='-q'):
    """Perform full doctest of all relevant .py and .dt files.

    The function performs a doctest of all .py and .dt files located
    in or below either a specified directory or the working directory,
    and it either does so in quiet ('-q') or detailed ('-v') verbose
    level. In '-q' mode only failed tests are listed whereas all
    test details are provided in '-v' mode.

    Args:
        *path* (str): Path of the source directory for which to search
        for doctest containing .py and .dt files. All directories
        below *path* are also searched. If necessary, path segments
        should be separated by '/' and no absolute path should be
        used (i.e. the path may not begin with '/').

        *verbose* (str): Verbose level where '-v' indicates detailed
        test information is printed, and '-q' means quiet mode where
        only failed tests are reported.

    Returns:
        Nothing.

    Raises:
        ValueError if the specified directory does not exist.
        ValueError if verbose level is incorrectly specified.

    """
    # Determine path and verbose level
    if not os.path.isdir(path):
        raise ValueError('Specified directory does not exist.')
    if not verbose in ('-v', '-q'):
        raise ValueError('Verbose level incorrectly specified.')

    # Files not included in the test
    OMIT_FILES = ('full.py', '__init__.py')

    # Perform test
    print('{0}'.format(78*'-'))
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            # Extract filename extension
            ext_name = os.path.splitext(filename)[1][1:].strip().lower()

            # Perform doctest for all relevant .py and .dt files
            go = filename not in OMIT_FILES
            if ext_name in ('py', 'dt') and go:
                full_filename = os.sep.join([dirpath, filename])
                disp_str = "Test-file:   {0}".format(full_filename)
                print("{0}\n".format(disp_str))
                doctest.testfile(full_filename, module_relative=False)
                print('{0}'.format(78*'-'))
    

if __name__ == "__main__":
    (path, verbose) = ('./', '-q')
    if len(sys.argv) > 2:
        path = sys.argv[1]
    if len(sys.argv) > 1:
        verbose = sys.argv[-1]
    run(path=path, verbose=verbose)
