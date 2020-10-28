from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    return jsonify({"status": "aaa"})

if __name__ == '__main__':
    app.run(debug=True)