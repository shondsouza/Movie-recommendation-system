document.addEventListener('DOMContentLoaded', () => {
    // DOM elements
    const customSelect = document.getElementById('custom-select');
    const selectTrigger = document.getElementById('select-trigger');
    const selectedOption = document.getElementById('selected-option');
    const selectDropdown = document.getElementById('select-dropdown');
    const selectOptions = document.getElementById('select-options');
    const selectSearch = document.getElementById('select-search');
    const recommendBtn = document.getElementById('recommend-btn');
    const loadingElement = document.getElementById('loading');
    const recommendationsElement = document.getElementById('recommendations');
    const movieGridElement = document.getElementById('movie-grid');
    const noResultsElement = document.getElementById('no-results');
    
    // Variables
    let movies = [];
    let selectedMovie = '';
    let filteredMovies = [];
    
    // Fetch all movies when the page loads
    fetchMovies();
    
    // Event listeners
    selectTrigger.addEventListener('click', toggleDropdown);
    selectSearch.addEventListener('input', filterMovies);
    recommendBtn.addEventListener('click', getRecommendations);
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (event) => {
        if (!customSelect.contains(event.target)) {
            closeDropdown();
        }
    });
    
    // Functions
    function toggleDropdown() {
        selectDropdown.classList.toggle('active');
        if (selectDropdown.classList.contains('active')) {
            selectSearch.focus();
        }
    }
    
    function closeDropdown() {
        selectDropdown.classList.remove('active');
    }
    
    async function fetchMovies() {
        try {
            // Make API call to get movies
            const response = await fetch('/get_movies');
            movies = await response.json();
            
            // Sort movies alphabetically
            movies.sort();
            filteredMovies = [...movies];
            
            populateOptions(movies);
        } catch (error) {
            console.error('Error fetching movies:', error);
            // For demonstration, use sample movies if the API fails
            movies = [
                'The Shawshank Redemption', 'The Godfather', 'The Dark Knight',
                'Pulp Fiction', 'Forrest Gump', 'Inception', 'The Matrix',
                'Goodfellas', 'The Silence of the Lambs', 'Fight Club',
                'Star Wars: Episode IV', 'The Lord of the Rings: The Fellowship of the Ring',
                'Interstellar', 'The Lion King', 'The Avengers', 'Joker',
                'Titanic', 'Jurassic Park', 'Avatar', 'The Terminator'
            ];
            filteredMovies = [...movies];
            populateOptions(movies);
        }
    }
    
    function populateOptions(movieList) {
        selectOptions.innerHTML = '';
        
        if (movieList.length === 0) {
            noResultsElement.style.display = 'block';
            return;
        }
        
        noResultsElement.style.display = 'none';
        
        movieList.forEach(movie => {
            const option = document.createElement('div');
            option.classList.add('select-option');
            option.textContent = movie;
            option.addEventListener('click', () => {
                selectedMovie = movie;
                selectedOption.textContent = movie;
                closeDropdown();
            });
            selectOptions.appendChild(option);
        });
    }
    
    function filterMovies() {
        const searchTerm = selectSearch.value.toLowerCase();
        
        if (searchTerm === '') {
            filteredMovies = [...movies];
        } else {
            filteredMovies = movies.filter(movie => 
                movie.toLowerCase().includes(searchTerm)
            );
        }
        
        populateOptions(filteredMovies);
    }
    
    async function getRecommendations() {
        if (!selectedMovie) {
            // Visual feedback if no movie is selected
            selectTrigger.style.borderColor = 'var(--netflix-red)';
            setTimeout(() => {
                selectTrigger.style.borderColor = 'rgba(255, 255, 255, 0.16)';
            }, 1500);
            return;
        }
        
        // Show loading indicator
        loadingElement.style.display = 'flex';
        recommendationsElement.style.display = 'none';
        
        try {
            // Make API call to get recommendations
            const response = await fetch('/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ movie: selectedMovie })
            });
            
            const recommendations = await response.json();
            
            // Hide loading indicator
            loadingElement.style.display = 'none';
            
            // Display recommendations
            displayRecommendations(recommendations);
        } catch (error) {
            console.error('Error getting recommendations:', error);
            
            // For demonstration, use sample recommendations if the API fails
            setTimeout(() => {
                loadingElement.style.display = 'none';
                
                // Sample data
                const sampleRecommendations = [
                    { title: 'Inception', year: '2010', poster: '/api/placeholder/400/600' },
                    { title: 'The Social Network', year: '2010', poster: '/api/placeholder/400/600' },
                    { title: 'Parasite', year: '2019', poster: '/api/placeholder/400/600' },
                    { title: 'Whiplash', year: '2014', poster: '/api/placeholder/400/600' },
                    { title: 'La La Land', year: '2016', poster: '/api/placeholder/400/600' },
                    { title: 'Black Panther', year: '2018', poster: '/api/placeholder/400/600' }
                ];
                
                displayRecommendations(sampleRecommendations);
            }, 1500);
        }
    }
    
    function displayRecommendations(recommendations) {
        // Clear previous recommendations
        movieGridElement.innerHTML = '';
        
        // Create movie cards for each recommendation
        recommendations.forEach(movie => {
            const movieCard = document.createElement('div');
            movieCard.classList.add('movie-card');
            
            const posterContainer = document.createElement('div');
            posterContainer.classList.add('movie-poster-container');
            
            const moviePoster = document.createElement('img');
            moviePoster.classList.add('movie-poster');
            
            // Handle image loading with better error handling
            if (movie.poster && movie.poster.startsWith('http')) {
                // Set placeholder first while the actual image loads
                moviePoster.src = '/api/placeholder/1';
                
                // Handle image loading errors
                moviePoster.onerror = function() {
                    console.log('Error loading image:', movie.poster);
                    this.src = '/api/placeholder/1';
                };
                
                // Try to load the actual movie poster
                moviePoster.src = movie.poster;
            } else {
                // Use placeholder if no valid poster URL
                moviePoster.src = '/api/placeholder/1';
            }
            
            moviePoster.alt = movie.title;
            
            const playIcon = document.createElement('div');
            playIcon.classList.add('play-icon');
            
            const movieInfo = document.createElement('div');
            movieInfo.classList.add('movie-info');
            
            const movieTitle = document.createElement('div');
            movieTitle.classList.add('movie-title');
            movieTitle.textContent = movie.title;
            
            const movieYear = document.createElement('div');
            movieYear.classList.add('movie-year');
            movieYear.textContent = movie.year || '';
            
            posterContainer.appendChild(moviePoster);
            movieCard.appendChild(posterContainer);
            movieCard.appendChild(playIcon);
            
            movieInfo.appendChild(movieTitle);
            movieInfo.appendChild(movieYear);
            movieCard.appendChild(movieInfo);
            
            movieGridElement.appendChild(movieCard);
        });
        
        // Show recommendations section
        recommendationsElement.style.display = 'block';
        
        // Scroll to recommendations
        recommendationsElement.scrollIntoView({ behavior: 'smooth' });
    }
});