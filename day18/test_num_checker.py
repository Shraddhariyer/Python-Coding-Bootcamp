from num_checker import is_positive
def test_positive():
    assert is_positive(5)==True
def test_negative():
    assert is_positive(-5)==False
def test_zero():
    assert is_positive(0)==False