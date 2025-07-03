


# 🧠 Unsupervised Learning: Customer Segmentation

This project uses **K-Means Clustering** to segment customers based on their purchasing behavior using the **Mall Customers Dataset**. The goal is to identify distinct customer groups that businesses can target more effectively.

---

## 📁 Project Structure

```

UNSUPERVISED-LEARNING/
│
├── backend/                        # Python virtual environment
│
├── notebook/
│   └── customer\_segmentation.ipynb # Jupyter notebook (EDA + clustering)
│
├── scripts/
│   └── clustering.py               # Python script for clustering
│
├── Mall\_Customers.csv              # Dataset file
├── app.py                          # (Optional) for future app deployment
└── README.md                       # Project documentation

````

---

## 📌 Problem Statement

Companies want to understand customer behavior to:

- Personalize marketing strategies
- Improve customer satisfaction
- Increase revenue through customer segmentation

This project uses **unsupervised learning** (no labels) to discover natural patterns in the customer data.

---

## 📊 Dataset Overview

**File Used:** `Mall_Customers.csv`

**Features Selected:**

- `Annual Income (k$)`
- `Spending Score (1-100)`

These features are ideal for visualizing customer purchasing power and behavior.

---

## ⚙️ How It Works

### 🔹 Step 1: Data Preprocessing

- Load data using `pandas`
- Select relevant columns
- Standardize values using `StandardScaler`

### 🔹 Step 2: Clustering

- Use `KMeans` algorithm from scikit-learn
- Assign cluster labels to each customer
- Add labels as a new column in the DataFrame

### 🔹 Step 3: Visualization

- Use `seaborn` and `matplotlib` to plot clusters
- Each cluster has a distinct color
- Shows segmentation clearly on a 2D scatter plot

---

## 🧪 How to Run This Project Locally

Follow these steps to run the project on your system:

### ✅ Step 1: Clone or Download the Repository

```bash
git clone https://github.com/yourusername/unsupervised-customer-segmentation.git
cd unsupervised-customer-segmentation
````

> Alternatively, if you have this on your Desktop, open the folder in terminal or VS Code.

---

### ✅ Step 2: Create and Activate a Virtual Environment

#### For Windows:

```bash
python -m venv backend
backend\Scripts\activate
```

#### For macOS/Linux:

```bash
python3 -m venv backend
source backend/bin/activate
```

---

### ✅ Step 3: Install Required Packages

```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

### ✅ Step 4: Add the Dataset

Make sure `Mall_Customers.csv` is located in the root of your project directory.

If it's not, place it manually or update the path in `clustering.py`.

---

### ✅ Step 5: Run the Python Script

```bash
python scripts/clustering.py
```

You will see:

* A **scatter plot** of customer segments
* A printed DataFrame showing sample rows with cluster labels
* A count of customers per cluster

---



---

## ✅ Output

* Clustered visualization of customers by income and spending
* Cluster counts and customer segmentation DataFrame
* Clear insights for targeted marketing and business strategies

---

## 🛠️ Requirements

* Python 3.7+
* Libraries:

  ```bash
  pip install pandas scikit-learn matplotlib seaborn

  run the code python scripts/clustering.py
  ```

---


---




