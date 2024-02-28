$(document).ready(function () {
  // Fetch character data from the URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the fetched data
    const characterName = data.name;

    // Display the character name in the <div> element with the ID "character"
    $('#character').text(characterName);
  });
});
