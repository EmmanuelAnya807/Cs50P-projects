from test_plates.plates import is_valid


def test_valid_two_letter_start():
    # Verify plates starting with at least two letters are valid
    assert is_valid("he")
    assert is_valid("HE")


def test_valid_maximum_length_boundary():
    # Verify plates within the minimum (2) and maximum (6) character limits are valid
    assert is_valid("helloi")
    assert is_valid("HELLOI")


def test_valid_numeric_suffix():
    # Verify plates ending with numbers are valid
    assert is_valid("he4")
    assert is_valid("he40")


def test_invalid_letter_following_number():
    # Verify plates containing letters after numbers are invalid
    assert not is_valid("he4r")


def test_invalid_leading_zero_in_numbers():
    # Verify plates where the first used number is a '0' are invalid
    assert not is_valid("HE04")
    assert not is_valid("HE0")


def test_invalid_punctuation_and_whitespace():
    # Verify plates containing periods, spaces, or punctuation marks are invalid
    assert not is_valid("he ")
    assert not is_valid("HE j")
    assert not is_valid("he?")
    assert not is_valid("HE.")
    assert not is_valid("he!")
    assert not is_valid("HE l")


def test_invalid_length_out_of_bounds():
    # Verify plates shorter than 2 characters or longer than 6 characters are invalid
    assert not is_valid("h")
    assert not is_valid("morning")
    assert not is_valid("")
    assert not is_valid("morning-afternoon-night")


def test_invalid_single_letter_start():
    # Verify plates starting with fewer than two letters are invalid
    assert not is_valid("h23488")
