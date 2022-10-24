"""
Database format

[{
    "name": <string>
    "id": <int>
    "blood_type": <string>
    "test_names": [<string>]
    "test_results": [<string>]
}]
"""

from flask import Flask, jsonify, request


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


@app.route('/new_patient', methods=['POST'])
def post_new_patient():
    """
    1. Receive data from post request
    2. Call other functions to do all the work
    3. Return information
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


# @app.route('/add_test', methods='POST')


# @app.route('/get_results/<patient_id>', methods=['GET'])


if __name__ == '__main__':
    init_server()
    app.run()
