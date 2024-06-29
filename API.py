import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name':'praisy',
        'email':'praisy@outlook.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)