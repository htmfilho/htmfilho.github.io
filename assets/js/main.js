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
            <h3><a href="/books${el.querySelector("link").innerHTML}" target="_blank">${el.querySelector("title").innerHTML}</a> <small>${el.querySelector("author").innerHTML}</small></h3>
            <img align="left" border="0" style="margin-right: 10px;" width="90" src="${el.querySelector("image").innerHTML}">
            <p>${el.querySelector("summary").innerHTML}</p>
            <div class="progress">
              <div class="progress-bar" role="progressbar" style="width: ${el.querySelector("progress").innerHTML}%;" aria-valuenow="${el.querySelector("progress").innerHTML}" aria-valuemin="0" aria-valuemax="100">${el.querySelector("progress").innerHTML}%</div>
            </div>
          `;
        });
        reads.insertAdjacentHTML("beforeend", html);
      });
});
