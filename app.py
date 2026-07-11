import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("models/churn_model.pkl","rb") as file:
    model=pickle.load(file)

with open("models/scaler.pkl","rb") as file:
    scaler=pickle.load(file)

with open("models/feature_names.pkl","rb") as file:
    feature_names=pickle.load(file)
    
# Load Dataset
df = pd.read_csv("data/cleaned_churn.csv")

total_customers = len(df)

churn_customers = len(df[df["Churn"] == 1])

retained_customers = len(df[df["Churn"] == 0])

churn_rate = round((churn_customers/total_customers)*100,2)


with st.sidebar:

    st.title("📊 Dashboard")

    st.markdown("---")

    st.header("Project")

    st.write("Customer Churn Prediction")

    st.markdown("---")

    st.header("Machine Learning")

    st.write("Model : Logistic Regression")

    st.write("Accuracy : 78.75%")

    st.write("Features : 30")

    st.markdown("---")

    st.success("Model Loaded Successfully")
    
st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("""
Predict whether a telecom customer is likely to churn using a Machine Learning model.
""")
col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric(
        "Customers",
        "7043"
    )

with col2:
    st.metric(
        "Features",
        "30"
    )

with col3:
    st.metric(
        "Best Model",
        "Logistic Regression"
    )

with col4:
    st.metric(
        "Accuracy",
        "78.75%"
    )

st.divider()

st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])

with col2:
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    total = st.number_input("Total Charges", min_value=0.0, value=1000.0)
    
    
st.subheader("🌐 Service Information")

col3, col4 = st.columns(2)

with col3:
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col4:

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )
    
st.subheader("💳 Billing Information")

col5, col6 = st.columns(2)

with col5:

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

with col6:

    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )
st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🚀 Predict Customer Churn",
    use_container_width=True
)

if predict:

    # Create dictionary with all features initialized to 0
    input_data = {feature: 0 for feature in feature_names}

    # Numerical Features
    input_data["SeniorCitizen"] = senior
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly
    input_data["TotalCharges"] = total

    # Gender
    if gender == "Male":
        input_data["gender_Male"] = 1

    # Partner
    if partner == "Yes":
        input_data["Partner_Yes"] = 1

    # Dependents
    if dependents == "Yes":
        input_data["Dependents_Yes"] = 1

    # Phone Service
    if phone_service == "Yes":
        input_data["PhoneService_Yes"] = 1

    # Multiple Lines
    if multiple_lines == "Yes":
        input_data["MultipleLines_Yes"] = 1
    elif multiple_lines == "No phone service":
        input_data["MultipleLines_No phone service"] = 1

    # Internet Service
    if internet == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1
    elif internet == "No":
        input_data["InternetService_No"] = 1

    # Online Security
    if online_security == "Yes":
        input_data["OnlineSecurity_Yes"] = 1
    elif online_security == "No internet service":
        input_data["OnlineSecurity_No internet service"] = 1

    # Online Backup
    if online_backup == "Yes":
        input_data["OnlineBackup_Yes"] = 1
    elif online_backup == "No internet service":
        input_data["OnlineBackup_No internet service"] = 1

    # Device Protection
    if device_protection == "Yes":
        input_data["DeviceProtection_Yes"] = 1
    elif device_protection == "No internet service":
        input_data["DeviceProtection_No internet service"] = 1

    # Tech Support
    if tech_support == "Yes":
        input_data["TechSupport_Yes"] = 1
    elif tech_support == "No internet service":
        input_data["TechSupport_No internet service"] = 1

    # Streaming TV
    if streaming_tv == "Yes":
        input_data["StreamingTV_Yes"] = 1
    elif streaming_tv == "No internet service":
        input_data["StreamingTV_No internet service"] = 1

    # Streaming Movies
    if streaming_movies == "Yes":
        input_data["StreamingMovies_Yes"] = 1
    elif streaming_movies == "No internet service":
        input_data["StreamingMovies_No internet service"] = 1

    # Contract
    if contract == "One year":
        input_data["Contract_One year"] = 1
    elif contract == "Two year":
        input_data["Contract_Two year"] = 1

    # Paperless Billing
    if paperless == "Yes":
        input_data["PaperlessBilling_Yes"] = 1

    # Payment Method
    if payment == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1
    elif payment == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1
    elif payment == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Scale Data
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]
    
    st.divider()

    st.subheader("📊 Prediction Result")
    
    if prediction == 1:

        st.error("⚠️ Customer is likely to Churn")

        st.progress(float(probability))

        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

        st.info("""
### Recommendation

• Offer Loyalty Discount

• Offer One-Year Contract

• Assign Customer Support Executive

• Send Promotional Offers
""")
    else:

        st.success("✅ Customer is NOT likely to Churn")

        st.progress(float(probability))

        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

        st.info("""
### Recommendation

• Customer is Loyal

• Continue Regular Service

• Offer Premium Plans

• Maintain Customer Satisfaction
""")
        



