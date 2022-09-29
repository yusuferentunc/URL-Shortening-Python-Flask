from app import decoding


def test_decode_with_url():
    code = 'v3bm5'
    code_id = decoding(code)
    assert code_id == 52223117


def test_decode_with_empty_code():
    code = ''
    code_id = decoding(code)
    assert code_id == 0


def test_decode_with_wrong_input():
    code = 1234
    code_id = decoding(code)
    assert code_id is None