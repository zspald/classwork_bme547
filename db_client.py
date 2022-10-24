import requests

url = 'http://127.0.0.1:5000'

out_data = {'name': 'Charlie', 'id': 3, 'blood_type': 'AB-'}
r = requests.post(url + '/new_patient', json=out_data)
print(r.status_code)
print(r.text)
