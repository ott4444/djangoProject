document.addEventListener('DOMContentLoaded', function () {
    fetchmovies();
});

function fetchmovies() {
    // TMDb API key
    const apiKey = '71c28d0bbc034d9385032100b32e03db';

    // MoviesGrid element
    const MoviesGrid = document.getElementById('MoviesGrid');

    // Display loading message
    MoviesGrid.innerHTML = '<p>Loading movies...</p>';

    const randomSearchTerms = ['action', 'comedy', 'drama', 'adventure'];
    const randomTerm = randomSearchTerms[Math.floor(Math.random() * randomSearchTerms.length)];

    // Fetch movie data from TMDb API with a default search term
    fetch(`https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${randomTerm}`)
        .then(response => response.json())
        .then(data => {
            if (data.results && data.results.length > 0) {
                moviestoshow(data.results);
            } else {
                MoviesGrid.innerHTML = '<p>No random movies found!</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching random movies:', error);
            MoviesGrid.innerHTML = '<p>Error fetching movies. Please try again later.</p>';
        });
}

function searchMovies(event) {
    event.preventDefault();  // Prevent the default form submission

    // TMDb API key
    const apiKey = '71c28d0bbc034d9385032100b32e03db';
    const searchInput = document.getElementById('searchInput').value;

    // MoviesGrid element
    const MoviesGrid = document.getElementById('MoviesGrid');

    // Search result validation
    if (searchInput.trim() !== '') {
        // Display loading message
        MoviesGrid.innerHTML = '<p>Loading movies...</p>';

        // Fetch movie data from TMDb API
        fetch(`https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${searchInput}`)
            .then(response => response.json())
            .then(data => {
                if (data.results && data.results.length > 0) {
                    moviestoshow(data.results);
                } else {
                    MoviesGrid.innerHTML = '<p>No movies found with the given name!</p>';
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                MoviesGrid.innerHTML = '<p>Error fetching movies. Please try again later.</p>';
            });
    } else {
        alert('Enter a movie title then search!');
    }
}

function moviestoshow(movies) {
    const MoviesGrid = document.getElementById('MoviesGrid');

    // Clear previous results
    MoviesGrid.innerHTML = '';

    // Display each movie in the results
    movies.forEach(movie => {
        const posterPath = movie.poster_path ? `https://image.tmdb.org/t/p/w500${movie.poster_path}` : '/static/images/placeholder.png';
        const releaseYear = movie.release_date ? movie.release_date.slice(0, 4) : 'N/A';

        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');

        // Link each movie to its detail page using Django's URL reversing
        movieCard.innerHTML = `
             <a href="/moviesearch/movie/${movie.tmdb_id}/">
                <img src="${posterPath}" alt="${movie.title}">
                <h2>${movie.title}</h2>
                <p>${releaseYear}</p>
            </a>
        `;

        MoviesGrid.appendChild(movieCard);
    });
}

