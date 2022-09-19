import pytest

@pytest.mark.parametrize("HDL_val, expected", 
    [(85, "Normal"), 
     (50, "Borderline Low"), 
     (35, "Low")],
    ids=['Normal Test', 'Borderline Low Test', 'Low Test'])
def test_check_HDL(HDL_val, expected):
    from blood_calculator import check_HDL
    result = check_HDL(HDL_val)
    assert result == expected

