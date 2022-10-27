"""
Database format

[{
    "name": <string>
    "id": <int>
    "blood_type": <string>
    "test_names": [<string>]
    "test_result": [<string>]
}]
"""

from flask import Flask, jsonify, request
import logging

db = []


app = Flask(__name__)


@app.route('/', methods=['GET'])
def server_status():
    return "DB server is on"


def add_patient(pt_name, pt_id, blood_type):
    new_pt = {'name': pt_name,
              'id': pt_id,
              'blood_type': blood_type,
              'test_name': [],
              'test_result': []}
    db.append(new_pt)


def init_server():
    add_patient('Ann Ables', 1, 'A+')
    add_patient('Bob Boyles', 2, 'B+')
    # initialize logging
    logging.basicConfig(filename='server.log')


@app.route('/new_patient', methods=['POST'])
def post_new_patient():
    """
    1. Receive data from post request
    2. Call other functions to do all the work
    3. Return information

    NEED TO ADD DATA FORMAT IN DOCSTRINGS OF ALL FLASK HANDLERS

    """
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient(in_data)
    if result is not True:
        return result, 400

    add_patient(in_data['name'],
                in_data['id'],
                in_data['blood_type'])
    return 'Patient successfully added', 200


def validate_new_patient(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"

    expected_keys = ['name', 'id', 'blood_type']
    for key in expected_keys:
        if key not in in_data:
            return f'Key {key} is missing from POST data'

    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return f'Value of key {key} is not of data type {ex_type}'

    return True


@app.route('/add_test', methods=['POST'])
def post_add_test():
    """
    in_data format: {
        'id': int,
        'test_name': str,
        'test_result': int
        }
    """
    in_data = request.get_json()
    message, status_code = add_test_worker(in_data)
    return message, status_code


def add_test_worker(in_data):
    result = validate_add_test(in_data)
    if result is not True:
        return result, 400

    add_test(in_data['id'], in_data['test_name'], in_data['test_result'])
    return 'Test successfully added', 200


def validate_add_test(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"

    # check for correct keys and that keys map to correct type
    expected_keys = ['id', 'test_name', 'test_result']
    expected_types = [int, str, int]
    for key, ex_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return f'Key {key} is missing from POST data'
        if type(in_data[key]) is not ex_type:
            return f'Value of key {key} is not of data type {ex_type}'

    # check patient is in database
    id = in_data['id']
    pt = find_pt(id)
    if not pt:
        return f'ID {id} not in patient database'

    return True


def find_pt(id):
    for pt in db:
        if pt['id'] == id:
            return pt
    return False


def add_test(id, test_name, test_result):
    pt = find_pt(id)
    pt['test_name'].append(test_name)
    pt['test_result'].append(test_result)


# @app.route('/get_results/<patient_id>', methods=['GET'])


if __name__ == '__main__':
    init_server()
    app.run()
