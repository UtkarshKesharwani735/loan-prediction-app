import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan_prediction_model.pkl")

st.set_page_config(page_title="Loan Repayment Prediction")

st.title("🏦 Loan Repayment Prediction System")

st.write("Enter Applicant Information")

# User Inputs

age = st.number_input("Age", 18, 100, 25)

gender = st.selectbox("Gender", ["Male", "Female"])

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

education_level = st.selectbox(
    "Education Level",
    ["High School", "Bachelor", "Master", "PhD"]
)

annual_income = st.number_input(
    "Annual Income",
    min_value=0.0
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0
)

employment_status = st.selectbox(
    "Employment Status",
    ["Employed", "Self-employed", "Unemployed"]
)

debt_to_income_ratio = st.number_input(
    "Debt To Income Ratio",
    min_value=0.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0
)

loan_purpose = st.selectbox(
    "Loan Purpose",
    ["Home", "Business", "Education", "Personal"]
)

interest_rate = st.number_input(
    "Interest Rate",
    min_value=0.0
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1
)

installment = st.number_input(
    "Installment",
    min_value=0.0
)

grade_subgrade = st.text_input(
    "Grade Subgrade",
    value="A1"
)

num_of_open_accounts = st.number_input(
    "Open Accounts",
    min_value=0
)

total_credit_limit = st.number_input(
    "Total Credit Limit",
    min_value=0.0
)

current_balance = st.number_input(
    "Current Balance",
    min_value=0.0
)

delinquency_history = st.number_input(
    "Delinquency History",
    min_value=0
)

public_records = st.number_input(
    "Public Records",
    min_value=0
)

num_of_delinquencies = st.number_input(
    "Number of Delinquencies",
    min_value=0
)

# Encoding

gender_map = {
    "Male":0,
    "Female":1
}

marital_map = {
    "Single":0,
    "Married":1,
    "Divorced":2
}

education_map = {
    "High School":0,
    "Bachelor":1,
    "Master":2,
    "PhD":3
}

employment_map = {
    "Employed":0,
    "Self-employed":1,
    "Unemployed":2
}

loan_purpose_map = {
    "Home":0,
    "Business":1,
    "Education":2,
    "Personal":3
}

if st.button("Predict"):

    input_df = pd.DataFrame({

        "age":[age],
        "gender":[gender_map[gender]],
        "marital_status":[marital_map[marital_status]],
        "education_level":[education_map[education_level]],
        "annual_income":[annual_income],
        "monthly_income":[monthly_income],
        "employment_status":[employment_map[employment_status]],
        "debt_to_income_ratio":[debt_to_income_ratio],
        "credit_score":[credit_score],
        "loan_amount":[loan_amount],
        "loan_purpose":[loan_purpose_map[loan_purpose]],
        "interest_rate":[interest_rate],
        "loan_term":[loan_term],
        "installment":[installment],
        "grade_subgrade":[0],
        "num_of_open_accounts":[num_of_open_accounts],
        "total_credit_limit":[total_credit_limit],
        "current_balance":[current_balance],
        "delinquency_history":[delinquency_history],
        "public_records":[public_records],
        "num_of_delinquencies":[num_of_delinquencies]

    })

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ Customer is likely to repay the loan.")
    else:
        st.error("❌ High Risk: Customer may default.")