// Select the header and toggle_header elements
const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

// Add a click event listener to the toggle_header element
toggleHeader.addEventListener('click', () => {
  // Toggle the header's class between 'red' and 'green'
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
