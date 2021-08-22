import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output


@pytest.mark.parametrize("num",[1,2,3,4,5])
def test_prime(num):
    assert num%2 == 0
