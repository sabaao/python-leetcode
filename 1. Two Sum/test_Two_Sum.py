import pytest
from TwoSumSolution import Solution

def test_1():
    s = Solution()
    input = [2,7,9,11,15]
    target:int = 9
    expect = [0,1]
    result = s.twoSum(input,target)
    assert expect ==  result

def test_1():
    s = Solution()
    input = [3,2,4]
    target:int = 6
    expect = [1,2]
    result = s.twoSum(input,target)
    assert expect ==  result
