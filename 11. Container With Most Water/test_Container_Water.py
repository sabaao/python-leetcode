import pytest
from ContainerWater import Solution

def test_186254837():
    s = Solution()
    input = [1,8,6,2,5,4,8,3,7]
    expect = 49
    result = s.maxArea(input)
    assert expect ==  result

def test_11():
    s = Solution()
    input = [1,1]
    expect = 1
    result = s.maxArea(input)
    assert expect ==  result

def test_121():
    s = Solution()
    input = [1,2,1]
    expect = 2
    result = s.maxArea(input)
    assert expect ==  result