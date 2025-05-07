import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

print("Loading data...")
movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

print("Movies shape:", movies.shape)
print("Credits shape:", credits.shape)
print("\nMovies columns:", movies.columns.tolist())
print("Credits columns:", credits.columns.tolist())


credits = credits.rename(columns={'movie_id': 'id'})


print("\nMerging datasets...")
movies = movies.merge(credits, on='id')

print("Merged shape:", movies.shape)
print("Merged columns:", movies.columns.tolist())


print("\nProcessing movie features...")

movies['overview'] = movies['overview'].fillna('')
movies['genres'] = movies['genres'].fillna('')
movies['keywords'] = movies['keywords'].fillna('')

movies['tags'] = movies['overview'] + ' ' + movies['genres'] + ' ' + movies['keywords']


new_df = movies[['id', 'title_x', 'tags']]
new_df = new_df.rename(columns={'title_x': 'title'})


duplicate_titles = new_df['title'].duplicated()
if duplicate_titles.any():
    print("\nWarning: Found duplicate movie titles:")
    print(new_df[new_df['title'].duplicated(keep=False)]['title'].unique())


print("\nCreating feature vectors...")
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new_df['tags']).toarray()


print("\nCalculating similarity matrix...")
similarity = cosine_similarity(vector)
print(f"Similarity matrix shape: {similarity.shape}")


os.makedirs('artifacts', exist_ok=True)


print("\nSaving model files...")
pickle.dump(new_df, open('artifacts/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('artifacts/similarity.pkl', 'wb'))

print("Done! Model files have been generated successfully.") 
