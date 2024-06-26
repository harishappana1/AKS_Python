from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Dhaapps Students!!! Tomorrow is important Election date, Vote for Correct person , voting starts from 7 AM"

@app.route("/api/data")
def data():
    return jsonify({"message": "Here's some JSON data", "status": "success"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
