import requests

# r = requests.get('http://127.0.0.1:5000/info')
# print(r.status_code)
# print(r.text)

# out_data = {'name': 'David Ward', 'hdl_value': 30}
# r = requests.post('http://127.0.0.1:5000/hdl_check', json=out_data)
# print(r.status_code)
# print(r.text)

out_data = {'a': 50, 'b': 11}
r = requests.post('http://127.0.0.1:5000/add_numbers', json=out_data)
print(r.status_code)
print(r.text)

answer = r.json()
a = answer + 3
print(a)

# r = requests.get('http://127.0.0.1:5000/add/50/11')
# print(r.status_code)
# print(r.text)
