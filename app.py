

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

from weather_service import get_weather, get_forecast


app = Flask(__name__)
CORS(app)


MODEL_PATH_N = "npk_model_n.joblib"
MODEL_PATH_P = "npk_model_p.joblib"
MODEL_PATH_K = "npk_model_k.joblib"
ENCODER_PATH = "crop_encoder.joblib"



def load_models():
    """Load all ML models and encoder."""
    try:
        model_n = joblib.load(MODEL_PATH_N)
        model_p = joblib.load(MODEL_PATH_P)
        model_k = joblib.load(MODEL_PATH_K)
        encoder = joblib.load(ENCODER_PATH)

        print("✓ Models loaded successfully")
        crops = encoder.classes_ if hasattr(encoder, "classes_") else "unknown"
        print("✓ Available crops:", crops)

        return model_n, model_p, model_k, encoder

    except Exception as e:
        print("❌ Error loading models:", e)
        return None, None, None, None


model_n, model_p, model_k, encoder = load_models()



@app.route("/weather", methods=["POST"])
def weather_api():
    data = request.get_json() or {}
    city = data.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        weather = get_weather(city)
        return jsonify({
            "status": "success",
            "city": city,
            "weather": weather
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/crops", methods=["GET"])
def get_crops():
    if encoder is None:
        return jsonify({"error": "Encoder not loaded"}), 500

    try:
        crops = list(encoder.classes_)
        return jsonify({"status": "success", "crops": crops})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/forecast", methods=["POST"])
def forecast_api():
    data = request.get_json() or {}
    city = data.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        forecast = get_forecast(city, days=7)
        return jsonify({
            "status": "success",
            "city": city,
            "forecast": forecast
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/predict_with_weather", methods=["POST"])
def predict_with_weather():
    data = request.get_json() or {}
    crop = data.get("crop")
    city = data.get("city")

    if not crop or not city:
        return jsonify({"error": "Crop and City are required"}), 400

    if not all([model_n, model_p, model_k, encoder]):
        return jsonify({"error": "Models not loaded"}), 500

    try:

        weather = get_weather(city)
        temperature = weather["temperature"]
        humidity = weather["humidity"]
        rainfall = weather["rainfall"]


        crop_encoded = encoder.transform([crop])[0]


        X_input = [[crop_encoded, temperature, humidity, rainfall]]

        pred_n = round(float(model_n.predict(X_input)[0]), 2)
        pred_p = round(float(model_p.predict(X_input)[0]), 2)
        pred_k = round(float(model_k.predict(X_input)[0]), 2)


        


        def classify(value):
            if value < 50:
                return "Low"
            elif value < 120:
                return "Optimal"
            else:
                return "High"

        def recommendation(nutrient, status):
            if status == "Low":
                return {
                    "N": "Apply Urea (46% N): 45–60 kg per acre.",
                    "P": "Apply SSP (16% P2O5): 50–75 kg per acre.",
                    "K": "Apply MOP (60% K2O): 15–25 kg per acre."
                }[nutrient]

            elif status == "Optimal":
                return "Nutrient levels are optimal. Apply compost/FYM."

            else:
                return "Reduce fertilizer use. Soil nutrient levels high."

        status_n = classify(pred_n)
        status_p = classify(pred_p)
        status_k = classify(pred_k)

        return jsonify({
            "status": "success",
            "city": city,
            "weather_used": weather,
            "predicted_nutrients": {
                "N": pred_n,
                "P": pred_p,
                "K": pred_k
            },
            "fertilizer_recommendation": {
                "N_status": status_n,
                "N_recommendation": recommendation("N", status_n),
                "P_status": status_p,
                "P_recommendation": recommendation("P", status_p),
                "K_status": status_k,
                "K_recommendation": recommendation("K", status_k)
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    



if __name__ == "__main__":
    app.run(debug=True)
