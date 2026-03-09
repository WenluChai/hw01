import pytest
from src.queens import solve_n_queens

def test_n_queens_4():
    """测试4皇后问题，预期2种解法"""
    assert len(solve_n_queens(4)) == 2
def test_n_queens_8():
    """测试8皇后问题，预期92种解法"""
    assert len(solve_n_queens(8)) == 92

def test_n_queens_1():
    """边界测试：1皇后问题，预期1种解法"""
    assert len(solve_n_queens(1)) == 1