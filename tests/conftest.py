import pytest
from mixer.backend.django import mixer
from django.conf import settings

"""
Sharing fixtures
pytest encourages you to write them in a special file called conftest.py. 
Sharing fixtures is then as easy as writing a function, decorate it with @pytest.
fixture and then pass it as parameter to whatever function needs it.

By default fixtures have a scope of “function” 
(meaning the database will be opened and then closed for each test function), 
but you can chose to have a “module scope” or even a “session scope”.

You can even have fixtures that are always implicitly called, by using autouse=True in the fixture definition.
"""



def pytest_configure(config):
    settings.NPLUSONE_RAISE = True


@pytest.fixture
def client():
    print("\r================security fixture======================\r")
    return mixer.blend('client.Client', name="client_name", key="key")

