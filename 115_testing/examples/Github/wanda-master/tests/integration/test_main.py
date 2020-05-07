from pytest import mark
from unittest import TestCase

from wanda import config


@mark.dev
def test_parameter_dev_profile():
    assert config.config['parameter'] == 'dev-value'


@mark.usefixtures('local_config')
@mark.usefixtures('monkeypatch2')
class TestMain_Local(TestCase):

    @mark.local
    def test_parameter_local_profile(self):
        self.monkeypatch2.setattr(config, 'config', self.local_config)

        assert config.config['parameter'] == 'local-value'
