"""
When running this file as a script it can be done in the following
ways:

.. code-block:: python

   $ python full.py
   $ python full.py -q
   $ python full.py -v
   $ python full.py DIRECTORY -q
   $ python full.py DIRECTORY -v
   $ python full.py DIRECTORY LOGFILE -q
   $ python full.py DIRECTORY LOGFILE -v

where DIRECTORY is the directory from where a full test is conducted
including all sub-directories and files with extensions '.py' and '.dt';
LOGFILE is the name of a file in which to store logging information.
DIRECTORY must not be absolute (i.e. not begin with '/') and it must
separate segments by '/' (such as './subdir1/subdir2').

An example of the content of a logging file can be.

.. code-block:: python

   *************************************************************************
   Date and time: 12:55PM on June 14, 2014
   Python version: 2.7.7 |Anaconda 2.0.0 (x86_64)|
   (default, Jun  2 2014, 12:48:16) [GCC 4.0.1 (Apple Inc. build 5493)]
   Number of CPU cores: 2
   Physical memory [MiB]: 8192
   Used physical memory [MiB]: 3921
   *************************************************************************
   =========================================================================
   W .//run_full_doctest.py                    Succeeded:    0, Failed:    0
   W ./.backup/run_full_doctest.py             Succeeded:    0, Failed:    0
   W ./.backup/run_single_doctest.py           Succeeded:    0, Failed:    0
   W ./doc/source/conf.py                      Succeeded:    0, Failed:    0
   W ./examples/.../run_all_scripts.py         Succeeded:    0, Failed:    0
   W ./examples/.../cases/case1.py             Succeeded:    0, Failed:    0
   W ./examples/.../cases/case2.py             Succeeded:    0, Failed:    0
   W ./examples/.../cases/case3.py             Succeeded:    0, Failed:    0
   W ./examples/.../cases/case4.py             Succeeded:    0, Failed:    0
   W ./pytils/launchers/doctests.py            Succeeded:    0, Failed:    0
   W ./pytils/launchers/doctests_bu01.py       Succeeded:    0, Failed:    0
   W ./pytils/launchers/doctests_bu02.py       Succeeded:    0, Failed:    0
   W ./pytils/launchers/scripts.py             Succeeded:    0, Failed:    0
   P ./test/pytils/.../test_doctests_pep8.dt   Succeeded:    3, Failed:    0
   P ./test/pytils/.../test_scripts_pep8.dt    Succeeded:    3, Failed:    0
   P ./test/pytils/.../test_scripts_raise.dt   Succeeded:   20, Failed:    0
   =========================================================================
   Accumulated                                 Succeeded:   26, Failed:    0
   =========================================================================

"""

import doctest
import os
import sys
import psutil
import datetime

import _validate


def _commands(path):
    """Form a tuple of all required test files.

    Args:
        *path* (str): Relative path to the directory containing the
        scripts to be executed.

    Returns:
        *file_names* (tuple): Tuple of commands to execute all
        the relevant scripts. The commands are str types.

    Raises:
        **ValueError** if *path* is not an existing directory.

        **ValueError** if *headname* is not a str.

    """
    # _validate._dir_exists(path)

    # Files not included in the test
    OMIT_FILES = ('full.py', '__init__.py')

    file_names = ()
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            # Extract filename extension
            ext_name = os.path.splitext(filename)[1][1:].strip().lower()

            # Perform doctest for all relevant .py and .dt files
            go = filename not in OMIT_FILES
            if ext_name in ('py', 'dt') and go:
                full_filename = os.sep.join([dirpath, filename])
                file_names += (full_filename, )

    return file_names


def _create_info_str(filename, failed, succeeded):
    """Creates a single line for logging with doctest information.

    This function creates a single line per call for the results of
    a performed doctest::

        status   filename              F: failed, S: succeeded

    where *status* can be any one of W/F/S (Warning, Failed, Succeeded),
    *filename* is the name of the doctested file, *failed* indicates
    the number of failed tests in the file *filename*, and *succeeded*
    indicates the number of passed tests in the file *filename*. A
    line such as this one is made for each doctested file and the
    information is contained as part of the logging.

    Args:
        *filename* (str): Name of tested file.

        *failed* (int): Number of failed doctests in the file
        *filename*.

        *succeeded* (int): Number of succeeded doctests in the file
        *filename*.

    Return:
        *file_result* (str): A str (line) of results for the doctest
        performed on the file *filename*. The line contains 1) a single
        letter indicating status (W: Warning; F: Failed; S: Succeeded);
        2) the *filename*; 3) number of failed tests in the file
        *filename*; and 4) number of succeeded tests in the file
        *filename*. A 'W' (Warning) status is given is no tests have
        been performed in the file *filename*. An 'F' (Failed) is
        indicated as status of just a single failed test is observed.
        A 'P' (Pass) status is only given if at least one test has
        been performed and that **all** tests were passed.

    Raises:
        IOError raised if *filename* is not a file.

        TypeError raised if *failed* and *succeeded* are not integers.

        ValueError raised if *failed* and *succeeded* are not positive
        (zero included).

    """
    # Validate input
    # _validate._file_exists(filename)
    # _validate._positive0_int(failed)
    # _validate._positive0_int(succeeded)

    # Determine status
    tests = failed + succeeded
    if tests == 0:
        status = 'W'
    elif tests > 0 and failed == 0:
        status = 'P'
    else:
        status = 'F'

    # Build result str (cut full filename to max. 60 characters)
    st1 = '{0} {1:<63} '.format(status, filename[-60:])
    st2 = 'S: {0:>3}, F: {1:>3}'.format(succeeded, failed)
    file_result = '{0}{1}\n'.format(st1, st2)

    return file_result


