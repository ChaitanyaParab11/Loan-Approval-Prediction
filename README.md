## Run locally

pip install -r requirements.txt

streamlit run app.py

# 💳 Loan Approval Prediction using Machine Learning

## 📌 Problem Statement

The objective of this project was to predict whether a loan application would be approved or rejected based on applicant financial details, credit profile, loan history and existing debt information.

Target Variable:

`Loan_Approval_Status`

Classification task:

0 = Rejected  
1 = Approved

Dataset size:

~52,000 records

---

## 📊 Dataset Understanding

The dataset contained:

Financial information:
- Annual Income
- Monthly Income
- Monthly Expenses
- Outstanding Debt
- Existing Loans
- Total Existing Loan Amount

Loan details:
- Requested Loan Amount
- Loan Term
- Interest Rate
- Loan Type

Risk indicators:
- Credit Score
- Loan History
- Default Risk
- Bank Account History

Personal profile:
- Age
- Dependents
- Employment
- Marital Status
- Co-applicant

---

## 🧠 Business Understanding

High Risk Customer:

- Low income with high loan amount
- Multiple existing loans
- Poor credit score
- Bad repayment history
- High debt burden
- Unsecured loans
- No co-applicant

Low Risk Customer:

- High income
- Good credit score
- Low debt burden
- Co-applicant available
- Secured loans
- Stable repayment history

---

## 🤖 Models Trained

1. Logistic Regression

Accuracy: 85.57%

Precision: 85.74%

Recall: 93.47%

F1 Score: 89.43%

2. Decision Tree Classifier

Initial tree:

Accuracy ≈ 73%

After tuning:

max_depth = 5

Accuracy improved to:

85.51%

Observation:

Initial model overfit heavily. Restricting depth improved generalization.

3. Random Forest Classifier

Accuracy: 85.57%

Precision: 85.77%

Recall: 93.44%

F1 Score: 89.44%

Random Forest performed best overall.

---

## 📈 Important Features

Top contributing features:

Credit Score → 0.19
Loan Amount Requested → 0.15
Annual Income → 0.07
Monthly Income → 0.07
Age → 0.05
income_to_loan_ratio → 0.04
expense_ratio → 0.04
loan_burden → 0.04
emi_capacity → 0.04

---

## Interesting Failure Cases

Example:

Customer:

Income = 77866

Monthly Expenses = 3751

Debt Per Loan = 36874

Credit Score = 788

Actual Result:

Rejected

Model Prediction:

Approved

Reason:

Model prioritized strong credit score and income over debt exposure.

Another observation:

Some approved customers had:

Low credit score
High debt burden
Negative cash flow

These decisions conflicted with financial intuition.

This indicates hidden business rules may exist in dataset labels.

---

## 🚀 Key Learnings
Classification metrics differ from regression metrics
Accuracy alone is insufficient
Precision / Recall / F1 are important
Feature engineering significantly improves business understanding
Error analysis reveals hidden dataset behavior
Domain understanding is important for ML projects