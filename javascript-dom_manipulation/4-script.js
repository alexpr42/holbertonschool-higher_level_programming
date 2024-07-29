// Select the add_item div and the my_list ul
const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

// Add a click event listener to the add_item element
addItem.addEventListener('click', () => {
  // Create a new li element
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  // Append the new li element to the ul
  myList.appendChild(newItem);
});
