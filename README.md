
# 📊 Customer Churn Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn using customer demographics, service details, contract information, and billing data. The project includes data preprocessing, exploratory data analysis (EDA), model comparison, explainable AI (SHAP), and deployment through a professional multi-page Streamlit application.

---

## 🚀 Project Highlights

- 📂 End-to-End Machine Learning Pipeline
- 🧹 Data Cleaning & Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- 🔧 Feature Engineering
- 🔢 One-Hot Encoding & Feature Scaling
- 🤖 Model Training & Comparison
- 📈 Model Performance Evaluation
- 🧠 SHAP Explainability
- 👤 Single Customer Churn Prediction
- 📁 Batch Prediction using CSV Upload
- 📥 Download Prediction Results
- 🌐 Multi-Page Streamlit Dashboard
- 📘 About Project Page

---

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

**Dataset Summary**

- Total Customers: **7043**
- Original Features: **20**
- Encoded Features: **30**
- Target Variable: **Churn**

### Features Used

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

# 📊 Exploratory Data Analysis

The project includes visual analysis such as:

- Churn Distribution
- Contract Type vs Churn
- Internet Service vs Churn
- Monthly Charges Distribution
- Tenure vs Churn
- Gender vs Churn
- Payment Method vs Churn
- Correlation Heatmap

---

# 🤖 Machine Learning Models Compared

| Model               | Accuracy            |
| ------------------- | ------------------- |
| Logistic Regression | **78.75%** ✅ |
| Random Forest       | 78.53%              |
| SVM                 | 78.11%              |
| KNN                 | 75.20%              |
| Decision Tree       | 72.49%              |
| Naive Bayes         | 65.60%              |

---

# 🏆 Best Model

### Logistic Regression

**Accuracy:** **78.75%**

### Why Logistic Regression?

- Highest accuracy among tested models
- Fast prediction
- Easy to interpret
- Well suited for binary classification
- Stable performance

---

# 📈 Model Evaluation

The project evaluates the model using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- Classification Report

---

# 🧠 Explainable AI (SHAP)

This project uses **SHAP (SHapley Additive exPlanations)** to improve model interpretability.

SHAP helps explain:

- Which features increase churn probability
- Which features decrease churn probability
- Overall feature importance
- Model transparency for business users

---

# 🌐 Streamlit Dashboard

The application contains multiple pages.

## 🏠 Dashboard

- Customer Information
- Service Information
- Billing Information
- Predict Customer Churn
- Prediction Probability
- Business Recommendations
- Dataset Statistics
- Interactive Charts

---

## 📈 Model Performance

Displays:

- Confusion Matrix
- ROC Curve
- Classification Report
- Accuracy
- Precision
- Recall
- F1 Score

---

## 📂 Batch Prediction

Features include:

- Upload Customer CSV
- Predict Multiple Customers
- Churn Probability
- Prediction Summary
- Download Prediction CSV
- Churn Distribution Charts

---

## 🧠 Feature Importance

Displays:

- SHAP Summary Plot
- Feature Importance
- Model Explainability

---

## 📘 About Project

Includes:

- Project Overview
- Dataset Information
- Workflow
- Technologies Used
- Business Impact
- Future Improvements

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- SHAP
- Pickle

---

# 📁 Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   ├── cleaned_churn.csv
│   └── sample_customers.csv
│
├── notebook/
│   └── customer_churn.ipynb
│
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
│
├── pages/
│   ├── 1_Model_Performance.py
│   ├── 2_Batch_Prediction.py
│   ├── 3_About_Project.py
│   └── 4_Feature_Importance.py
│
├── images/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── shap_summary.png
│   ├── dashboard.png
│   ├── model_performance.png
│   ├── batch_prediction.png
│   └── about_project.png
│
└── artifacts/
```

---

# ⚙ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
```

### 2. Move into the Project Folder

```bash
cd customer-churn-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

# 📊 Business Impact

This solution helps organizations:

- Identify customers likely to churn
- Improve customer retention strategies
- Reduce revenue loss
- Support data-driven business decisions
- Enable targeted marketing campaigns

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- XGBoost
- LightGBM
- CatBoost
- Database Integration
- REST API Development
- Docker Deployment
- AWS/Azure Cloud Deployment
- Real-Time Prediction System

---

# 📷 Dashboard Screenshots

Add screenshots after deployment.

Example:

- Dashboard
- Prediction Result
- Batch Prediction
- Model Performance
- Feature Importance
- About Project

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

# 👩‍💻 Author

**Renuka Chand**

Aspiring Data Scientist

### Skills

- Python
- SQL
- Power BI
- Machine Learning
- Data Analysis
- Streamlit

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
