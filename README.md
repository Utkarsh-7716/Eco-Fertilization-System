# 🌱 Eco-Fertilization System

An intelligent Machine Learning-based system that predicts the optimal **Nitrogen (N), Phosphorus (P), and Potassium (K)** requirements for crops using real-time weather data and provides fertilizer recommendations.

---

## 🚀 Features

- 🌾 Predicts NPK nutrient requirements
- 🌦️ Uses real-time weather data (Temperature, Humidity, Rainfall)
- 📊 Displays 7-day weather forecast graph
- 🧠 Machine Learning model (Random Forest)
- 🌿 Fertilizer recommendation system
- 🔄 Supports 110+ crops

---

## 🧠 Tech Stack

- **Machine Learning:** Scikit-learn (Random Forest)
- **Backend:** Flask (Python)
- **Data Processing:** Pandas, NumPy
- **API Integration:** WeatherAPI
- **Visualization:** Recharts (for graphs)

---

## ⚙️ How It Works

1. User selects crop and enters city  
2. System fetches real-time weather data  
3. ML model predicts N, P, K values  
4. System generates fertilizer recommendations  
5. Results + 7-day forecast are displayed  

---

## 📂 Project Structure
Eco-Fertilization/
│
├── app/ # Flask backend
├── frontend/ # Frontend files
├── models/ # ML models (.joblib)
├── dataset/ # Training data
├── README.md


---

## ▶️ How to Run

### Backend

```bash
cd app
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py


cd frontend
npm install
npm run dev


Create a .env file and add your WeatherAPI key:
VITE_API_KEY=your_api_key_here
