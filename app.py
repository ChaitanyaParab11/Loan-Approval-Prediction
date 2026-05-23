import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan_pipeline.pkl")

st.title("Loan Approval Prediction")

# ---------- Numeric Inputs ----------

age = st.number_input(
"Age",
18,
100,
35
)

dependents = st.number_input(
"Dependents",
0,
10,
1
)

annual_income = st.number_input(
"Annual Income",
20000,
200000,
80000
)

monthly_expenses = st.number_input(
"Monthly Expenses",
500,
10000,
3000
)

credit_score = st.number_input(
"Credit Score",
300,
900,
700
)

existing_loans = st.number_input(
"Existing Loans",
0,
5,
1
)

total_existing_loan = st.number_input(
"Total Existing Loan Amount",
0,
100000,
20000
)

outstanding_debt = st.number_input(
"Outstanding Debt",
0,
100000,
10000
)

loan_amount = st.number_input(
"Loan Amount Requested",
5000,
100000,
20000
)

loan_term = st.number_input(
"Loan Term (months)",
12,
300,
120
)

interest_rate = st.number_input(
"Interest Rate",
1.0,
20.0,
8.0
)

bank_history = st.number_input(
"Bank Account History",
0,
10,
5
)

transaction_freq = st.number_input(
"Transaction Frequency",
1,
50,
15
)

default_risk = st.slider(
"Default Risk",
0.0,
1.0,
0.5
)

loan_history = st.selectbox(
"Loan History",
[0,1]
)

# ---------- Categorical Inputs ----------

gender = st.selectbox(
"Gender",
["Male","Female"]
)

marital_status = st.selectbox(
"Marital Status",
["Single","Married","Divorced"]
)

education = st.selectbox(
"Education",
[
"High School",
"Graduate",
"Post Graduate"
]
)

employment = st.selectbox(
"Employment Status",
[
"Unemployed",
"Self Employed",
"Salaried"
]
)

occupation = st.selectbox(
"Occupation Type",
[
"Type1",
"Type2",
"Type3",
"Type4"
]
)

residential = st.selectbox(
"Residential Status",
[
"Owned",
"Rented",
"Family"
]
)

city = st.selectbox(
"City/Town",
[
"City1",
"City2",
"City3"
]
)

loan_purpose = st.selectbox(
"Loan Purpose",
[
"Personal",
"Business",
"Education",
"Home"
]
)

loan_type = st.selectbox(
"Loan Type",
[
"Secured",
"Unsecured"
]
)

co_applicant = st.selectbox(
"Co Applicant",
[
"No",
"Yes"
]
)

# ---------- Feature Engineering ----------

monthly_income = annual_income / 12

debt_per_loan = (
total_existing_loan /
max(existing_loans,1)
)

income_to_loan_ratio = (
annual_income /
loan_amount
)

loan_burden = (
total_existing_loan /
annual_income
)

emi_capacity = (
(monthly_income-monthly_expenses)
/
monthly_income
)

expense_ratio = (
monthly_expenses /
monthly_income
)

# ---------- Prediction ----------

if st.button(
"Predict Loan Approval"
):

    data = pd.DataFrame({

    "Gender":[gender],

    "Age":[age],

    "Marital_Status":
    [marital_status],

    "Dependents":
    [dependents],

    "Education":
    [education],

    "Employment_Status":
    [employment],

    "Occupation_Type":
    [occupation],

    "Residential_Status":
    [residential],

    "City/Town":
    [city],

    "Annual_Income":
    [annual_income],

    "Monthly_Expenses":
    [monthly_expenses],

    "Credit_Score":
    [credit_score],

    "Existing_Loans":
    [existing_loans],

    "Total_Existing_Loan_Amount":
    [total_existing_loan],

    "Outstanding_Debt":
    [outstanding_debt],

    "Loan_History":
    [loan_history],

    "Loan_Amount_Requested":
    [loan_amount],

    "Loan_Term":
    [loan_term],

    "Loan_Purpose":
    [loan_purpose],

    "Interest_Rate":
    [interest_rate],

    "Loan_Type":
    [loan_type],

    "Co-Applicant":
    [co_applicant],

    "Bank_Account_History":
    [bank_history],

    "Transaction_Frequency":
    [transaction_freq],

    "Default_Risk":
    [default_risk],

    "Monthly_Income":
    [monthly_income],

    "debt_per_loan":
    [debt_per_loan],

    "income_to_loan_ratio":
    [income_to_loan_ratio],

    "loan_burden":
    [loan_burden],

    "emi_capacity":
    [emi_capacity],

    "expense_ratio":
    [expense_ratio]

    })

    prediction = model.predict(
    data
    )

    if prediction[0]==1:
        st.success(
        "Loan Approved"
        )
    else:
        st.error(
        "Loan Rejected"
        )