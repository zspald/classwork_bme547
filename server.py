from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def server_status():
    return "Server is on."


@app.route('/info', methods=['GET'])
def information():
    x = 'This website will calculate the blood cholesterol levels.\n'
    x += 'It is written by Zac Spalding.'
    return x


@app.route('/hdl_check', methods=['POST'])
def hdl_check_from_internet():
    """
        incoming_json = {'name': <name_str>,
                         'hdl_value': <hdl_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_val = in_data['hdl_value']
    print(f'Received value was {hdl_val}')
    answer = check_HDL(hdl_val)
    return answer


@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    in_data = request.get_json()
    answer = in_data['a'] + in_data['b']
    return jsonify(answer)


@app.route('/add/<a>/<b>', methods=['GET'])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == '__main__':
    app.run()
