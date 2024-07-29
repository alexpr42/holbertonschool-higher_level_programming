// Define the URL to fetch data from
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Select the HTML element where the translation will be displayed
const helloElement = document.querySelector('#hello');

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
    // Get the 'hello' value from the data
    const helloText = data.hello;

    // Display the 'hello' value in the HTML element
    helloElement.textContent = helloText;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There has been a problem with your fetch operation:', error);
  });
