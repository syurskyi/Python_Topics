____ setuptools ______ setup, find_packages
______ sys
sys.pa__.append('./src')
sys.pa__.append('./test')

setup(
    name _ "Sample",
    version _ "1.0",
    packages _ find_packages(),
    test_suite _ 'sample_test.suite'
)