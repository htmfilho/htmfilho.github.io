$(document).ready(function() {
  let reads = $('#reads');

  $.get("/books/feed.xml", function (data) {
    console.log(data);
  });

  reads.html("Feed from the book section");
});


{% for book in site.data.books %}
  <h3>{{ book.title }} <small>by {{ book.author }}</small></h3>
  <img align="left" border="0" style="margin-right: 10px;" width="90" src="{{ book.image }}" >
  <p>{{ book.description }}</p>
  <div class="progress">
    <div class="progress-bar" role="progressbar" style="width: {{ book.progress }}%;" aria-valuenow="{{ book.progress }}" aria-valuemin="0" aria-valuemax="100">{{ book.progress }}%</div>
  </div>
{% endfor %}
