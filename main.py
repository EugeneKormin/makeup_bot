from flask import Flask, request
from API import API


app = Flask(__name__)
api = API()


@app.route('/make-up_bot/', methods=['GET'])
def makeup_bot():
    param = request.args
    param = api.set_params(param=param)
    return param


@app.route('/send_api/', methods=['GET'])
def send_api():
    parsed_response = api.send_api()
    return parsed_response


if __name__ == '__main__':
    app.run(debug=True)
