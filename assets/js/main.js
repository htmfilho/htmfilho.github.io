$(document).ready(function() {
  let reads = $('#reads');

  const RSS_URL = `https://www.hildeberto.com/books/feed.xml`;

  fetch(RSS_URL)
    .then(response => response.text())
    .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
    .then(data => console.log(data));

  reads.html("Feed from the book section");
});
