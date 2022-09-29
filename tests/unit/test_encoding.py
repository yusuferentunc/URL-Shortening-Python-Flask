from main import encoding


def test_encode_with_id():
    test_id = 52223117
    code = encoding(test_id)
    assert code == 'http://short.est/v3bm5'


def test_encode_with_zero_id():
    test_id = 0
    code = encoding(test_id)
    assert code is None


def test_encode_with_wrong_input():
    test_id = 'irrelavant input'
    code = encoding(test_id)
    assert code is None
