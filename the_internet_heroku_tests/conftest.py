import pytest
from the_internet.herokuInternet import HerokuApp


@pytest.fixture
def herokuapp(py):
    _herokuapp = HerokuApp(py)

    return _herokuapp
