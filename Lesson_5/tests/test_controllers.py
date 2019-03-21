import sys
sys.path.append('..')
from server.text import get_lower_text, get_upper_text


TEST_TEXT = 'DaTa1-/+'
ASSERT_TEXT_LOW = 'data1-/+'
ASSERT_TEXT_UP = 'DATA1-/+'


def test_get_lower_text():
    assert get_lower_text(TEST_TEXT) == ASSERT_TEXT_LOW


def test_get_upper_text():
    assert get_upper_text(TEST_TEXT) == ASSERT_TEXT_UP
