scripts
=======
This sub-package includes modules (which can also run as scripts) to
assist a developer in ensuring that all doctests in a package are
executed. The functions are based on doctests included in '.py' or
'.dt' files:

#. The '.py' type of files typically includes relevant examples, which
   assists in actual typical use-cases. These both serves as a direct
   help to the user on how to use the functions but also serves a
   partial testing framework.
#. The '.dt' type of files are used for some special doctests, which
   for example can be to test functionality against an 'oracle'
   (a known correct result to a specific problem).

.. include:: ../../../../pytils/launchers/scripts.py
   :start-after: """
   :end-before: """


Functions
---------

.. autofunction:: pytils.launchers.scripts._validate_input

.. autofunction:: pytils.launchers.scripts._script_commands

.. autofunction:: pytils.launchers.scripts.run_seq

.. autofunction:: pytils.launchers.scripts.run_par


Code
----

.. literalinclude:: ../../../../pytils/launchers/scripts.py



Test
----

PEP8
++++


