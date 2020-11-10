import pytest
from ShuffleTheArray import Solution 

def test_251347():
    s = Solution()
    n = 3
    input = [2,5,1,3,4,7]
    expect = [2,3,5,4,1,7]
    result = s.shuffle(input,n)
    assert expect ==  result

def test_12344321():
    s = Solution()
    n = 4
    input = [1,2,3,4,4,3,2,1]
    expect = [1,4,2,3,3,2,4,1]
    result = s.shuffle(input,n)
    assert expect ==  result

def test_1122():
    s = Solution()
    n = 2
    input = [1,1,2,2]
    expect = [1,2,1,2]
    result = s.shuffle(input,n)
    assert expect ==  result
