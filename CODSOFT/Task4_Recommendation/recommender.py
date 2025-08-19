# recommendation.py
# CODSOFT - Task 4: Simple Movie Recommendation System
# Content-based filtering using TF-IDF and Cosine Similarity

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# Sample Movie Dataset
# ---------------------------
data = {
    "title": [
        "Inception", "Interstellar", "The Dark Knight",
        "The Prestige", "Avengers: Endgame", "Iron Man",
        "The Matrix", "John Wick", "Gladiator"
    ],
    "genre": [
        "sci-fi thriller", "sci-fi drama", "action superhero",
        "mystery thriller", "superhero action", "superhero sci-fi",
        "sci-fi action", "action thriller", "historical action"
    ]
}

df = pd.DataFrame(data)

# ---------------------------
# TF-IDF + Cosine Similarity
# ---------------------------
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["genre"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# ---------------------------
# Recommendation Function
# ---------------------------
def recommend(movie_title):
    movie_title = movie_title.strip().lower()  # normalize input
    titles = df["title"].str.lower().tolist()  # normalize dataset

    if movie_title not in titles:
        return ["⚠️ Movie not found in database."]
    
    idx = titles.index(movie_title)  # index of selected movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # top 3 recommendations
    
    recommended_movies = [df.iloc[i[0]]["title"] for i in sim_scores]
    return recommended_movies

# ---------------------------
# Run Program
# ---------------------------
if __name__ == "__main__":
    print("🎬 Movie Recommendation System")
    print("Available movies:", ", ".join(df["title"].tolist()))

    movie = input("\nEnter a movie title: ")
    results = recommend(movie)

    print(f"\nBecause you watched '{movie}', we recommend:")
    for r in results:
        print("👉", r)
