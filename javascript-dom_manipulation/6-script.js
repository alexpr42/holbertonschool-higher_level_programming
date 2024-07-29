// Define the URL to fetch data from
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Select the element where the character name will be displayed
const characterElement = document.querySelector('#character');

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
    // Update the text content of the characterElement with the character name
    characterElement.textContent = data.name;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There has been a problem with your fetch operation:', error);
  });
