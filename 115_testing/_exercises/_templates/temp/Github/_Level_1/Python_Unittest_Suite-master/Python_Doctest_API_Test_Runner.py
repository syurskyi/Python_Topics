# Python Doctest API
# The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work
# exactly as shown.
#
#  There are several common ways to use doctest:
# > To check that a module�s docstrings are up-to-date by verifying that all interactive examples still work as documented.
# > To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
# > To write tutorial documentation for a package, liberally illustrated with input-output examples.
#   Depending on whether the examples or the expository text are emphasized, this has the flavor of �literate testing� or �executable documentation�.
#
 
#
# Test Runner:
#
# When you have placed your tests in a module, the module can itself be the test runner.
# When a test fails, you can arrange for your test runner to re-run only the failing doctest while you debug the problem.
#
# Here is a minimal example of such a test runner:
# 

__ _____ __ _____
    ______ doctest

    flags _ doctest.REPORT_NDIFF|doctest.FAIL_FAST

    __ le.(___.argv) > 1:
        name _ ___.argv[1]

        __ name __ globals(
            obj _ globals()[name]

        ____:
            obj _ __test__[name]

        doctest.run_docstring_examples(obj, globals(), name_name,
                                       optionflags_flags)
    ____:
        fail, total _ doctest.testmod(optionflags_flags)

        print("{} failures out of {} tests".f..(fail, total))
