import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Batch Customer Churn Prediction")

st.write("""
Upload a CSV file containing customer records to predict churn for multiple customers.
""")

# ==========================
# Load Model
# ==========================
with open("models/churn_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("models/feature_names.pkl", "rb") as file:
    feature_names = pickle.load(file)

# ==========================
# Upload CSV
# ==========================
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    uploaded = pd.read_csv(uploaded_file)
    
    st.write("Columns:")
    st.write(uploaded.columns.tolist())

    st.write("Data Types:")
    st.write(uploaded.dtypes)

    st.write("First Row")
    st.write(uploaded.head(1))

    st.subheader("📄 Uploaded Dataset")
    st.dataframe(uploaded.head(10), use_container_width=True)

    # Check Columns
    if list(uploaded.columns) != feature_names:
        st.error("❌ Uploaded CSV does not match the required feature columns.")
        st.stop()

    # ==========================
    # Prediction
    # ==========================
    if st.button("🚀 Predict All Customers", use_container_width=True):
        st.write(uploaded.iloc[0])
        uploaded_scaled = scaler.transform(uploaded)

        prediction = model.predict(uploaded_scaled)

        probability = model.predict_proba(uploaded_scaled)[:, 1]

        uploaded["Prediction"] = prediction

        uploaded["Prediction"] = uploaded["Prediction"].map({
            0: "No Churn",
            1: "Churn"
        })

        uploaded["Probability (%)"] = (probability * 100).round(2)

        st.success("✅ Prediction Completed Successfully")

        # ==========================
        # Summary Metrics
        # ==========================

        total = len(uploaded)
        churn = (uploaded["Prediction"] == "Churn").sum()
        retained = (uploaded["Prediction"] == "No Churn").sum()
        rate = churn / total * 100

        st.subheader("📊 Prediction Summary")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total Customers", total)
        c2.metric("Likely to Churn", churn)
        c3.metric("Retained Customers", retained)
        c4.metric("Churn Rate", f"{rate:.2f}%")

        st.divider()

        # ==========================
        # Prediction Table
        # ==========================

        st.subheader("📋 Prediction Results")

        def color_prediction(val):
            if val == "Churn":
                return "background-color:#ffcccc"
            else:
                return "background-color:#ccffcc"

        st.dataframe(
            uploaded.style.applymap(
                color_prediction,
                subset=["Prediction"]
            ),
            use_container_width=True
        )

        st.divider()

        # ==========================
        # Charts
        # ==========================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🥧 Churn Distribution")

            fig, ax = plt.subplots(figsize=(5,5))

            uploaded["Prediction"].value_counts().plot(
                kind="pie",
                autopct="%1.1f%%",
                startangle=90,
                ax=ax
            )

            ax.set_ylabel("")
            st.pyplot(fig)

        with col2:

            st.subheader("📊 Customer Count")

            fig, ax = plt.subplots(figsize=(5,5))

            sns.countplot(
                x="Prediction",
                data=uploaded,
                palette="Set2",
                ax=ax
            )

            st.pyplot(fig)

        st.divider()

        # ==========================
        # Insights
        # ==========================

        st.subheader("💡 Prediction Insights")

        if rate >= 50:
            st.error("⚠ High churn risk detected. Immediate customer retention strategies are recommended.")

        elif rate >= 25:
            st.warning("🟠 Moderate churn risk detected. Consider targeted promotional campaigns.")

        else:
            st.success("🟢 Customer base appears stable with low churn risk.")

        st.divider()

        # ==========================
        # Churn Customers
        # ==========================

        st.subheader("⚠ Customers Likely to Churn")

        churn_df = uploaded[uploaded["Prediction"] == "Churn"]

        if len(churn_df) > 0:
            st.dataframe(
                churn_df,
                use_container_width=True
            )
        else:
            st.success("🎉 No customers are predicted to churn.")

        st.divider()

        # ==========================
        # Download CSV
        # ==========================

        csv = uploaded.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Prediction CSV",
            data=csv,
            file_name="customer_churn_predictions.csv",
            mime="text/csv",
            use_container_width=True
        )