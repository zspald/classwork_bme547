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

@pytest.mark.parametrize("LDL_val, expected", 
    [(120, "Normal"), 
     (145, "Borderline High"), 
     (175, "High"), 
     (200, "Very High")],
    ids=['Normal Test', 'Borderline High Test', 'High Test', 'Very High Test'])
def test_check_LDL(LDL_val, expected):
    from blood_calculator import check_LDL
    result = check_LDL(LDL_val)
    assert result == expected

