import pytest
from NestingDepth import Solution 

def test_depth_3():
    s = Solution()
    input = "(1+(2*3)+((8)/4))+1"
    expect:int = 3
    result = s.maxDepth(input)
    assert expect ==  result

def test_depth_3_sample_2():
    s = Solution()
    input = "(1)+((2))+(((3)))"
    expect:int = 3
    result = s.maxDepth(input)
    assert expect ==  result

def test_depth_1():
    s = Solution()
    input = "1+(2*3)/(2-1)"
    expect:int = 1
    result = s.maxDepth(input)
    assert expect ==  result