import pytest
from jar import Jar

# Test that Jar initializes with default capacity of 12 and starting size of 0


def test_init():
    jar = Jar()
    assert str(jar.capacity) == '12'
    assert str(jar.size) == '0'

# Test string representation (__str__) returns the correct number of cookie emojis


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

# Test valid cookie deposits update both the jar's size and string representation


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == '🍪'
    assert str(jar.size) == '1'
    jar = Jar()
    jar.deposit(0)
    assert str(jar) == ''
    assert str(jar.size) == '0'

# Test that depositing more cookies than the capacity allows raises a ValueError


def test_invalid_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.deposit(13)

# Test that depositing non-integer types raises a ValueError


def test_deposit_with_invalid_data_type():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.deposit('cat')

# Test valid cookie withdrawal reduces the jar's size


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert str(jar.size) == '1'

# Test that withdrawing more cookies than are currently in the jar raises a ValueError


def test_invalid_withdrawal():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        assert jar.withdraw(7)

# Test that withdrawing non-integer types raises a ValueError


def test_withdrawal_with_invalid_data_type():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        assert jar.withdraw('cat')

# Test that attempting to withdraw from an empty jar raises a ValueError


def test_withdrawal_without_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.withdraw(7)
