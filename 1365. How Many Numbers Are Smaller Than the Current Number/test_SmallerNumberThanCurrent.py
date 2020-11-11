import pytest
from SmallerNumbersThanCurrent import Solution 

def test_81223():
    s = Solution()
    input = [8,1,2,2,3]
    expect = [4,0,1,1,3]
    result = s.smallerNumbersThanCurrent(input)
    assert expect ==  result

def test_6548():
    s = Solution()
    input = [6,5,4,8]
    expect = [2,1,0,3]
    result = s.smallerNumbersThanCurrent(input)
    assert expect ==  result

def test_7777():
    s = Solution()
    input = [7,7,7,7]
    expect = [0,0,0,0]
    result = s.smallerNumbersThanCurrent(input)
    assert expect ==  result