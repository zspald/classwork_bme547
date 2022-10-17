import requests

# r = requests.get('https://api.github.com/repos/dward2/BME547/branchasdfes')
# print(r)
# print(type(r))
# print(r.text)
# print(r.status_code)

# if r.status_code == 200:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch['name'])
# else:
#     print(f"Bad request: {r.text}")

# output_info = {
#    "name": "Zac Spalding",
#    "net_id": "zms14",
#    "e-mail": "zac.spalding@duke.edu"
# }

# r = requests.post('http://vcm-21170.vm.duke.edu:5000/student',
#                   json=output_info)
# print(r)
# print(r.text)

# r = requests.get('http://vcm-21170.vm.duke.edu:5000/list')
# print(r.text)

# partner message activity
message = {"user": "zms14", "message": "whats up"}
r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message',
                  json=message)

r = requests.get('http://vcm-21170.vm.duke.edu:5001/get_messages/hmb39')
print(r.text)
