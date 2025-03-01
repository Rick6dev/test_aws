from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return jsonify({"message": "Hola Mundo!", "status": "ok"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello!", "status": "ok"})
@app.route('/foo',methods=['GET'])
def foo():
    return jsonify({'message':'Fooziman'};

@app.route('/gm')
def gm():
    return jsonify({"message": "gm!", "status": "ok"})

@app.route('/status')
def status():
    return jsonify({"status": "active", "timestamp": datetime.now().isoformat()})

@app.route('/data')
def data():
    return jsonify({"items": [1, 2, 3], "count": 3})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
