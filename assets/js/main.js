$(document).ready(function() {
  let reads = document.getElementById("reads");

  const RSS_URL = `https://www.hildeberto.com/books/atom.xml`;

  fetch(RSS_URL)
    .then(response => response.text())
    .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
    .then(data => {
        console.log(data);
        const items = data.querySelectorAll("entry");
        let html = ``;
        items.forEach(el => {
          html += `
            <article>
              <img src="${el.querySelector("image").innerHTML}" alt="">
              <h2>
                <a href="${el.querySelector("link").innerHTML}" target="_blank" rel="noopener">
                  ${el.querySelector("title").innerHTML}
                </a>
              </h2>
            </article>
          `;
        });
        reads.insertAdjacentHTML("beforeend", html);
      });
});
