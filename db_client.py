import requests

url = 'http://127.0.0.1:5000'


def upload_patient_info(patient_name, patient_id, patient_blood_type):
    out_data = {'name': patient_name, 'id': patient_id,
                'blood_type': patient_blood_type}
    r = requests.post(url + '/new_patient', json=out_data)
    return r.text, r.status_code
# out_data = {'name': 'Charlie', 'id': 3, 'blood_type': 'AB-'}
# r = requests.post(url + '/new_patient', json=out_data)
# print(r.status_code)
# print(r.text)


# out_data_test = {'id': 3, 'test_name': 'LDL', 'test_result': 100}
# r_test = requests.post(url + '/add_test', json=out_data_test)
# print(r_test.status_code)
# print(r_test.text)
