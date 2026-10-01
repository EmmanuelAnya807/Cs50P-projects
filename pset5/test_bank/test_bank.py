from bank import value


def test_greeting_starting_with_hello():
    # Test strings starting with "hello" (case-insensitive, handling symbols/spaces)
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello1.") == 0
    assert value(" hello") == 0


def test_greeting_starting_with_h():
    # Test strings starting with "h" but not "hello" (case-insensitive, handling symbols/spaces)
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("HI1.") == 20
    assert value(" hi") == 20


def test_greeting_starting_with_other():
    # Test strings that do not start with "h" or "hello" at all
    assert value("Good Morning") == 100
    assert value("GOOD MORNING") == 100
    assert value("1") == 100
    assert value(".") == 100
    assert value("") == 100
    assert value(" ") == 100
