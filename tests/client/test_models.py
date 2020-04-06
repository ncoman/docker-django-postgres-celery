import pytest

# Connects our tests with our database
from client.models import Client

pytestmark = pytest.mark.django_db


@pytest.mark.django_db(transaction=True)
class TestModels:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
            usually contains tests).
        """
        print(f"\r==================SetUp Class: {cls.__name__}\r")
        # for k, v in cls.__dict__.items():
        #     print(k, v)

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
            setup_class.
        """
        print(f"\r==================TearDown Class: {cls.__name__}\r")

    @classmethod
    def setup_method(cls, method):
        print(f"\r==================SetUp method: {method.__name__}\r")

    @classmethod
    def teardown_method(cls, method):
        print(f"\r==================TearDown method: {method.__name__}\r")

    def test_model_client(self, client):
        print(client.__dict__, type(client.name))
        assert "client_name" == client.name
        assert "key" == client.key
        assert str(type(client.name)) in ("<class 'str'>", "class 'str'")

    def test_client___str__(self):
        obj = Client.objects.create(name="client_name", key="key")
        assert obj.__str__() == "client_name, None, key"

    def test_client_verbose_name_plural(self, client):
        assert str(client._meta.verbose_name_plural) == "clients"
