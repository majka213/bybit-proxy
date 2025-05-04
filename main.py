from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BYBIT_URL = "https://api.bybit.com/v2/public/funding/prev-funding-rate?symbol=BTCUSDT"

@app.route("/funding")
def funding():
    print("FUNKCJA /funding ZOSTAŁA URUCHOMIONA")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(BYBIT_URL, headers=headers)

        print("=== RESPONSE STATUS CODE ===")
        print(response.status_code)
        print("=== RESPONSE TEXT ===")
        print(response.text)
        print("=====================")

        return jsonify(response.json())
    except Exception as e:
        print("=== ERROR WYWALONY ===")
        import traceback
        traceback.print_exc()
        print("=====================")
        return jsonify({"error": str(e)}), 500

app.run(host="0.0.0.0", port=10000)
