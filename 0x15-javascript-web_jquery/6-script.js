$(document).ready(function () {
  // Add a click event listener to the <div> element with the ID "update_header"
  $('DIV#update_header').click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('<New Header!!!');
  });
});
