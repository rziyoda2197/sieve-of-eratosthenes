import pytest
from your_module import sieve_of_eratosthenes

def test_sieve_of_eratosthenes():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sieve_of_eratosthenes_edge_cases():
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(2) == [2]
    assert sieve_of_eratosthenes(0) == []

def test_sieve_of_eratosthenes_invalid_input():
    with pytest.raises(TypeError):
        sieve_of_eratosthenes("10")
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(-10)
