import pickle
import requests
from flask import Flask, request, jsonify, render_template, send_from_directory, redirect
import os
import random
import pandas as pd
import time
import json
import urllib.parse

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the movie list and similarity matrix
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Use the provided API key
TMDB_API_KEY = "c1a1248fca735c015639fb65afe3fde6"

def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API with retry logic"""
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            print(f"Fetching poster for movie ID: {movie_id} (Attempt {retry_count + 1})")
            
            
            if not movie_id or pd.isna(movie_id):
                print(f"Invalid movie ID: {movie_id}")
                return get_placeholder_image("No Poster Available", movie_id)
            
            # Make API request
            url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
            response = requests.get(url, timeout=3)
            
            
            if response.status_code != 200:
                print(f"API error: Status {response.status_code} for movie ID {movie_id}")
                
                if response.status_code in [401, 404]:
                    return get_placeholder_image(f"Movie Not Found", movie_id)
                
                retry_count += 1
                if retry_count < max_retries:
                    time.sleep(1)  
                    continue
                return get_placeholder_image(f"API Error", movie_id)
                
            data = response.json()
            
            # Check if poster path exists
            if 'poster_path' in data and data['poster_path']:
                poster_path = data['poster_path']
                full_path = "https://image.tmdb.org/t/p/w500" + poster_path
                print(f"Found poster: {full_path}")
                return full_path
            else:
                print(f"No poster found for movie ID {movie_id}")
                return get_placeholder_image(f"{data.get('title', 'No Title')}", movie_id)
        
        except requests.exceptions.Timeout:
            print(f"Timeout error fetching poster for movie ID {movie_id}")
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(1)  
                continue
            return get_placeholder_image("Timeout", movie_id)
            
        except requests.exceptions.ConnectionError:
            print(f"Connection error fetching poster for movie ID {movie_id}")
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(1)  
                continue
            return get_placeholder_image("Connection Error", movie_id)
            
        except Exception as e:
            print(f"Error fetching poster for movie ID {movie_id}: {e}")
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(1)  
                continue
            return get_placeholder_image("Error", movie_id)

def get_placeholder_image(message, movie_id):
    """Generate a placeholder image URL with a message"""
    encoded_message = urllib.parse.quote(message)
    placeholder = f"https://via.placeholder.com/500x750/222222/e50914?text={encoded_message}"
    return placeholder

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        
        for i in distances[1:6]:
            # Get movie info
            movie_id = int(movies.iloc[i[0]].id)
            movie_title = movies.iloc[i[0]].title
            
            # Fetch the movie poster
            poster_url = fetch_poster(movie_id)
            
            recommended_movie_posters.append(poster_url)
            recommended_movie_names.append(movie_title)

        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        print(f"Error in recommend function: {e}")
        # Return empty recommendations in case of error
        return [], []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_movies', methods=['GET'])
def get_movies():
    movie_list = movies['title'].values.tolist()
    return jsonify(movie_list)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    movie = data['movie']
    recommended_movie_names, recommended_movie_posters = recommend(movie)
    
    recommendations = []
    for i in range(len(recommended_movie_names)):
        recommendations.append({
            'title': recommended_movie_names[i],
            'poster': recommended_movie_posters[i]
        })
    
    return jsonify(recommendations)

@app.route('/api/placeholder/<int:id>')
def placeholder_image(id):
    # Use a more reliable placeholder image service
    return redirect(f"https://via.placeholder.com/500x750/222222/e50914?text=MovieMatch")

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('artifacts', exist_ok=True)
    
    app.run(debug=True)
