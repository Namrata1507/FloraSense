from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="frontend")

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend", path)

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]

    result = "Plant detected"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)