import pytest
from RunningSumSolution import Solution 

def test_1234():
    s = Solution()
    input = [1,2,3,4]
    expect = [1,3,6,10]
    result = s.runningSum(input)
    assert expect ==  result

def test_11111():
    s = Solution()
    input = [1,1,1, 1,1]
    expect = [1,2,3,4, 5]
    result = s.runningSum(input)
    assert expect ==  result

def test_312101():
    s = Solution()
    input = [3,1,2,10,1]
    expect = [3,4,6,16,17]
    result = s.runningSum(input)
    assert expect ==  result
