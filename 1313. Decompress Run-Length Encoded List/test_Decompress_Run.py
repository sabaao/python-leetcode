import pytest
from DecompressRun import Solution 

def test_1234():
    s = Solution()
    input = [1,2,3,4]
    expect = [2,4,4,4]
    result = s.decompressRLElist(input)
    assert expect ==  result

def test_1123():
    s = Solution()
    input = [1,1,2,3]
    expect = [1,3,3]
    result = s.decompressRLElist(input)
    assert expect ==  result
