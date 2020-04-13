$(document).ready(function() {
  let reads = $('#reads');

  $.get("/books/feed.xml", function (data) {
    console.log(data);
  });

  reads.html("Feed from the book section");
});
