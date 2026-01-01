from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load Prophet model
model = joblib.load("prophet_model.joblib")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Prophet Model API Running"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert JSON to DataFrame
        future_df = pd.DataFrame(data)

        # Prophet requires 'ds' column
        if "ds" not in future_df.columns:
            return jsonify({"error": "Missing 'ds' column"}), 400

        forecast = model.predict(future_df)

        output = forecast[
            ["ds", "yhat", "yhat_lower", "yhat_upper"]
        ].to_dict(orient="records")

        return jsonify({"forecast": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
