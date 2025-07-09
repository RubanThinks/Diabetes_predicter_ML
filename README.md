# 🩺 Diabetes Predictor App

A user-friendly **Machine Learning web app** built with **Streamlit**, powered by a **Random Forest Classifier**, to predict diabetes risk based on demographic, medical, and lifestyle inputs.

---

## 📊 Dataset

- Based on the Kaggle “Diabetes Prediction Dataset” (~100,000 samples, 9 features) :contentReference[oaicite:14]{index=14}.
- Features:
  - `gender`, `age`, `hypertension`, `heart_disease`
  - `smoking_history`, `bmi`, `HbA1c_level`, `blood_glucose_level`
  - Target: `diabetes` (0/1)

---

## 🛠 Model

- **Algorithm**: Random Forest Classifier
- **Inputs**: 8 features above → **predicts diabetes risk**
- **Expected Accuracy**: ~85–90% depending on train-test split and preprocessing

---

## 🚀 Installation

```bash
git clone https://github.com/RubanThinks/Diabetes_predicter_ML.git
pip install -r requirements.txt
▶️ Usage

streamlit run app.py
