# an example of doing tests without unit test syntax
# pytest will run this just fine

from lambdata.my_mod import Helper

helper = Helper()


def test_enlarge():
    assert helper.enlarge(5) == 500
