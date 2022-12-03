$(document).ready(function() {
  loadReads();
  loadSports();
});

function loadReads() {
  loadRSS("reads", "https://www.hildeberto.com/books/atom.xml", "books");
}

function loadSports() {
  loadRSS("sports", "https://www.hildeberto.com/sports/atom.xml", "sports");
}

function loadRSS(contentElement, url, target) {
  let element = document.getElementById(contentElement);

  fetch(url)
    .then(response => response.text())
    .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
    .then(data => {
        const items = data.querySelectorAll("entry");
        let html = ``;
        items.forEach(el => {
          html += `
            <h3><a href="/${target}${el.querySelector("link").innerHTML}" target="_blank">${el.querySelector("title").innerHTML}</a> 
            <small>${el.querySelector("author").innerHTML}</small></h3>
            <img align="left" border="0" style="margin-right: 10px;" width="90" src="${el.querySelector("image").innerHTML}">
            <p>${el.querySelector("summary").innerHTML}</p>
          `;
        });
        element.insertAdjacentHTML("beforeend", html);
      });
}