import pytest
from database_definition import Patient


def test_add_patient():
    from db_server import add_patient, init_server
    init_server()
    pt_name = 'David'
    pt_id = 222
    blood_type = 'A+'
    answer = add_patient(pt_name, pt_id, blood_type)
    find_patient = Patient.objects.raw({'_id': 222}).first()
    print(find_patient)
    find_patient.delete()
    assert answer.name == pt_name


def test_add_test():
    from db_server import init_server, add_patient, add_test
    init_server()

    pt_id = 123
    pt_name = 'David'
    added_pt = add_patient(pt_name, pt_id, 'A+')

    test_name = 'XXX'
    test_result = 200
    answer = add_test(pt_id, test_name, test_result)

    pt_from_db = Patient.objects.raw({'_id': pt_id}).first()
    added_pt.delete()

    assert pt_from_db.test_name[-1] == test_name
    assert pt_from_db.test_result[-1] == test_result
