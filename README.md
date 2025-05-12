![Image](https://github.com/user-attachments/assets/3e4e1bc1-6a43-494d-a163-967c4c0b8dd2)

## About
A sophisticated movie recommendation engine that combines machine learning with an interactive web interface to deliver personalized movie suggestions based on user preferences.

![Movie Recommender](https://img.shields.io/badge/Project-Movie%20Recommender-orange)
![ML](https://img.shields.io/badge/Machine%20Learning-Content--Based-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Web](https://img.shields.io/badge/Web-HTML%2FCSS%2FJS-yellow)

### YouTube Video - [Click here](https://www.youtube.com/watch?v=9F2yq7q5Q9s)

## Features

- **Intelligent Recommendations**: Uses content-based filtering to suggest movies similar to your favorites
- **Responsive Web Interface**: Built with modern HTML, CSS, and JavaScript for a seamless user experience
- **Advanced ML Pipeline**: Processes movie metadata including genres, cast, crew, and plot details
- **Fast Performance**: Optimized algorithms with cached computations for instant recommendations
- **Interactive Experience**: Dynamic content loading and responsive design for all devices

## Tech Stacks

![Python](https://img.shields.io/badge/Python-%233776ab.svg?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-%23f05032.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## Installation & Setup

1. **Fork and Clone the repository**:
   ```bash
   git clone https://github.com/shondsouza/Movie-recommendation-system.git
   cd Movie-recommendation-system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Dataset setup**:
   - Download the TMDB 5000 Movie Dataset from Kaggle
   - Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the `data/` directory

5. **Process the data**:
   ```bash
   python src/preprocessing.py
   ```

## Running the Application

1. **Start the web server**:
   ```bash
   python app.py
   ```

2. **Access the web interface**:
   - Open your browser and go to `http://localhost:5000`
   - Search for a movie and get personalized recommendations!

3. **Alternatively, use the CLI**:
   ```bash
   python src/recommender.py --movie "Movie Title"
   ```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
