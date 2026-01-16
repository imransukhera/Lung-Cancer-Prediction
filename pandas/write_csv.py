# %%

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
# Using for the display data in. table view
from IPython.display import display
# Import the csv file
import os
df = pd.read_csv(os.path.expanduser('~/Downloads/dataset.csv'))

display(df)
plt.figure(figsize=(5,4))
sns.countplot(x="LUNG_CANCER", data=df, palette=["#4CAF50", "#F44336"])
plt.title("Lung Cancer Distribution")
plt.xlabel("Lung Cancer (YES / NO)")
plt.ylabel("Number of People")
plt.legend(
    handles=[
        Rectangle((0,0),1,1,color="#4CAF50"),
        Rectangle((0,0),1,1,color="#F44336")
    ],
    labels=["NO", "YES"],
    title="Lung Cancer",
    loc="lower left"
)
# plt.savefig("D:\\ML_Project\\plot10_lung_cancer.png", dpi=300, bbox_inches="tight")
plt.show()

# 4️⃣ Pie Chart (Lung Cancer Ratio)
# -------------------------------
cancer_counts = df["LUNG_CANCER"].value_counts()

plt.figure(figsize=(5,4))
plt.pie(
    cancer_counts,
    labels=["NO", "YES"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#4CAF50", "#F44336"]
)
plt.title("Lung Cancer Percentage Distribution")
# plt.savefig("D:\\ML_Project\\plot11_pie_chart.png", dpi=300, bbox_inches="tight")
plt.show()


# -------------------------------
# 5️⃣ Age Distribution (Histogram)
# -------------------------------
plt.figure(figsize=(5,4))
sns.histplot(df["AGE"], bins=20, kde=True, color="#03A9F4")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
# plt.savefig("D:\\ML_Project\\plot12_age.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# 6️⃣ Scatter Plot (Age vs Smoking)
# -------------------------------
plt.figure(figsize=(5,4))
sns.scatterplot(
    x="AGE",
    y="SMOKING",
    hue="LUNG_CANCER",
    data=df,
    palette=["#4CAF50", "#F44336"]
)
plt.title("Scatter Plot: Age vs Smoking")
plt.xlabel("Age")
plt.ylabel("Smoking (0 = No, 1 = Yes)")
plt.legend(title="Lung Cancer", labels=["No", "Yes"])
# plt.savefig("D:\\ML_Project\\plot13_scatter.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# 7️⃣ Cancer Patients Only
# -------------------------------
cancer_df = df[df["LUNG_CANCER"] == "YES"]

# -------------------------------
# 8️⃣ Smoking (Cancer Patients)
# -------------------------------
plt.figure(figsize=(5,4))
sns.countplot(x="SMOKING", data=cancer_df, palette=["#2196F3", "#FF9800"])
plt.title("Smoking Status of Lung Cancer Patients")
plt.xlabel("Smoking (0 = No, 1 = Yes)")
plt.ylabel("Number of People")
# plt.savefig("D:\\ML_Project\\plot14_smoking.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# 9️⃣ Gender (Cancer Patients)
# -------------------------------
plt.figure(figsize=(5,4))
sns.countplot(x="GENDER", data=cancer_df, palette=["#9C27B0", "#3F51B5"])
plt.title("Gender Distribution of Lung Cancer Patients")
plt.xlabel("Gender")
plt.ylabel("Number of People")
# plt.savefig("D:\\ML_Project\\plot15_gender.png", dpi=300, bbox_inches="tight")
plt.show()

# -------------------------------
# 🔟 Data Preprocessing
# -------------------------------
le = LabelEncoder()
df["GENDER"] = le.fit_transform(df["GENDER"])   # Female=0, Male=1
df["LUNG_CANCER"] = df["LUNG_CANCER"].map({"YES": 1, "NO": 0})

X = df.drop("LUNG_CANCER", axis=1)
y = df["LUNG_CANCER"]

# -------------------------------
# 1️⃣1️⃣ Train Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 1️⃣2️⃣ Logistic Regression Model
# -------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("\n✅ Logistic Regression Accuracy:", accuracy_score(y_test, y_pred))

# %%
