$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Displaying the value of hello from that fetch in the HTML tag DIV#hello
    $('DIV#hello').text(data.hello);
  });
});
