$(document).ready(function() {
  let reads = document.getElementById("reads");

  const RSS_URL = `https://www.hildeberto.com/books/atom.xml`;

  fetch(RSS_URL)
    .then(response => response.text())
    .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
    .then(data => {
        const items = data.querySelectorAll("entry");
        let html = ``;
        items.forEach(el => {
          html += `
            <h3><a href="/books${el.querySelector("link").innerHTML}" target="_blank">${el.querySelector("title").innerHTML}</a> <small>${el.querySelector("author").innerHTML}</small></h3>
            <img align="left" border="0" style="margin-right: 10px;" width="90" src="${el.querySelector("image").innerHTML}">
            <p>${el.querySelector("summary").innerHTML}</p>
          `;
        });
        reads.insertAdjacentHTML("beforeend", html);
      });
});
