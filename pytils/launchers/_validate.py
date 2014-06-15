"""
The purpose of this module is to provide validation of the input
provided to the functions in the :py:mod:`pytils.launchers.doctests`
module.

"""

import doctest
import inspect
import numpy as np
import os
import sys


def _dir_exists(idir):
    """Validates the *idir* directory exists.

    Args:
        *idir* (str): Relative path for the input directory.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *idir* is not an existing directory.

    """
    if not os.path.isdir(idir):
        caller = inspect.stack()[1][3]
        st1 = 'Specified directory ({0}'.format(caller)
        st2 = '{!r}) does not exist.'.format(idir)
        raise ValueError('{0}::{1}'.format(st1, st2))


def _verbose(verbose):
    """Validates the *verbose* variable and raises error if necessary.

    Args:
        *verbose* (str): Verbose level where '-v' or '-V' indicate
        detailed test information is printed, and '-q' or '-Q' mean
        quiet mode where only failed tests are reported.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *path* is not an existing directory.

        **ValueError** if *verbose* level is incorrectly specified.

    """
    if verbose not in ('-v', '-V', '-q', '-Q'):
        caller = inspect.stack()[1][3]
        st1 = 'Verbose level ({0}'.format(caller)
        st2 = '{!r}) incorrectly specified.'.format(verbose)
        raise ValueError('{0}::{1}'.format(st1, st2))


def _file_exists(filename):
    """Validates *filename* exists.

    Args:
        *filename* (str): Filename ...

    Returns:
        Nothing.

    Raises:
        **IOError** if *filename* is not a file.

    """
    if not type(filename) == str:
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) must be a str.'.format(filename)
        raise TypeError('{0}::{1}'.format(st1, st2))
    if not os.path.isfile(filename):
        caller = inspect.stack()[1][3]
        st1 = 'File ({0}'.format(caller)
        st2 = '{!r}) does not exist.'.format(filename)
        raise IOError('{0}::{1}'.format(st1, st2))


def _not_exists(name):
    """Validates *filename* does not exists (dir or file).

    Args:
        *filename* (str): Variable tested for existence as either
        a directory or as a file.

    Returns:
        Nothing.

    Raises:
        **IOError** if *filename* already exists as file or directory.

    """
    if not type(name) == str:
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) must be a str.'.format(name)
        raise TypeError('{0}::{1}'.format(st1, st2))
    if os.path.exists(name):
        caller = inspect.stack()[1][3]
        st1 = 'File or directory ({0}'.format(caller)
        st2 = '{!r}) already exists.'.format(name)
        raise IOError('{0}::{1}'.format(st1, st2))


def _positive0_int(var):
    """Validates *var* is positive int and raises error if necessary.

    Args:
        *var* (int): Input variable which is supposed to be an int.

    Returns:
        Nothing.

    Raises:
        **TypeError** if *var* is not an int.

        **ValueError** if *var* is not positive (zero included).

    """
    np_ints = (np.int8, np.int16, np.int32, np.int64)
    np_uints = (np.uint8, np.uint16, np.uint32, np.uint64)
    if not type(var) in (int, long) + np_ints + np_uints:
        caller = inspect.stack()[1][3]
        st1 = 'Variable ({0}'.format(caller)
        st2 = '{!r}) must be an int.'.format(var)
        raise TypeError('{0}::{1}'.format(st1, st2))
    if not var >= 0:
        caller = inspect.stack()[1][3]
        st1 = 'Variable ({0}'.format(caller)
        st2 = '{!r}) must be positive.'.format(var)
        raise TypeError('{0}::{1}'.format(st1, st2))


def _logfile(logfilename=None):
    """Validates *logfilename* and raises error if necessary.

    Args:
        *logfilename* (str): Name of the logfile. Default is
        None in which case logging is not performed.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *logfilename* is not None or a str.

        **ValueError** if *logfilename* already exists.

    """
    if logfilename is not None:
        if not type(logfilename) == str:
            caller = inspect.stack()[1][3]
            st1 = 'Logfile ({0}'.format(caller)
            st2 = '{!r}) invalid (must be str or None).'.format(logfilename)
            raise ValueError('{0}::{1}'.format(st1, st2))
        if os.path.exists(logfilename):
            caller = inspect.stack()[1][3]
            st1 = 'Logfile ({0}'.format(caller)
            st2 = '{!r}) already exists.'.format(logfilename)
            raise ValueError('{0}::{1}'.format(st1, st2))


def _list_str(lst):
    """Validates *lst* and raises error if necessary.

    Args:
        *lst* (str): List of strings each describing the doctest of a
        given doctest file. All list items are of type str, the first
        character is W, F or S, and all items are of identical length.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *lst* is not None or a str.

        **ValueError** if *lst* already exists.

    """
    if not type(lst) == list:
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) must be a list.'.format(lst)
        raise ValueError('{0}::{1}'.format(st1, st2))
    if not all(isinstance(item, str) for item in lst):
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) list members must all be str.'.format(lst)
        raise ValueError('{0}::{1}'.format(st1, st2))
    for item in lst:
        if len(item) != len(lst[0]) or item[0] not in ('W', 'F', 'S'):
            caller = inspect.stack()[1][3]
            st1 = 'Input list ({0}'.format(caller)
            st2 = '{!r}) have invalid members.'.format(lst)
            raise ValueError('{0}::{1}'.format(st1, st2))


def _dict_keys(idict, keylist):
    """Validates *idict* matches with specified *keylist*.

    Args:
        *idict* (dist): Input dictionary which is checked for correctness.

        *keylist* (list): A list of str keys that **must** be present in
        the *idict* dictionary.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *logfilename* is not None or a str.

        **ValueError** if *logfilename* already exists.

    """
    if not type(keylist) == list:
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) must be a list.'.format(keylist)
        raise TypeError('{0}::{1}'.format(st1, st2))
    if not all(isinstance(item, str) for item in keylist):
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) list members must all be str.'.format(keylist)
        raise ValueError('{0}::{1}'.format(st1, st2))
    if not type(idict) == dict:
        caller = inspect.stack()[1][3]
        st1 = 'Input ({0}'.format(caller)
        st2 = '{!r}) must be a dictionary.'.format(idict)
        raise TypeError('{0}::{1}'.format(st1, st2))
    for item in keylist:
        if item not in idict.keys():
            caller = inspect.stack()[1][3]
            st1 = 'Keylist ({0}'.format(caller)
            st2 = '{!r}) contains invalid key(s).'.format(keylist)
            raise ValueError('{0}::{1}'.format(st1, st2))
