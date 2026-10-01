import pytest
from datetime import date
from seasons import date_pattern, DateCalculation


# Test that valid YYYY-MM-DD strings successfully parse into date objects
def test_valid_date_pattern():
    assert date_pattern('1900-01-01') == date(1900, 1, 1)
    assert date_pattern('2025-01-01') == date(2025, 1, 1)
    assert date_pattern('2025-08-03') == date(2025, 8, 3)


# Test that non-standard date string formats raise a ValueError
def test_non_standard_date_pattern():
    with pytest.raises(ValueError):
        date_pattern('January 1, 2000')
    with pytest.raises(ValueError):
        date_pattern('1900/01/01')


# Test that incorrect date ordering (e.g., DD-MM-YYYY) raises a ValueError
def test_wrong_date_arrangement():
    with pytest.raises(ValueError):
        date_pattern('01-01-1900')
    with pytest.raises(ValueError):
        date_pattern('31-01-1900')
    with pytest.raises(ValueError):
        date_pattern('01-31-1900')


# Test that invalid calendar values (e.g., month 13, day 32) raise a ValueError
def test_invalid_calendar_values():
    with pytest.raises(ValueError):
        date_pattern('1900-01-32')
    with pytest.raises(ValueError):
        date_pattern('1900-02-30')
    with pytest.raises(ValueError):
        date_pattern('1900-13-30')
    with pytest.raises(ValueError):
        date_pattern('1900-0-30')
    with pytest.raises(ValueError):
        date_pattern('1900-02-0')


# Run multiple test cases pairing input dates with expected minute words
@pytest.mark.parametrize(
    'input_date, expected_mins', [
        (date(2025, 8, 3), 'Five hundred twenty-five thousand, six hundred minutes'),
        (date(2024, 8, 3), 'One million, fifty-one thousand, two hundred minutes'),
        (date(2026, 8, 2), 'One thousand, four hundred forty minutes'),
        (date(1900, 1, 1), 'Sixty-six million, five hundred seventy-eight thousand, four hundred minutes'),
        (date(2026, 8, 3), "Zero minutes")
    ]
)
def test_calculate_date_str(input_date, expected_mins):
    past_time = DateCalculation(input_date)
    assert past_time.calculate_mins() == expected_mins
