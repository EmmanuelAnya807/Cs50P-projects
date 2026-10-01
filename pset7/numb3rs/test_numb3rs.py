from numb3rs import validate


def test_leading_zeros():
    """Ensure IP addresses with leading zeros in octets are rejected."""
    assert not validate('007.0.0.0')
    assert not validate('255.255.255.001')


def test_invalid_values_within_range():
    """Ensure octets exceeding 255 but having 3 digits are rejected."""
    assert not validate('275.255.255.255')
    assert not validate('300.1.1.1')


def test_valid_inputs():
    """Ensure properly formatted IPv4 addresses are accepted."""
    assert validate('1.1.1.1')
    assert validate('0.0.0.0')
    assert validate('255.255.255.255')


def test_out_of_range_numbers():
    """Ensure octets with more than 3 digits are rejected."""
    assert not validate('3000.1.1.1')


def test_too_many_octets():
    """Ensure addresses with more than four octets are rejected."""
    assert not validate('1.1.1.1.1')


def test_too_few_octets():
    """Ensure addresses with fewer than four octets are rejected."""
    assert not validate('1.1.1')


def test_non_numeric():
    """Ensure inputs with alphabetic, special, or missing characters are rejected."""
    assert not validate('cat')
    assert not validate('/?')
    assert not validate('1.c.1.0')
    assert not validate('1.1.1.')
    assert not validate(' ')
