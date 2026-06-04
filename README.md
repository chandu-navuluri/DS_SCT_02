# DS_SCT_02 - Titanic Dataset: Data Cleaning & Exploratory Data Analysis

## 📌 Overview

This project is part of the **SkillCraft Technology Data Science Internship**.

The objective of this task is to perform **Data Cleaning** and **Exploratory Data Analysis (EDA)** on the Titanic dataset to uncover patterns, trends, and relationships between passenger characteristics and survival outcomes.

---

## 🎯 Task Objective

* Clean and preprocess the dataset.
* Handle missing values.
* Explore relationships between variables.
* Identify patterns affecting passenger survival.
* Visualize data using charts and graphs.

---

## 📊 Dataset

The Titanic dataset contains information about passengers aboard the Titanic, including:

* PassengerId
* Survived
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* VS Code

---

## 🔍 Data Cleaning Performed

* Filled missing values in the **Age** column using the median.
* Filled missing values in the **Embarked** column using the mode.
* Removed the **Cabin** column due to a large number of missing values.
* Checked dataset structure and summary statistics.

---

## 📈 Visualizations Created

* Passenger ID Distribution
* Survival Distribution
* Gender Distribution
* Survival by Gender
* Passenger Class Distribution
* Survival by Passenger Class
* Age Distribution
* Fare Distribution
* Age vs Fare Scatter Plot
* Correlation Heatmap

---

## 📌 Key Insights

1. Female passengers had a significantly higher survival rate than males.
2. First-class passengers were more likely to survive.
3. Most passengers were between 20 and 40 years old.
4. Higher ticket fares were associated with higher survival chances.
5. Passenger class and gender were important factors influencing survival.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/chandu-navuluri/DS_SCT_02.git
```

2. Navigate to the project directory:

```bash
cd DS_SCT_02
```

3. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

4. Run the script:

```bash
python task2.py
```

---

## 📂 Project Structure

```text
DS_SCT_02/
│
├── train.csv
├── test.csv
├── gender_submission.csv
├── task2.py
├── README.md
└── figures.png
```

---

## 👨‍💻 Author

**Chandu Navuluri**

GitHub: https://github.com/chandu-navuluri

---

## ⭐ Acknowledgements

* SkillCraft Technology
* Titanic Dataset (Kaggle)
* Python Data Analysis & Visualization Libraries
