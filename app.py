from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
latest = []   # stores latest BLE scan JSON list

@app.route('/ble', methods=['POST'])
def post_ble():
    global latest
    data = request.get_json(force=True)
    latest = data if isinstance(data, list) else [data]
    return "OK"

@app.route('/ble', methods=['GET'])
def get_ble():
    return jsonify(latest)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "time": datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
