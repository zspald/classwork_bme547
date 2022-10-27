import requests

url = 'http://127.0.0.1:5000'

# out_data = {'name': 'Charlie', 'id': 3, 'blood_type': 'AB-'}
# r = requests.post(url + '/new_patient', json=out_data)
# print(r.status_code)
# print(r.text)

out_data_test = {'id': 2, 'test_name': 'HDL', 'test_result': 1}
r_test = requests.post(url + '/add_test', json=out_data_test)
print(r_test.status_code)
print(r_test.text)
