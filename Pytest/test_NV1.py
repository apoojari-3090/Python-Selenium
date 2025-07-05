import pytest
@pytest.mark.login
def test_m1():
    a = 3
    b = 2
    assert a+1 == b, "Test failed"
    assert a == b, "This test is failed as a is not equal to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENUIM"
@pytest.mark.login
def test_m3():
    assert False
@pytest.mark.login
def test_m4():
    assert True