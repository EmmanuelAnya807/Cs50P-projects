from fuel import convert, gauge
import pytest


def test_convert_valid_boundaries():
    # Verify that minimum and maximum valid fractional inputs calculate correctly
    assert convert("0/2") == 0
    assert convert("2/2") == 100


def test_convert_standard_fractions():
    # Verify accurate percentage calculations for typical proper fractions
    assert convert("1/2") == 50
    assert convert("0/100") == 0


def test_convert_invalid_value_exceptions():
    # Verify ValueError is raised if numerator exceeds denominator or if negative values are provided
    with pytest.raises(ValueError):
        convert("8/2")

    with pytest.raises(ValueError):
        convert("-1/2")


def test_convert_malformed_string_exceptions():
    # Verify ValueError is raised for non-numeric, whitespace, or malformed characters
    with pytest.raises(ValueError):
        convert(" /2")

    with pytest.raises(ValueError):
        convert("./?")

    with pytest.raises(ValueError):
        convert("///")


def test_convert_zero_denominator_exception():
    # Verify ZeroDivisionError is raised when attempting to divide by zero
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge_empty_and_full_thresholds():
    # Verify gauge accurately outputs 'E' at <= 1% and 'F' at >= 99%
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_standard_percentage_formatting():
    # Verify typical numerical percentages are formatted with a trailing '%' symbol
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
