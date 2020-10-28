from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    status = "aaa"
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True)