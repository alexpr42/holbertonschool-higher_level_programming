// Select the header and the red_header elements
const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

// Add a click event listener to the red_header element
redHeader.addEventListener('click', () => {
  // Add the 'red' class to the header element
  header.classList.add('red');
});
