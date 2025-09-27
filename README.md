# ❤️ Heart Disease Prediction Project

## 📌 Overview

This project predicts the risk of heart disease using the [UCI Heart Disease dataset](https://archive.ics.uci.edu/dataset/45/heart+disease).
It applies **data preprocessing, dimensionality reduction (PCA), supervised and unsupervised learning, and hyperparameter tuning** to build and evaluate machine learning models.

As a bonus, it includes a **Streamlit UI** for real-time predictions.

---

## 📂 Project Structure

```
Heart_Disease_Project/
│── data/
│   ├── heart_disease.csv              # Raw dataset
│   ├── heart_disease_cleaned.csv      # Cleaned dataset
│
│── notebooks/
│   ├── data_preprocessing.ipynb       # Data cleaning & preprocessing
│   ├── PCA_Analysis.ipynb              # Dimensionality reduction with PCA
│   ├── Feature_Selection.ipynb         # Feature selection methods
│   ├── Supervised_Learning.ipynb       # Baseline supervised models
│   ├── unsupervised_learning.ipynb     # Clustering approaches
│   ├── hyperparameter_tuning.ipynb     # GridSearchCV for model optimization
│
│── models/
│   ├── final_model.pkl                 # Saved tuned ML pipeline
│
│── ui/
│   ├── app.py                          # Streamlit UI for predictions
│
│── deployment/
│   ├── ngrok_setup.txt                 # Steps to deploy app online with ngrok
│
│── results/
│   ├── evaluation_metrics.txt          # Model performance summary
│
│── requirements.txt                    # Required Python packages
│── README.md                           # Project documentation
│── .gitignore                          # Files ignored by Git
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Heart_Disease_Project.git
cd Heart_Disease_Project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Run Jupyter notebooks

Open any notebook in the `notebooks/` folder to see preprocessing, PCA, supervised/unsupervised learning, and hyperparameter tuning steps.

### 2. Run the Streamlit UI

```bash
streamlit run ui/app.py
```

This will launch the app at `http://localhost:8501`.
Enter patient details to predict the **risk of heart disease**.

### 3. (Optional) Deploy using ngrok

Follow steps in `deployment/ngrok_setup.txt` to share your app with others.

---

## 📊 Results

* Baseline models tested: Logistic Regression, Decision Tree, Random Forest, SVM
* Hyperparameter tuning performed with **GridSearchCV**
* ✅ **Final model: Tuned SVM (C=10, kernel=linear)**
* Accuracy: **85%**
* Recall (disease detection): **93%**

See detailed metrics in `results/evaluation_metrics.txt`.

---

## 📦 Requirements

Main packages used:

* pandas, numpy
* matplotlib, seaborn
* scikit-learn
* streamlit
* joblib

Install them via:

```bash
pip install -r requirements.txt
```

---

## 🎯 Deliverables Checklist

✔️ Cleaned dataset
✔️ PCA results
✔️ Supervised & unsupervised models
✔️ Performance metrics in `results/`
✔️ Hyperparameter optimized model (`final_model.pkl`)
✔️ Streamlit UI for real-time prediction

---

Repo's Link: https://github.com/OmarHesham2356/sprints-microsoft-summer-camp-ai-ml-project
