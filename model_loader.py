import os
import joblib
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH_N = os.path.join(BASE_DIR, "npk_model_n.joblib")
MODEL_PATH_P = os.path.join(BASE_DIR, "npk_model_p.joblib")
MODEL_PATH_K = os.path.join(BASE_DIR, "npk_model_k.joblib")
ENCODER_PATH = os.path.join(BASE_DIR, "crop_encoder.joblib")

def load_models():
    try:
        model_n = joblib.load(MODEL_PATH_N)
        model_p = joblib.load(MODEL_PATH_P)
        model_k = joblib.load(MODEL_PATH_K)
        encoder = joblib.load(ENCODER_PATH)
        print("✓ Models loaded successfully")
        try:
            print("✓ Available crops:", list(encoder.classes_))
        except Exception:
            pass
        return {"n": model_n, "p": model_p, "k": model_k, "enc": encoder}
    except Exception as e:
        print("❌ Error loading models:", e)
        raise e

def predict(models, crop, temperature, humidity, rainfall):
    encoder = models["enc"]
    try:
        classes = list(encoder.classes_)
    except Exception:
        classes = None
    if classes is not None and crop not in classes:
        raise ValueError(f"Crop '{crop}' is not recognized. Valid crops: {classes}")
    crop_encoded = encoder.transform([crop])[0]
    X = [[float(crop_encoded), float(temperature), float(humidity), float(rainfall)]]
    pred_n = models["n"].predict(X)[0]
    pred_p = models["p"].predict(X)[0]
    pred_k = models["k"].predict(X)[0]
    return {"N": float(round(pred_n, 3)), "P": float(round(pred_p, 3)), "K": float(round(pred_k, 3))}
