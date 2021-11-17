"""
test basic_maths.py.
"""

import basic_maths as bm


def test_add():
    """
    Test add
    """
    assert(bm.add(6, 3) == 9)


def test_minus():
    """
    Test minus
    """
    assert(bm.minus(6, 3) == 3)


def test_multiply():
    """
    Test multiply
    """
    assert(bm.multiply(6, 3) == 18)


def test_divide():
    """
    Test divide
    """
    assert(bm.divide(6, 3) == 2)

