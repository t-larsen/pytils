"""
Script/module to support easy execution of multiple scripts

"""

import os
import multiprocessing as mp


def _validate_input(path, headname):
    """Validates the input variables used for several functions.

    Args:
        *path* (str): Relative path to the directory containing the
        scripts to be executed.

        *headname* (str): Common name for the scripts to be executed.
        This can for example be 'case' when the script files are
        named 'case1.py', 'case2.py', 'case3.py' and 'case4.py'.
        It is assumed that the extension for all scripts is '.py'.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *path* is not an existing directory.

        **ValueError** if *headname* is not a str.

    """
    if not os.path.isdir(path):
        st = 'Path ({!r}) is not a directory.'.format(path)
        raise ValueError(st)
    if not type(headname) == str:
        st = 'Headname ({!r}) is not of type str.'.format(headname)
        raise ValueError(sr)


def _script_commands(path='./', headname='case'):
    """Form a tuple of all required script commands.

    Args:
        *path* (str): Relative path to the directory containing the
        scripts to be executed.

        *headname* (str): Common name for the scripts to be executed.
        This can for example be 'case' when the script files are
        named 'case1.py', 'case2.py', 'case3.py' and 'case4.py'.
        It is assumed that the extension for all scripts is '.py'.

    Returns:
        *script_commands* (tuple): Tuple of commands to execute all
        the relevant scripts. The commands are str types.

    Raises:
        **ValueError** if *path* is not an existing directory.

        **ValueError** if *headname* is not a str.

    """
    _validate_input(path, headname)

    # Determine tuple of relevant script commands
    script_commands = ()
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            # Extract filename head and extension
            ext_name = os.path.splitext(filename)[1][1:].strip().lower()
            head_name = filename[:len(headname)]
            if head_name == headname and ext_name == 'py':
                cmd = "cd {0}; python {1}".format(path, filename)
                script_commands += (cmd, )

    return script_commands


def run_seq(path='./', headname='case'):
    """Sequential execution of all relevant script-files.

    Args:
        *path* (str): Relative path to the directory containing the
        scripts to be executed.

        *headname* (str): Common name for the scripts to be executed.
        This can for example be 'case' when the script files are
        named 'case1.py', 'case2.py', 'case3.py' and 'case4.py'.
        It is assumed that the extension for all scripts is '.py'.

    Returns:
        Nothing.

    Raises:
        **ValueError** if *path* is not an existing directory.

        **ValueError** if *headname* is not a str.

        **ValueError** if no scripts comply with the conditions.

    """
    _validate_input(path, headname)
    script_commands = _script_commands(path, headname)
    if not len(script_commands) > 0:
        raise ValueError('No valid script files.')
    map(os.system, script_commands)

    return len(script_commands)


def run_par(path='./', headname='case', cores='max'):
    """Parallel execution of all relevant script-files (independent).

    Args:
        *path* (str): Relative path to the directory containing the
        scripts to be executed.

        *headname* (str): Common name for the scripts to be executed.
        This can for example be 'case' when the script files are
        named 'case1.py', 'case2.py', 'case3.py' and 'case4.py'.
        It is assumed that the extension for all scripts is '.py'.

        *cores* (int, 'max'): Number of cores allocated for the
        parallel processing of the scripts.

    Returns:
        Nothing.

    Raises:
        **ValueError** if only singe-core processor available.

        **ValueError** if *path* is not an existing directory.

        **ValueError** if *headname* is not a str.

        **ValueError** if *cores* not in valid range.

    """
    # Validate input
    if not mp.cpu_count() > 1:
        raise ValueError('No multi-core functionality available.')
    _validate_input(path, headname)
    if not cores == 'max' or cores in (int, float):
        raise ValueError('Cores ({!r}) incorrectly specified.')
    if cores in (int, float) and not 0 < cores <= mp.cpu_count():
        raise ValueError('Cores chosen badly.')

    # Extract
    script_commands = _script_commands(path, headname)

    # Execute scripts
    if cores == 'max':
        processes = mp.cpu_count()
    else:
        processes = int(cores)
    pool = mp.Pool(processes)
    pool.map(os.system, script_commands)
    pool.close()
    pool.join()

    return len(script_commands)


if __name__ == "__main__":
    (path, headname, cores) = ('./cases', 'case', 'max')
    run_par(path, headname, cores)
