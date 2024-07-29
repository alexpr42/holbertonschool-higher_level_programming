// Select the header and the red_header elements
const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

// Add a click event listener to the red_header element
redHeader.addEventListener('click', () => {
  // Change the text color of the header to red
  header.style.color = '#FF0000';
});
