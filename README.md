Swiggy Restaurant Recommendation System

A personalized restaurant recommendation system built with K-Means clustering, cosine similarity, and Streamlit. Filters restaurants by city, rating, cost, and cuisine preferences.

🎯 Features Data Preprocessing: Cleaned Swiggy dataset (duplicates, missing values, currency parsing).

Multi-label Cuisine Encoding: Handles "North Indian,Chinese" → binary features.

Hybrid Recommendations: Filter + NearestNeighbors similarity search.

Interactive UI: City selector, rating/cost sliders, multi-cuisine picker.

Metrics Dashboard: Median rating, avg cost, best match similarity.

📁 Project Structure text PROJECT/ ├── 📁 data/ │ ├── swiggy.csv # Raw dataset (45MB) │ ├── cleaned_data.csv # Cleaned data (no duplicates/NaNs) │ └── encoded_data.csv # One-hot encoded + numeric features ├── 📁 models/ │ ├── mlb_cuisine.pkl # MultiLabelBinarizer for cuisines │ ├── scaler.pkl # StandardScaler for features │ ├── nn_model.pkl # NearestNeighbors model │ └── kmeans_model.pkl # K-Means clusters (optional) ├── 📁 notebooks/ │ └── swiggy.ipynb # Preprocessing + model training ├── 🟡 app.py # Streamlit web app ├── 🟡 utils.py # Recommendation engine ├── 📄 README.md # This file └── 📄 .gitignore 🚀 Quick Start

Install Dependencies bash pip install streamlit pandas scikit-learn numpy jupyter

Run the App bash streamlit run app.py App opens at: http://localhost:8501

Preprocess Data (First Time Only) bash jupyter notebook notebooks/swiggy.ipynb Run all cells → Creates cleaned_data.csv, encoded_data.csv, and model .pkl files.

🎛️ How to Use Select City (e.g., "Delhi")

Set Min Rating (e.g., 3.5⭐)

Set Max Cost (e.g., ₹400)

Pick Cuisines (e.g., "North Indian", "Chinese")

Click "Get Recommendations"

Output:

Metrics: Median rating, rating count, avg cost, best similarity.

Table: Top restaurants sorted by similarity score.

🧠 Recommendation Algorithm text

Filter: city + rating ≥ X + cost ≤ ₹Y + cuisines match
Scale: encoded features with saved scaler
Similarity: NearestNeighbors(cosine) on filtered subset
Profile: Use centroid of filtered restaurants as "user profile"
Rank: Top-N by cosine similarity (1 - distance) Features Used:
text Numeric: rating, rating_count, cost Categorical: city (one-hot), cuisine (multi-label binarized) 📊 Dataset Source: Swiggy restaurant data (~45MB CSV) Columns Used: id, name, city, rating, rating_count, cost, cuisine Rows After Cleaning: ~XXK (depends on your dataset)

🛠️ Development Workflow text Day 1-2: notebooks/swiggy.ipynb (clean + encode + train) Day 3-4: utils.py (recommendation engine) Day 5-6: app.py (Streamlit UI) Day 7: Test + README 🔧 Customization Add New Features python

In utils.py recommend()
Add more filters:
mask_new_feature = df_clean["delivery_time"] <= 30 Change Algorithm python

Replace NearestNeighbors with KMeans
cluster_labels = kmeans.predict(X_scaled) similar_clusters = find_similar_clusters(user_cluster) 📈 Project Evaluation Metric Status Data Alignment Indices match between cleaned_data.csv ↔ encoded_data.csv Recommendation Quality Cosine similarity + filtered relevance App Usability Responsive UI, fast queries (<2s) Reproducibility Random seed=42, saved models/encoders 🤝 Business Value Personalized Recommendations → Higher conversion

Customer Experience → Faster decisions

Market Insights → Popular cities/cuisines

Operational Efficiency → Optimize menu offerings

📝 Report Summary Data Cleaning: Removed duplicates (X rows), imputed medians for NaNs, parsed currency. Methodology: MultiLabelBinarizer → StandardScaler → NearestNeighbors(cosine). Key Insights: Delhi has highest-rated restaurants, North Indian most popular cuisine.

🐛 Troubleshooting Issue Solution FileNotFoundError Run swiggy.ipynb first ModuleNotFoundError pip install -r requirements.txt No recommendations Lower rating/increase budget Slow app Filter fewer cities 📦 Requirements text streamlit==1.28.0 pandas==2.0.3 scikit-learn==1.3.0 numpy==1.24.3 jupyter==1.0.0 📄 License MIT License – Feel free to use/modify for portfolios, interviews, projects.

🙏 Acknowledgments Built for Swiggy Restaurant Recommendation System project. Dataset: Swiggy public restaurant data.

About
End‑to‑end restaurant recommendation system using Swiggy data, unsupervised ML (K‑Means / cosine similarity), MultiLabelBinarizer encoding, and an interactive Streamlit web app.

Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Contributors
1
@PratikMahalle28
PratikMahalle28 Pratik Mahalle
Languages
Jupyter Notebook
75.0%
 
Python
25.0%
Footer
