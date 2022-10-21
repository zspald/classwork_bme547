import requests

url = 'http://vcm-7631.vm.duke.edu:5002'

r1 = requests.get(url + '/get_patients/zms14')
print(f'Patient ID request code: {r1.status_code}')
pt_dict = r1.json()
# print(pt_dict)

r_donor = requests.get(url + '/get_blood_type/' + pt_dict['Donor'])
print(f'Donor type request code: {r_donor.status_code}')
donor_type = r_donor.text
print(f'Donor blood type: {donor_type}')

r_recip = requests.get(url + '/get_blood_type/' + pt_dict['Recipient'])
print(f'Recipient type request code: {r_recip.status_code}')
recip_type = r_recip.text
print(f'Recipient blood type: {recip_type}')

match_dict = {'Name': 'zms14', 'Match': 'Yes'}
r_answer = requests.post(url + '/match_check', json=match_dict)
print(f'Blood match request code: {r_answer.status_code}')
print(f'Blood match result: {r_answer.text}')
