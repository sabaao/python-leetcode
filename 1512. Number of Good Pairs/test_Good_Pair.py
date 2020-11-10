import pytest
from GoodPair import Solution 

def test_123113():
    s = Solution()
    input = [1,2,3,1,1,3]
    expect = 4
    result = s.numIdenticalPairs(input)
    assert expect ==  result

def test_1111():
    s = Solution()
    input = [1,1,1,1]
    expect = 6
    result = s.numIdenticalPairs(input)
    assert expect ==  result

def test_123():
    s = Solution()
    input = [1,2,3]
    expect = 0
    result = s.numIdenticalPairs(input)
    assert expect ==  result
