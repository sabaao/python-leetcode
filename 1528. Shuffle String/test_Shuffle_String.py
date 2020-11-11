import pytest
from ShuffleString import Solution 

def test_codeleet_45670213():
    s = Solution()
    str = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    expect = "leetcode"
    result = s.restoreString(str,indices)
    assert expect ==  result

def test_abc_012():
    s = Solution()
    str = "abc"
    indices = [0,1,2]
    expect = "abc"
    result = s.restoreString(str,indices)
    assert expect ==  result

def test_aiohn_31420():
    s = Solution()
    str = "aiohn"
    indices = [3,1,4,2,0]
    expect = "nihao"
    result = s.restoreString(str,indices)
    assert expect ==  result