from twttr import shorten
import pytest

def test_vowel_a():
    assert shorten("CHELLIOS") == "CHLLS"
    assert shorten("twitter") == "twttr"
    assert shorten("e") == ""
    assert shorten("oh!") == "h!"
    assert shorten("enchant123") == "nchnt123"
    assert shorten("up") == "p"
