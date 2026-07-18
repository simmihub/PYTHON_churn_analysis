# 📉 Customer Churn Analysis using Python

## 📌 Overview

Customer churn is a key business challenge, as retaining existing customers is often more cost-effective than acquiring new ones. This project analyzes customer churn data using Python to identify patterns, explore customer behavior, and uncover factors that influence churn through data cleaning and exploratory data analysis (EDA).

---

## 🎯 Project Objectives

- Clean and preprocess customer data
- Perform exploratory data analysis (EDA)
- Visualize customer demographics and service usage
- Identify factors associated with customer churn
- Generate insights to support customer retention strategies

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

---

## 📂 Dataset

The dataset includes customer information such as:

- Customer ID
- Gender
- Senior Citizen
- Partner & Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

---

## 📊 Analysis Performed

- Data Cleaning
- Handling Missing Values
- Data Type Conversion
- Duplicate Check
- Descriptive Statistics
- Customer Churn Distribution
- Service-wise Churn Analysis
- Contract-wise Churn Analysis
- Payment Method Analysis
- Internet Service Analysis
- Monthly Charges Analysis
- Tenure Analysis

---

## 📁 Repository Structure

```
PYTHON_churn_analysis/
│
├── Dataset/
│   └── Customer Churn.csv
│
├── Notebook/
│   └── TC_churnanalysis.py
│
├── Images/
│   └── Visualizations
│
├── Report/
│   └──Telco_customer_analysis.pdf
│
└── README.md
```

---

## 📈 Visualizations and insights

### Customer Churn Distribution

![Customer Churn Distribution](Images/customer%20churn%20distribution.png)

![Percentage of Churn Distribution](Images/percentage%20of%20churn%20distribution.png)

**Insight:**
-Approximately **26.54%** of customers have churned, whereas **73.46%** remain active.

### Gender-wise Churn

![Gender-wise Churn](Images/churn%20by%20gender.png)

### Senior Citizen Analysis

![Customer Count by Senior Citizen Status](Images/customer%20count%20by%20senior%20citizen%20status.png)

![Percentage of Churn by Senior Citizen](Images/percentage%20of%20churn%20customer%20by%20senior%20citizen.png)

**Insight:**
-comparative a greater pecentage of people in senior citizen category have churned

### Contract Type Analysis

![Customer Count by Contract](Images/customer%20count%20by%20contract.png)

**Insight:**
-people who have month to month contract are likely to churn then from those who have 1 or 2 years or contract.

### Tenure Distribution

![Tenure Distribution](Images/Tenure%20distribution.png)

**Insight:**
-people who have used our services for a long time have stayed and people who have used our sevices 1 or 2 months  have churned

### Subplot

![Subplot](Images/subplot.png)

**Insight:**
-The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL),
and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably 
higher when these services are not used or are unavailable. 

### Payment Method Analysis

![Churn by Payment Method](Images/churned%20customer%20by%20payment%20method.png)

**Insight:**
-customers are likely to churn when they are using electronic check as a payment method. 

---



## 🚀 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Business Insight Generation
- Statistical Analysis
- Python Programming

---

---

⭐ If you found this project useful, feel free to star the repository!
