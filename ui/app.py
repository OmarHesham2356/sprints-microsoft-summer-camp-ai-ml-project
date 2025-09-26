import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline (preprocessing + model)
model = joblib.load("../models/final_model.pkl")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below to check the risk of heart disease.")

# Collect user input
age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0 = typical angina, 1 = atypical angina, 2 = non-anginal, 3 = asymptomatic)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG results (0 = normal, 1 = ST-T abnormality, 2 = LV hypertrophy)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", 70, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.5, 1.0)
slope = st.selectbox("Slope of ST segment (0 = upsloping, 1 = flat, 2 = downsloping)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)", [3, 6, 7])

# Convert categorical: sex -> 1 male, 0 female
sex = 1 if sex == "Male" else 0

# Build input DataFrame (raw features)
input_data = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of Heart Disease (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Low risk of Heart Disease (Probability: {prob:.2f})")
