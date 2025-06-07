import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import os

# === Load the cleaned dataset ===
file_path = 'cleaned_netflix_titles_with_mood.csv'
netflix_df = pd.read_csv(file_path)

# === Combine metadata for TF-IDF ===
netflix_df['metadata'] = netflix_df[['title', 'director', 'cast', 'country', 'listed_in', 'mood']].fillna('').agg(' '.join, axis=1)

# === Compute TF-IDF matrix ===
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(netflix_df['metadata'])

# === Compute cosine similarity matrix ===
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# === Poster Fetching Function ===
def get_poster(title):
    api_key = os.getenv('OMDB_API_KEY', '73ef2faf')  # Use environment variable or fallback
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    fallback_url = 'https://via.placeholder.com/300x450?text=No+Image'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('Poster', fallback_url)
    except Exception:
        return fallback_url

# === Mood-Based Recommendation Function ===
def get_mood_based_recommendations(mood, netflix_df=netflix_df, cosine_sim=cosine_sim):
    try:
        # Filter movies by suggested mood
        mood_movies = netflix_df[netflix_df['suggested_mood'].str.contains(mood, case=False, na=False)]
        print(f"Filtering mood: {mood}")
        print("Matching entries:\n", mood_movies[['title', 'suggested_mood']].head())

        if mood_movies.empty:
            return [], [], []  # No mood-based match

        # Pick a random movie from filtered mood-based DataFrame
        random_index = mood_movies.sample(1).index[0]
        idx = netflix_df.index.get_loc(random_index)  # Ensure valid similarity index

        # Get top 20 similar movies (excluding the same movie)
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:21]
        movie_indices = [i[0] for i in sim_scores]

        # Generate title, poster, and link lists
        titles = netflix_df['title'].iloc[movie_indices].tolist()
        posters = [get_poster(title) for title in titles]
        links = [f'https://www.netflix.com/search?q={title.replace(" ", "%20")}' for title in titles]

        return titles, posters, links

    except Exception as e:
        return [f"Error: {str(e)}"], [], []

# === Example Usage ===
# mood = 'happy'
# titles, posters, links = get_mood_based_recommendations(mood)
# print(titles)
