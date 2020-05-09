______ __
______ u__
____ u__ ______ TestCase


c_ TestMyObject(TestCase
    """
    Showcase for different ways to skip test
    Keep in mind that there are only few scenarios where skipping tests is reasonable
    Do not skip a test just because it is not running, rather fix it
    """

    # a good example how skipping tests should not be done
    @u__.skip('there should be no skipped tests')
    ___ test_will_never_run
        aE..(2, 1)

    # can be used to skip test on a specific environment or an certain OS
    @u__.skipUnless(__.getenv('DEV_STAGE'), 'Only running on dev stage')
    ___ test_skip_with_condition
        aE..(3, 4)
