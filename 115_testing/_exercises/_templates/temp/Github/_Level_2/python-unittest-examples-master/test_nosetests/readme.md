This document will explain things that cannot be explained in the sample code.

nose plugins
============

AllModules
----------
type 'nosetests --all-modules' to enable collection and execution of tests in all python modules.

Attrib
------
A plugin to let you only execute the tests you want. Take a look at the sample code test_attrib_04.

Capture
-------
This plugin captures stdout during test execution. It is enabled by default but can be disabled with the options -s or --nocapture.

Collect
-------
This plugin bypasses the actual execution of tests, and instead just collects test names. 
Type 'nosetests -v --collect-only --with-id' to get the list of all test cases and indexes.

Cover
-----
To generate code coverage report.

Debug
-----
This plugin provides --pdb and --pdb-failures options. The --pdb option will drop the test runner into pdb when it encounters an error. To drop into pdb on failure, use --pdb-failures.

Type 'nosetests --pdb-failure hidden_examples_03.py' to see how it works.

Deprecated
----------
This plugin installs a DEPRECATED error class for the DeprecatedTest exception. Type 'nosetests -v' and notice the result of the test case in test_deprecated_plugin_06.py file.

Doctests
--------
Use the Doctest plugin with --with-doctest to enable collection and execution of doctests. Because doctests are usually included in the tested package, nose only looks for them in the non-test packages it discovers in the working directory.

Type 'nosetests -v --with-doctest' and see the result.

Failure Detail
--------------
This plugin provides assert introspection. When the plugin is enabled and a test failure occurs, the traceback is displayed with extra context around the line in which the exception was raised.

Isolate
-------
The isolation plugin resets the contents of sys.modules after running each test module or package. This plugin should not be used in conjunction with other plugins that assume that modules, once imported, will stay imported; for instance, it may cause very odd results when used with the coverage plugin.

Logcapture
----------
This plugin captures logging statements issued during test execution. It is enabled by default but can be turned off with the option --nologcapture.

Multiprocess
------------
The multiprocess plugin enables you to distribute your test run among a set of worker processes that run tests in parallel.

Type 'nosetests --processes=2' to run test cases in two processes.


Prof
----
This plugin will run tests using the hotshot profiler, which is part of the standard library. Now I only know this plugin relates to performance profiling.


Skip
----
This plugin installs a SKIP error class for the SkipTest exception. When SkipTest is raised, the exception will be logged in the skipped attribute of the result, ‘S’ or ‘SKIP’ (verbose) will be output, and the exception will not be counted as an error or failure. This plugin is enabled by default but may be disabled with the --no-skip option.

See the result of test_deprecated_plugin_06.py

Testid
------
This plugin adds a test id (like #1) to each test name output.

Type 'nosetests -v --with-id' to see the result.

Xunit
-----
It’s designed for the Jenkins (previously Hudson) continuous build system, but will probably work for anything else that understands an XUnit-formatted XML representation of test results.

Type 'nosetests --with-xunit' to see the result.

Setuptools integration
======================
nose may be used with the setuptools test command. Simply specify nose.collector as the test suite in your setup file:

    setup (
        # ...
        test_suite = 'nose.collector'
    )

Then to find and run tests, you can run:

    python setup.py test
