import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="📘",
    layout="wide"
)

st.title("📘 About Customer Churn Prediction Project")

st.markdown("---")

st.header("🎯 Project Overview")

st.write("""
Customer churn prediction is the process of identifying customers who are likely to stop using a company's services.

This project uses Machine Learning to predict customer churn based on customer demographics, billing information, contract details, and service usage.
""")

st.markdown("---")

st.header("📊 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Customers", "7043")
    st.metric("Features", "20 Original")

with col2:
    st.metric("Encoded Features", "30")
    st.metric("Target Variable", "Churn")

st.markdown("---")

st.header("⚙ Machine Learning Workflow")

st.markdown("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis (EDA)

4. Feature Engineering

5. One-Hot Encoding

6. Feature Scaling

7. Train-Test Split

8. Model Training

9. Model Evaluation

10. Deployment using Streamlit
""")

st.markdown("---")

st.header("🤖 Machine Learning Models Compared")

st.table({
    "Model":[
        "Logistic Regression",
        "Random Forest",
        "SVM",
        "KNN",
        "Decision Tree",
        "Naive Bayes"
    ],
    "Accuracy":[
        "78.75%",
        "78.53%",
        "78.11%",
        "75.20%",
        "72.49%",
        "65.60%"
    ]
})

st.markdown("---")

st.header("🏆 Best Model")

st.success("""
Logistic Regression

Accuracy : 78.75%

Reason:
• Fast Prediction
• Easy to Interpret
• Good Generalization
• Suitable for Binary Classification
""")

st.markdown("---")

st.header("🛠 Technologies Used")

st.write("""
• Python

• Pandas

• NumPy

• Matplotlib

• Seaborn

• Scikit-Learn

• Streamlit

• Pickle
""")

st.markdown("---")

st.header("📈 Business Impact")

st.info("""
• Identify customers at high risk of churn

• Improve customer retention strategies

• Reduce revenue loss

• Support data-driven business decisions

• Enable targeted marketing campaigns
""")

st.markdown("---")

st.header("🚀 Future Improvements")

st.write("""
✔ XGBoost

✔ LightGBM

✔ Hyperparameter Tuning

✔ SHAP Explainability

✔ Database Integration

✔ Real-Time Prediction API

✔ Cloud Deployment
""")

st.markdown("---")

st.header("🧠 Explainable AI")

st.success("""
This project uses SHAP (SHapley Additive exPlanations)
to improve model interpretability by showing
which features influence churn predictions.
""")

st.markdown("---")

st.header("👨‍💻 Developer")

st.success("""
Renuka Chand

Aspiring Data Scientist

Skills:
Python | SQL | Power BI | Machine Learning | Streamlit
""")