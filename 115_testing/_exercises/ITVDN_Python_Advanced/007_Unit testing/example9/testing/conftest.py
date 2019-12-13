import pytest
from models import User


@pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='function')
# @pytest.fixture
def user():
    return User(
        email='test@example.com',
        first_name='test1',
        last_name='test2',
        fixture=True
    )
