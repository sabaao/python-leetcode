import pytest
from LongestSubstring import Solution

def test_abcabcbb():
    s = Solution()
    input = 'abcabcbb'
    expect = 3
    result = s.lengthOfLongestSubstring(input)
    assert expect ==  result

def test_bbbbb():
    s = Solution()
    input = 'bbbbb'
    expect = 1
    result = s.lengthOfLongestSubstring(input)
    assert expect ==  result

def test_pwwkew():
    s = Solution()
    input = 'pwwkew'
    expect = 3
    result = s.lengthOfLongestSubstring(input)
    assert expect ==  result