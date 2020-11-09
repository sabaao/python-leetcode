import pytest
from Solution import Soltion 

def test_4_1():
    s = Soltion()
    input = "1.1.1.1"
    expect = "1[.]1[.]1[.]1"
    result = s.defangIPaddr(input)
    assert expect ==  result

def test_case_2():
    s = Soltion()
    input = "255.100.50.0"
    expect = "255[.]100[.]50[.]0"
    result = s.defangIPaddr(input)
    assert expect ==  result

