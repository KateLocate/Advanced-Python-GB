import sys
sys.path.append('..')
from server import get_server_response


TEST_REQUEST = {'action': 'lower_text', 'data': 'DaTa+/-.'}
ASSERT_REQUEST = 'data+/-.'


def test_server_response():
    assert get_server_response(TEST_REQUEST) == ASSERT_REQUEST
