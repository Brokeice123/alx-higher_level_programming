$(document).ready(function () {
  // Add item
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });

  // Remove item
  $('#remove_item').click(function () {
    // Remove the last <li> element from the <ul> with class "my_list"
    $('ul.my_list li:last-child').remove();
  });

  // Clear list
  $('#clear_list').click(function () {
    // Remove all <li> elements from the <ul> with class "my_list"
    $('ul.my_list').empty();
  });
});
