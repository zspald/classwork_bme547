from tkinter import filedialog
import base64
import requests


def upload_image():
    filename = get_image_file_name()
    b64_string = convert_file_to_b64(filename)
    result = upload_b64_to_server(b64_string)


def get_image_file_name():
    filename = filedialog.askopenfilename()
    return filename


def convert_file_to_b64(filename):
    with open(filename, 'rb') as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def upload_b64_to_server(b64_string):
    out_data = {'image': b64_string, 'net_id': 'zms14', 'id_no': 1}
    r = requests.post('http://vcm-21170.vm.duke.edu/add_image', json=out_data)
    return r


def download_image(net_id, id_no):
    url = 'http://vcm-21170.vm.duke.edu/get_image/' + net_id +\
          '/' + str(id_no)
    r = requests.get(url)
    convert_b64_to_image_file(r.text, 'downloaded_image.jpg')


def convert_b64_to_image_file(b64_string, filename):
    image_bytes = base64.b64decode(b64_string)
    with open(filename, "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == '__main__':
    download_image('zms14', 1)
