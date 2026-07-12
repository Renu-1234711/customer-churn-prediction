import streamlit as st

st.set_page_config(
    page_title="Feature Importance",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Feature Importance using SHAP")

st.write("""
SHAP (SHapley Additive exPlanations) helps explain why the model predicts
customer churn by showing the contribution of each feature.
""")

st.image(
    "images/shap_summary.png",
    caption="SHAP Summary Plot",
    width="stretch"
)

st.markdown("---")

st.subheader("📌 Interpretation")

st.markdown("""
Features at the top of the plot have the greatest influence on the prediction.

Typical influential features include:

- Contract Type
- Tenure
- Monthly Charges
- Total Charges
- Internet Service
- Tech Support
- Online Security

Red points indicate higher feature values.

Blue points indicate lower feature values.

Features pushing the prediction toward churn appear on the right side, while those reducing churn appear on the left.
""")