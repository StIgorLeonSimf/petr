import pytest
from calc_d import add, sub


@pytest.mark.parametrize('n1, d1, n2, d2, res', [
    (1, 3, 1, 2, (5, 6)),
    (1, 2, 1, 2, (2, 2)),
    (1, 0, 1, 2, (1, 1)),
    (1, 2, 1, 0, (1, 1))
])
def test_add(n1, d1, n2, d2, res):
    assert add(n1, d1, n2, d2) == res


# def test_add():
#     assert add(1, 3, 1, 2) == (5, 6)
#     assert add(1, 2, 1, 2) == (2, 2)
#     assert add(1, 0, 1, 2) == (1, 1)
#     assert add(1, 2, 1, 0) == (1, 1)

def test_sub():
    assert sub(1, 3, 1, 2) == (-1, 6)
    assert sub(1, 2, 1, 2) == (0, 2)
    assert sub(1, 0, 1, 2) == (1, 1)
    assert sub(1, 2, 1, 0) == (1, 1)