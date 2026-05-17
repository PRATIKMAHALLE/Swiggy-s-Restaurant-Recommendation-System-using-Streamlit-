
# 🍽️ Swiggy Restaurant Recommendation System

A Machine Learning powered restaurant recommendation system built using Python and Streamlit.
This project recommends restaurants based on user preferences like city, cuisine, rating, and budget using similarity-based recommendation.

---

## 🚀 Project Overview

This project builds a restaurant recommendation engine using:

- Data cleaning and preprocessing
- Feature encoding - One Hot Encoding
- Cosine similarity for recommendation
- Interactive Streamlit web app

Users can filter restaurants by:

- City
- Cuisine
- Minimum rating
- Maximum cost

The system then suggests the top 5 most similar restaurants.

---

## 📂 Project Structure

Swiggy-Restaurant-Recommendation/
│
├── data processing and model building.ipynb
├── cleaned_data.csv
├── encoded_data.csv
├── encoder.pkl
├── swiggy_app.py
├── requirements.txt
└── README.md

---

## 🧠 Machine Learning Approach

### Data Processing

- Removed null values and duplicates
The data set is in the string(object) values.

Duplicate removal:
Total Duplicate values in the data set is 35 as this has very minimal impact.Hence, I have dropped the duplicate values.

Null value handling:
I am extracting the numerical values from rating, rating count and cost. This is to convert the mentioned values to numericals values.
values like "--,No rating, new" are converted to NaN
Values like "+ratings" is avoided by just extracting the number before them

I have checked the difference in the impact of the droping and using imputation metiod to handle the NULL values.
Total Null values : 58.9%
However, I have dropped them in this project to reduce stress on my hardware.
I have dropped the Null values for categorical data : city and cuisine as we are only losing 0.05% of the data.

I have converted the attributes : cost, rating and rating count to numerical values as they are the input.

- Feature engineering:

I have dropped id, lic_no, name, address and menu

I have filtered only the top 20 cities to be passed as input. However, I have not filtered the cuisine.
By doing this, I have (61418, 6) also I have lost about 789 cuisine from the data.

- Categorical encoding:
I am using One Hot encoder as proided in the project requirements.
categorical_cols = ["city", "cuisine"]
numerical_cols = ["rating", "rating_count", "cost"]
Encoded dataset shape: (8495, 873)

- Feature scaling and vector preparation


### Recommendation Engine

- User input converted to feature vector
- Cosine similarity used to compare restaurants
- Cuisine-based similarity boosting
- Top 5 matches returned

---

## 📊 Features

- Interactive UI with Streamlit
- Real-time restaurant filtering
- Similarity score display
- Ranked recommendations
- Clean dashboard

---

## 🛠️ Installation

git clone https://github.com/your-username/Swiggy-Restaurant-Recommendation.git
cd Swiggy-Restaurant-Recommendation

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

---

## ▶️ Running the App

streamlit run swiggy_app.py

---

## 👨‍💻 Author

Pratik Mahalle
