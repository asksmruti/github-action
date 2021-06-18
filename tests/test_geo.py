from gh_action_demo.app import test, home
import geocoder
import pytest


def test_data():
    current_location = geocoder.ip('me')
    return current_location.geojson


def test_health_check():
    assert test() == test_data()


@pytest.mark.xfail()
def test_home():
    assert home() != test_data()
