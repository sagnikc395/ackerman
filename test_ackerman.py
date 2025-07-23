import pytest
from ackerman import lev 

@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("apple","dapple",1),
        ("apple","apple",0),
        ("apple","grapple",2),
        ("apple","dapled",3),
        ("apple","eappla",2),
    ]
)


def test_basic_levi(s1,s2,expected):
    assert lev(s1,s2) == expected
