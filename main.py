from flask import Flask, request
from API import API


app = Flask(__name__)
api = API()


@app.route('/send_api/', methods=['GET'])
def send_api():
    parsed_response = api.send_api(params=request.args)
    return parsed_response


if __name__ == '__main__':
    app.run(debug=True)
