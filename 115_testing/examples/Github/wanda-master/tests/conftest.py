from pytest import fixture


@fixture(scope='class')
def monkeypatch2(request):
    from _pytest.monkeypatch import MonkeyPatch
    mp = MonkeyPatch()

    def fin():
        mp.undo()

    request.addfinalizer(fin)
    request.cls.monkeypatch2 = mp


@fixture(scope='class')
def local_config(request):
    '''
    pulls the local configuration from an environment variable file.
    intended to be a stop-gap before porting the local mysql integration
      tests into integration tests that can execute idempotently in the dev
      environment.  only for tests marked 'local'.
    note that regular dev environment integration test simply use pyutils
      config library to pull parameters directly from SSM, so a fixture is not
      required for those tests marked 'dev'.
    '''
    import os
    from os.path import join, dirname
    from dotenv import load_dotenv
    envpath = join(dirname(__file__), '.local.env')

    if os.path.isfile(envpath):
        load_dotenv(envpath)
    else:
        raise EnvironmentError(
            f'executing local integration tests requires: {envpath}')

    local_config = {
        'parameter': os.getenv('PARAMETER'),
    }

    request.cls.local_config = local_config
