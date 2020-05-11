_____ u__


c_ AttribLoader(u__.TestLoader):
    ___  -  attrib):
        attrib = attrib

    ___ loadTestsFromModule module, use_load_tests=F..):
        r_ s__().loadTestsFromModule(module, use_load_tests=F..)

    ___ getTestCaseNames testCaseClass):
        test_names = s__().getTestCaseNames(testCaseClass)
        filtered_test_names = [test
                               ___ test __ test_names
                               __ hasattr(getattr(testCaseClass, test),
                                          attrib)]
        r_ filtered_test_names


__ __name__ == "__main__":
    loader = AttribLoader("slow")
    test_suite = loader.discover(".")
    runner = u__.TextTestRunner()
    runner.run(test_suite)
