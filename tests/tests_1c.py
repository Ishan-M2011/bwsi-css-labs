"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_random():
    assert max_subarray_sum([1, 2, 3]) == 6           
    assert max_subarray_sum([-1, 0, 5]) == 5       
    assert max_subarray_sum([0, 0, 0]) == 0   
    assert max_subarray_sum([-2, -5, -4]) == -2       

def test_invalid_operation():
    with pytest.raises(TypeError, match="All elements must be integers"):
        max_subarray_sum([1, 2, "s"])            # Test for positive numbers
    with pytest.raises(IndexError, match="Cannot compute max sum of empty list"):
        max_subarray_sum([])                     # Test for empty list

if __name__ == "__main__":
    pytest.main()