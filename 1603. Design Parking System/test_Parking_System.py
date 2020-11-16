import pytest
from ParkingSystem import ParkingSystem

def test_110():
    p = ParkingSystem(1,1,0)
    assert p.addCar(1) == True
    assert p.addCar(2) == True
    assert p.addCar(3) == False
    assert p.addCar(1) == False