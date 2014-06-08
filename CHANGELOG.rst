
0.0.1 (04-JUN-2014)
+++++++++++++++++++

- **pytils.dtest**: Changed the dtest scripts to be modules that can be
  used as both scripts and for import. Small modifications to the code
  was included such as inclusion of docstrings, catching invalid user
  input etc. Doctests also implemented.

0.0.1 (06-JUN-2014)
+++++++++++++++++++

- 'pytils.dtest' Modified the call to doctest.testfile to set
  module_relative=False. This means that directories for test are
  specified.
- Directory 'pytils/launchers' created where the earlier 'pytils.dtest'
  has been renamed to 'pytils.launchers.doctests'.
- File 'pytils.launchers.scripts' added. This supports running a
  collection of scripts by calling just one script.
