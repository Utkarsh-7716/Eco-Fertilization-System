THRESHOLDS = {"N": {"low": 50, "high": 200}, "P": {"low": 20, "high": 50}, "K": {"low": 50, "high": 150}}
RECOMMENDATIONS = {"N_low": "Apply Urea (46% Nitrogen): 45–60 kg per acre.", "N_high": "Avoid nitrogen fertilizers (can harm growth).", "P_low": "Apply DAP (46% P₂O₅): 20–30 kg per acre.", "P_high": "Avoid phosphorus fertilizers (micronutrient lockout).", "K_low": "Apply MOP (60% K₂O): 15–25 kg per acre.", "K_high": "Avoid potash fertilizers.", "optimal": "Nutrient levels are optimal. Apply compost/FYM."}

def get_fertilizer_recommendation(n, p, k):
    result = {}
    if n < THRESHOLDS["N"]["low"]:
        result["N_status"] = "Low"
        result["N_recommendation"] = RECOMMENDATIONS["N_low"]
    elif n > THRESHOLDS["N"]["high"]:
        result["N_status"] = "High"
        result["N_recommendation"] = RECOMMENDATIONS["N_high"]
    else:
        result["N_status"] = "Optimal"
        result["N_recommendation"] = RECOMMENDATIONS["optimal"]
    if p < THRESHOLDS["P"]["low"]:
        result["P_status"] = "Low"
        result["P_recommendation"] = RECOMMENDATIONS["P_low"]
    elif p > THRESHOLDS["P"]["high"]:
        result["P_status"] = "High"
        result["P_recommendation"] = RECOMMENDATIONS["P_high"]
    else:
        result["P_status"] = "Optimal"
        result["P_recommendation"] = RECOMMENDATIONS["optimal"]
    if k < THRESHOLDS["K"]["low"]:
        result["K_status"] = "Low"
        result["K_recommendation"] = RECOMMENDATIONS["K_low"]
    elif k > THRESHOLDS["K"]["high"]:
        result["K_status"] = "High"
        result["K_recommendation"] = RECOMMENDATIONS["K_high"]
    else:
        result["K_status"] = "Optimal"
        result["K_recommendation"] = RECOMMENDATIONS["optimal"]
    return result
