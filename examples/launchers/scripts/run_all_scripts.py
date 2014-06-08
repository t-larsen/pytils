"""
This script demonstrates the use of 'pytils.launchers.scripts.run_par'
to perform the four case scripts in the directory './cases' by using
the parallel processing of the :py:mod:`multiprocessing` package.

"""

import pytils

(path, headname, extension, cores) = ('./cases', 'case', 'py', 'max')
pytils.launchers.scripts.run_par(path, headname, extension, cores)
