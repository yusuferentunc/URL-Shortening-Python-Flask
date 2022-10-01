from main import decoding


def test_decode_with_url():
    """Test decode function in normal behaviour"""
    code = 'v3bm5'
    code_id = decoding(code)
    assert code_id == 52223117


def test_decode_with_empty_code():
    """Test decode function with empty string/code"""
    code = ''
    code_id = decoding(code)
    assert code_id == 0


def test_decode_with_wrong_input():
    """Test decode function with input that is in wrong format"""
    code = 1234
    code_id = decoding(code)
    assert code_id is None
