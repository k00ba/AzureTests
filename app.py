from flask import Flask, request, jsonify, render_template, url_for
from flask import request
import random

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    data = []
    statuslist = ["yes", "no"]
    content = request.get_json()
    for profile in content['data']:
        status = random.choice(statuslist)
        item = {"email": profile['email'], "status":status}
        data.append(item)

    return jsonify({"data":data})

if __name__ == '__main__':
    app.run(debug=True)


