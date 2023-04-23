from flask import Flask, jsonify

app = Flask(__name__)


@app.get('/')
def container():
    return jsonify({'message': 'Hello World!'})

