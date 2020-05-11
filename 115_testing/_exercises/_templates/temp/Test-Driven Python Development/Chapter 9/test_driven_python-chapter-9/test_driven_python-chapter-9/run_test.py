_____ u__


c_ AttribLoader(u__.TestLoader):
    ___  -  attrib):
        attrib = attrib

    ___ loadTestsFromModule module, use_load_tests=False):
        return super().loadTestsFromModule(module, use_load_tests=False)

    ___ getTestCaseNames testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        filtered_test_names = [test
                               for test in test_names
                               if hasattr(getattr(testCaseClass, test),
                                          attrib)]
        return filtered_test_names


if __name__ == "__main__":
    loader = AttribLoader("slow")
    test_suite = loader.discover(".")
    runner = u__.TextTestRunner()
    runner.run(test_suite)
