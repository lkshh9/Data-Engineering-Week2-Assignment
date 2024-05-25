from example import hi, bye, how_are_you
import pytest


@pytest.fixture
def lokesh():
    return {"name": "Lokesh"}


def test_hello(lokesh):
    assert hi(lokesh) == "Hi, Lokesh"


def test_bye(lokesh):
    assert bye(lokesh) == "Bye, Lokesh"


def test_how_are_you(lokesh):
    assert how_are_you(lokesh) == "How are you Lokesh?"