def _log_results(logfile, results, stats):
    """Logging of major results from doctest.

    This function controls the logging of results when performing
    doctests with the :py:func:`pytils.launchers.doctests.run` function.
    The logging provides to types of information:

    1. General information such as date, time, computer system etc.
    2. Results of the doctests with filename and failed/succeeded tests.

    The information is logged to a file. If the filename already exists
    an error is raised and the user needs to remove the 'old' file.

    Args:
        *logfile* (str): Name of file in which the result of the logging
        is stored. The logfile contains different types of information:
        1) system relevant information; 2) a line for each doctest'ed
        file indicating W/F/S (W: Warning, F: Fail, S: Success) for the
        given test, the name of the doctest file, and number of failed
        passed tests. After all the individual doctests an accumulative
        number of passed and failed tests are shown.

        *results* (list): A list of strings where each item is one line
        describing the result of the doctest of a single testfile.

        *stats* (dict): A dictionary indicating stats['failed'] and
        stats['succeeded'] tests seen overall.

    Returns:
        Nothing - but it stores the logging information in the file
        *logfile*.

    Raises:
        Nothing.

    """
    # Validate input
    # _validate._logfile(logfile)
    # _validate._list_str(results)
    # _validate._dict_keys(stats, ['failed', 'succeeded'])

    with open(logfile, "w") as f:
        # Data
        f.write('{0}\n'.format(80*'*'))
        now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        f.write('Time & date: {0}\n'.format(now))
        f.write('Current directory: {0}\n'.format(os.getcwd()))
        f.write('Python version: {0}\n'.format(sys.version))
        cores = psutil.cpu_count(logical=False)
        f.write('Number of CPU cores: {0}\n'.format(cores))
        phys_mem_mb = psutil.TOTAL_PHYMEM/2**20
        f.write('Physical memory [MiB]: {0}\n'.format(phys_mem_mb))
        avail_phy_mem_mb = psutil.avail_phymem()/2**20
        f.write('Used physical memory [MiB]: {0}\n'.format(avail_phy_mem_mb))
        f.write('{0}\n'.format(80*'*'))

        # Results for each file doctest
        f.write('{0}\n'.format(80*'='))
        for line in results:
            f.write(line)
        f.write('{0}\n'.format(80*'='))

        # Accumulated result
        st1 = 'S: {0:>3}'.format(stats['succeeded'])
        st2 = 'F: {0:>3}'.format(stats['failed'])
        st = '{0:<65} {1}, {2}\n'.format('Accumulated', st1, st2)
        f.write(st)
        f.write('{0}\n'.format(80*'='))


def run(path='./', logfile=False, verbose='-q'):
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

        *logfile* (str, False): If high-level logging is requested
        a (unexisting) filename must be specified.

        *verbose* (str): Verbose level where '-v' indicates detailed
        test information is printed, and '-q' means quiet mode where
        only failed tests are reported.

    Returns:
        Nothing.

    Raises:
        **ValueError** if the specified directory does not exist.

        **ValueError** if verbose level is incorrectly specified.

    """

    # Determine tuple of test filenames
    filenames = _commands(path)
    if len(filenames) == 0:
        raise ValueError('No files containing doctests.')

    # Perform test
    count = 0
    results = []
    stats = {'succeeded': 0, 'failed': 0}
    if len(filenames) > 0:
        print('{0}'.format(80*'='))
    for filename in filenames:
        count += 1
        if verbose in ('-v', '-V'):
            print('{0:>80}'.format(filename))
            t = doctest.testfile(filename, module_relative=False)
            print('{0}'.format(80*'='))
        else:
            t = doctest.testfile(filename, module_relative=False)

        # Logging info
        st = _create_info_str(filename, t.failed, t.attempted-t.failed)
        results.append(st)
        stats['succeeded'] += t.attempted - t.failed
        stats['failed'] += t.failed

    if type(logfile) == str:
        _log_results(logfile, results, stats)


if __name__ == "__main__":
    (PATH, LOGFILE, VERBOSE) = ('./', 'doctest.log', '-q')
    if len(sys.argv) > 1:
        VERBOSE = sys.argv[-1]
    if len(sys.argv) > 2:
        PATH = sys.argv[1]
    if len(sys.argv) > 3:
        LOGFILE = sys.argv[2]
    run(path=PATH, logfile=LOGFILE, verbose=VERBOSE)
