$(document).ready(function () {
  // Fetching data from the API
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Displaying the movie titles in the HTML <ul> element with id "list_movies"
    data.results.forEach(function (film) {
      $('<li>').text(film.title).appendTo('ul#list_movies');
    });
  });
});
