import streamlit as st

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance")

st.write("Evaluation of the Logistic Regression model.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Confusion Matrix")
    st.image("images/confusion_matrix.png", width="stretch")

with col2:
    st.subheader("ROC Curve")
    st.image("images/roc_curve.png", width="stretch")

st.divider()

st.subheader("Classification Report")

import pandas as pd

report = pd.read_csv("images/classification_report.csv")

st.dataframe(
    report,
    width="stretch"
)

st.divider()

st.subheader("Model Metrics")

metrics = pd.read_csv("images/model_metrics.csv")

st.dataframe(
    metrics,
    width="stretch"
)