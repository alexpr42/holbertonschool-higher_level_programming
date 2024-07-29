// Define the URL to fetch data from
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Select the <ul> element where movie titles will be displayed
const listMoviesElement = document.querySelector('#list_movies');

// Fetch data from the URL
fetch(url)
  .then(response => {
    // Check if the response is ok
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the JSON from the response
  })
  .then(data => {
    // Get the list of movies from the response data
    const movies = data.results;

    // Iterate through each movie and create a list item for it
    movies.forEach(movie => {
      const li = document.createElement('li'); // Create a new <li> element
      li.textContent = movie.title; // Set the text content to the movie title
      listMoviesElement.appendChild(li); // Append the <li> to the <ul>
    });
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There has been a problem with your fetch operation:', error);
  });
