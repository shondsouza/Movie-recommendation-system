![Image](https://github.com/user-attachments/assets/3e4e1bc1-6a43-494d-a163-967c4c0b8dd2)

## About

A sophisticated movie recommendation engine that combines machine learning with an interactive web interface to deliver personalized movie suggestions based on user preferences.


### YouTube Video - [Click here](https://www.youtube.com/watch?v=9F2yq7q5Q9s)

## Tech Stacks

![Python](https://img.shields.io/badge/Python-%233776ab.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) 
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![CountVectorizer](https://img.shields.io/badge/CountVectorizer-ML%20Tool-informational?style=for-the-badge)
![Cosine Similarity](https://img.shields.io/badge/Cosine%20Similarity-Metric-blueviolet?style=for-the-badge)
![TMDB 5000 Movie Dataset](https://img.shields.io/badge/Dataset-TMDB%205000%20Movies-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)
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
