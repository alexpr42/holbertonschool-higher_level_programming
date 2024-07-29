// Select the update_header div and the header element
const updateHeader = document.querySelector('#update_header');
const header = document.querySelector('header');

// Add a click event listener to the update_header element
updateHeader.addEventListener('click', () => {
  // Update the text content of the header element
  header.textContent = 'New Header!!!';
});
