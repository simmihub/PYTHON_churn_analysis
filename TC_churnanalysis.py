import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\simmi\\OneDrive\\Documents\\PYTHON_churnproject1\\Customer Churn.csv")

print("\nFetching the first 5 rows of the dataset......\n")
print(df.head())

print("\nDisplaying information about the dataset......\n")
df.info()

print("Changing datatype of TotalCharges column to float.....  \n")
df["TotalCharges"] = df["TotalCharges"].replace(" ","0").astype(float)
df.info()

print("\nChecking for null values...\n")
print(df.isnull().sum())

print("\nDescriptive statistics for the dataset......\n")
print(df.describe())

print("\nChecking for duplicate in the dataset......\n")
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate customerID values:", df["customerID"].duplicated().sum())

print("\nConverting 0/1 values of SeniorCitizen to yes/no......\n")
def conv(value):
    if value == 1:
        return "yes"
    return "no"

df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
print(df.head())

print("\nChecking the distribution of Churn column......\n")
plt.figure(figsize=(4,4))
ax = sns.countplot(x=df["Churn"])
ax.bar_label(ax.containers[0])
plt.title("Count of customer by churn")
#plt.show()

print("\nChecking the distribution of Churn column in percentage......\n")
plt.figure(figsize=(4,4))
gb = df.groupby("Churn").agg({"Churn":"count"})
plt.pie(gb["Churn"],labels = gb.index,autopct = "%1.2f%%")
plt.title("Percentage of customer by churn")
#plt.show()

#From the pie chart, we can conclude 26.54 have churned out. Now, let's explore the reason behind it.

print("\nChecking the distribution of Churn on the basis of gender and SeniorCitizen......\n")
plt.figure(figsize=(3,3))
sns.countplot(data=df, x="gender", hue="Churn")
plt.title("Churn by gender")
#plt.show()

print("\nChecking the distribution of Churn on the basis of SeniorCitizen......\n")
plt.figure(figsize=(4,4))
ax = sns.countplot(data=df, x="SeniorCitizen")
ax.bar_label(ax.containers[0])
plt.title("Count of customers by SeniorCitizen")

print("\nChecking the percentage of customers who churned and did not churn within each SeniorCitizen category.......  \n")
total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack() * 100

# Plot
fig, ax = plt.subplots(figsize=(4, 4))  # Adjust figsize for better visualization

# Plot the bars
total_counts.plot(kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e'])  # Customize colors if desired

# Add percentage labels on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')

plt.title('Churn by Senior Citizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', bbox_to_anchor = (0.9,0.9))  # Customize legend location

#comparative a greater pecentage of people in senior citizen category have churned

print("\nChecking the distribution of Churn on the basis of tenure......\n")
plt.figure(figsize=(4,4))
sns.histplot(data=df,x = "tenure",bins = 72,hue="Churn")
plt.title("Churn by tenure")

#people who have used our services for a long time have stayed and people who have used our sevices 
#1 or 2 months  have churned

print("\nChecking the distribution of Churn on the basis of Contract......\n")
plt.figure(figsize=(4,4))
ax = sns.countplot(data=df, x="Contract",hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of customers by Contract")

#people who have month to month contract are likely to churn then from those who have 1 or 2 years or contract. 

print(df.columns.values)

columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

print("\nChecking the distribution of Churn on the basis of various services......\n")
# Number of columns for the subplot grid (you can change this)
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))  # Adjust figsize as needed

# Flatten the axes array for easy iteration (handles both 1D and 2D arrays)
axes = axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Remove empty subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()

#The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL),
# and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably 
# higher when these services are not used or are unavailable. 

print("\nChecking the distribution of Churn on the basis of PaymentMethod......\n")
plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)

#customers are likely to churn when they are using electronic check as a payment method. 

plt.show()





