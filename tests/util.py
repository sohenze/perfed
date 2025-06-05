import pytest


def tolerant_approx(expected):
    return pytest.approx(expected, rel=1e-2)
