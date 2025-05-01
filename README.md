# Movie Recommender System Using Machine Learning

This project is a **Movie Recommender System** that uses machine learning techniques to recommend movies based on user input. It processes movie metadata and applies content-based filtering to suggest similar movies.

## 🚀 Features

- 🎬 **Content-Based Filtering**: Recommends movies based on genres, cast, crew, keywords, and overview
- 📊 **Data Preprocessing**: Handles missing values, duplicates, and text processing (stemming and tokenization)
- 🤖 **Machine Learning**: Uses cosine similarity and `CountVectorizer` for feature extraction and similarity computation
- 💾 **Serialization**: Saves processed data and similarity matrices for efficient reuse
- 📱 **User Interface**: Interactive web interface for movie recommendations
- 📈 **Performance Optimization**: Cached computations for faster recommendations

## 📦 Project Structure

```
Movie-Recommender/
├── data/                  # Raw and processed movie data
├── models/               # Saved machine learning models
├── src/                  # Source code
│   ├── preprocessing.py  # Data preprocessing pipeline
│   ├── recommender.py    # Recommendation engine
│   └── utils.py          # Utility functions
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the movie dataset:
   - The project uses the TMDB 5000 Movie Dataset
   - Download from: [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
   - Place the dataset in the `data/` directory

5. Run the preprocessing script:
   ```bash
   python src/preprocessing.py
   ```

## 🎮 Usage

### Command Line Interface

```bash
python src/recommender.py --movie "Movie Title"
```

### Web Interface

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000`

## 📊 Dependencies

- Python 3.8+
- pandas
- scikit-learn
- numpy
- Flask
- TMDB API (optional for extended movie data)

## 📈 Performance

- Average recommendation time: < 1 second
- Memory usage optimized for large datasets
- Caching implemented for frequently accessed data

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details
