from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/detect", methods=["POST"])
def detect():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Temporary result (AI will be added later)
    result = {
        "plant_name": "Neem",
        "category": "Native",
        "confidence": "92%"
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
