let urls = {
  "home": "https://www.hildeberto.com/atom.xml",
  "sports": "https://www.hildeberto.com/sports/atom.xml",
  "books": "https://www.hildeberto.com/books/atom.xml"
};

$(document).ready(function() {
  loadMain(urls);
  loadReads(urls);
  loadSports(urls);
});

function loadMain(urls) {
  let allPosts = [];

  for (const [key, value] of Object.entries(urls)) {
    allPosts.concat(loadPosts(value));
  }

  console.log(allPosts.length);
}

function loadPosts(url) {
  fetch(url)
    .then(response => response.text())
    .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
    .then(data => {
        return data.querySelectorAll("entry");
      });
}

function loadReads(urls) {
  loadRSS("reads", urls["books"], "books");
}

function loadSports(urls) {
  loadRSS("sports", urls["sports"], "sports");
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