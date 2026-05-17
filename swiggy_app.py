import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load files
cleaned_data = pd.read_csv("cleaned_data.csv")
encoded_data = pd.read_csv("encoded_data.csv")

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

st.title("🍽️ Swiggy Restaurant Recommendation System")
st.divider()

# User Inputs
city = st.selectbox("Select City", cleaned_data['city'].unique())
cuisine = st.selectbox("Select Cuisine", cleaned_data['cuisine'].unique())
rating = st.slider("Minimum Rating", 1.0, 5.0, 3.5)
cost = st.slider("Maximum Cost (₹)", 50, 1000, 300)

if st.button("Recommend Restaurants"):
    
    filtered_mask = (
        (cleaned_data['city'] == city) &
        (cleaned_data['rating'] >= rating) &
        (cleaned_data['cost'] <= cost)
    )

    filtered_cleaned = cleaned_data[filtered_mask]
    filtered_encoded = encoded_data[filtered_mask]

    if len(filtered_cleaned) == 0:
        st.warning("No restaurants match your filters.")
        st.stop()

    user_cat = encoder.transform([[city, cuisine]])
    user_vector = np.concatenate([[rating, 50, cost], user_cat[0]])

    similarity = cosine_similarity([user_vector], filtered_encoded)[0]
    
    cuisine_match = filtered_cleaned['cuisine'].str.contains(cuisine, case=False)
    similarity_boosted = similarity + (cuisine_match.astype(int) * 0.3)

    top_indices = similarity_boosted.argsort()[::-1][:5]
    results = filtered_cleaned.iloc[top_indices]

    st.divider()

    st.subheader("Similarity Score")
    st.markdown(f"**Max similarity:** {similarity.max():.4f}")
    st.markdown(f"**Mean similarity:** {similarity.mean():.4f}")
    
    st.divider()

    st.subheader("Recommended Restaurants")
    st.dataframe(results[['name', 'city', 'cuisine', 'rating', 'cost']])