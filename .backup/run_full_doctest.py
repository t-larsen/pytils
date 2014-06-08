
import doctest
import os
import sys


def full_test(*args):
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
    # Determine path and verbose level
    (path, verbose) = ('./', 'quiet')
    if len(args) > 0 and os.path.exists(args[0]):
        path = args[0]
    if len(args) > 1:
        verbose = args[1]

    # Files not included in the test
    omit_files = ('run_full_doctest.py', 'run_single_doctest.py',
                  '__init__.py')

    # Perform test
    print('{0}'.format(78*'='))
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            # Extract filename extension
            ext_name = os.path.splitext(filename)[1][1:].strip().lower()

            # Perform doctest for all relevant .py and .dt files
            go = filename not in omit_files
            if ext_name in ('py', 'dt') and go:
                full_filename = os.sep.join([dirpath, filename])
                disp_str = "Doctest file:   {0}".format(filename)
                print("{0}\n".format(disp_str))
                doctest.testfile(full_filename)
                print('{0}'.format(78*'='))


if __name__ == "__main__":
    full_test(*sys.argv[1:])
