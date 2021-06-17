from gh_action_demo.app import test
import geocoder


def test_data():
    current_location = geocoder.ip('me')
    return current_location.geojson


def test_index():
    assert test() == test_data()