st.divider()

st.subheader("📈 Dataset Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Total Customers",
        total_customers
    )

with c2:
    st.metric(
        "❌ Churn Customers",
        churn_customers
    )

with c3:
    st.metric(
        "✅ Retained Customers",
        retained_customers
    )

with c4:
    st.metric(
        "📊 Churn Rate",
        f"{churn_rate}%"
    )

st.divider()

st.header("📊 Business Insights Dashboard")

# ==========================
# First Row
# ==========================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Churn Distribution")

    fig = px.pie(
    df,
    names="Churn",
    title="Customer Churn Distribution",
    color="Churn",
    color_discrete_sequence=["#00CC96", "#EF553B"]
    )

    fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )

with col2:

    st.subheader("📃 Contract Type vs Churn")

    fig = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group",
    title="Contract Type vs Churn"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )

# ==========================
# Second Row
# ==========================

col3, col4 = st.columns(2)

with col3:

    st.subheader("🌐 Internet Service vs Churn")

    fig = px.histogram(
    df,
    x="InternetService",
    color="Churn",
    title="Internet Service vs Churn"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )

with col4:

    st.subheader("💰 Monthly Charges Distribution")

    ffig = px.histogram(
    df,
    x="MonthlyCharges",
    color="Churn",
    nbins=30,
    title="Monthly Charges Distribution"
    )

    st.plotly_chart(
    ffig,
    use_container_width=True
    )
    
col5, col6 = st.columns(2)
with col5:
    st.subheader("📊 Tenure vs Churn")

    fig = px.box(
    df,
    x="Churn",
    y="tenure",
    color="Churn",
    title="Tenure vs Churn"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
   )
    
with col6:
    st.subheader("👥 Gender vs Churn")
    
    fig = px.histogram(
    df,
    x="gender",
    color="Churn",
    barmode="group",
    title="Gender vs Churn"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )

col7, col8 = st.columns(2)
with col7:
    st.subheader("💳 Payment Method vs Churn")
    
    fig = px.histogram(
    df,
    x="PaymentMethod",
    color="Churn",
    title="Payment Method vs Churn"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )

numeric_df = df.copy()

for col in numeric_df.columns:
    if numeric_df[col].dtype == "object":
        numeric_df[col] = numeric_df[col].astype("category").cat.codes

corr = numeric_df.corr()

fig = px.imshow(
    corr,
    text_auto=False,
    color_continuous_scale="RdBu_r",
    title="Feature Correlation Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.markdown(
"""
<center>

Made with ❤️ using

Python • Streamlit • Scikit-Learn • Pandas • Matplotlib

</center>
""",
    unsafe_allow_html=True
)

st.divider()

st.header("🧠 Model Explainability")

st.write("""
The SHAP Summary Plot explains which features have the greatest impact
on customer churn prediction.
""")

st.image(
    "images/shap_summary.png",
    caption="SHAP Feature Importance",
    use_container_width=True
)