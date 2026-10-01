from um import count


def test_case_insensitivity():
    """Ensure count matching is case-insensitive for lower and upper case."""
    assert count('um') == 1
    assert count('UM') == 1


def test_with_trailing_whitespaces():
    """Ensure 'um' surrounded by leading or trailing spaces is counted."""
    assert count(' um ') == 1


def test_with_punctuation():
    """Ensure 'um' enclosed by or adjacent to punctuation is correctly matched."""
    assert count('(um)') == 1
    assert count('(um...') == 1


def test_multiple_occurences():
    """Ensure multiple valid instances of 'um' in a single string are counted."""
    assert count('um, hello, um, world') == 2
    assert count('Um, thanks, um...') == 2


def test_invalid_input():
    """Ensure substring matches inside other words are ignored."""
    assert count('yummy') == 0
    assert count('Aluminium is umbearable') == 0


def test_number_input():
    """Ensure digits and alphanumeric combinations without word boundaries return 0."""
    assert count('1') == 0
    assert count('1um') == 0


def test_whitespace():
    """Ensure strings containing only whitespace characters return 0."""
    assert count(' ') == 0
    assert count('  ') == 0


def test_no_input():
    """Ensure an empty string input returns 0."""
    assert count('') == 0


def test_underscore():
    """Ensure underscores act as word characters and prevent word boundary matching."""
    assert count('-um_,') == 0
    assert count('_um') == 0
    assert count('y_um_my') == 0
