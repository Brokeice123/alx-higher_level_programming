$(document).ready(function () {
  // Add a click event listener to the <div> element with the ID "toggle_header"
  $('#toggle_header').click(function () {
    // Toggle the class of the <header> element between "red" and "green"
    $('header').toggleClass('red green');
  });
});
