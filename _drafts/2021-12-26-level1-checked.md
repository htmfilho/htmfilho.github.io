---
layout: post
title: "Reaching RMM Level 1 in My Repositories"
date: 2021-12-26 12:00:00 +0200
image: /images/posts/gopher-writing.png
categories: repository programming documentation portfolio
---

![Gopher Writing](/images/posts/gopher-writing.png)

After proposing the [Repository Maturity Model (RMM)](/2021/12/repositories-portfolio.html#repository-maturity-model-rmm), I wanted to put it in practice in my [portfolio](/2021/12/knowledge-portfolio.html). The first step is to implement Level 1, which consists on writing the content to inform visitors about the repository and guide contributors through the process of fixing bugs and enhancing features. It doesn't necessarily need to have working code, but anyone should be able to understand what the repository is about and how to contribute to it. I'm reporting here what we have done to accomplish that in all repositories.

<!-- more -->

Documentation is often neglected at the initial stages of a project. It might be due to the fact that ["documenting" is less fun than "coding"](https://stackoverflow.blog/2020/07/13/tales-from-documentation-write-for-your-dumbest-user/). I agree with that, but in my experience, leaving the whole documentation to be written at the end is more painful than gradually writing it as the project evolves. Writing also leads to thinking and thinking is what we need to create great products. Amazon, Google, Twitter, Spotify and others have [built a culture of documentation](https://dev.to/doctave/how-google-twitter-and-spotify-built-a-culture-of-documentation-3e0m), and those who follow _lean_ practices like to test ideas before implementing them.

Documenting since the beginning makes the content lighter, cleaner, better. It passes through several revisions each time someone contributes with more content. So a repository reaches Level 1 when it contains enough content not only for users and contributors, but also to give them a chance to document as they use and build the product. After getting some inspiration from [opensource.guide](https://opensource.guide), we came up with the following artifacts for Level 1:

- _short description_
- _user guide website_
- _readme file_
- _code of conduct_
- _contribution guidelines_
- _license_
- _tags_
- _issue templates_
- _pull request template_

[Github](https://www.github.com) somehow helps us to implement Level 1. When creating a repository, it suggests creating a _readme_ file. It is then generated in the root of the repository. Github also has a checklist to make the repository welcoming to contributors, as we can see in the figure below.

![The community profile in the insights of a repository](/images/posts/github-insights-community.png)

You can find this checklist at "Insights > Community". It automatically checks for the presence of files in predefined locations, completing the checklist as the following files are created:

 - `.github/ISSUE_TEMPLATE/bug_report.md` (issue templates)
 - `.gitbub/ISSUE_TEMPLATE/feature_request.md` (issue templates)
 - `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` (pull request template)
 - `CODE_OF_CONDUCT.md` (code of conduct)
 - `CONTRIBUTING.md` (contribution guidelines)
 - `LICENSE` (license)
 - `README.md` (readme file)

We are left with _short description_, _user guide website_, and _tags_. The short description is the product summarized in a sentence, in the _About_ section of the repository. It also includes a paragraph at the beginning of the README file, as highlighted in read in the figure below.

![Github short description and tags](/images/posts/github-short-description.png)

The figure also highlights the tags, which are commonly used keywords across Github. They help to make the project discoverable by Github's search engine. We can also see the link to the user guide website above the tags. For the website, Github helps with [Github Pages](https://pages.github.com), whose configuration you can find at "Settings > Pages". Any HTML content in the folder `/docs` is served as a static website. All we have to do is to generate that HTML content and publish there. We're using [Asciidoctor](https://asciidoctor.org) for that, which processes the Asciidoc format and generates a good looking HTML page, like the one below.

![Asciidoctor User Guide](/images/posts/asciidoctor-user-guide.png)

In the last 5 days, we went through all repositories, produced all the documentation required by RMM Level 1 and now we have all of them ready to receive code. The following table compiles everything that was produced.

<table class="table table-striped">
  <thead>
    <tr>
      <th>Artifacts</th>
      <th>digger</th>
      <th>minimily</th>
      <th>controlato</th>
      <th>CSVSource</th>
      <th>pycific</th>
      <th>spitfhir</th>
      <th>liftbox</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Short description</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>Documentation website</i></td>
      <td align="center"><a href="https://www.hildeberto.com/digger/" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://www.hildeberto.com/minimily/" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://www.hildeberto.com/controlato/" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://www.hildeberto.com/csvsource/" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://www.hildeberto.com/spitfhir/" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>README file</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger/blob/main/README.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily/blob/main/README.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato/blob/main/README.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource/blob/main/README.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir/blob/main/README.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>License</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger/blob/main/LICENSE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily/blob/main/LICENSE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato/blob/main/LICENSE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource/blob/main/LICENSE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir/blob/main/LICENSE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>Code of conduct</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger/blob/main/CODE_OF_CONDUCT.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily/blob/main/CODE_OF_CONDUCT.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato/blob/main/CODE_OF_CONDUCT.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource/blob/main/CODE_OF_CONDUCT.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir/blob/main/CODE_OF_CONDUCT.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>Contribution guidelines</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger/blob/main/CONTRIBUTING.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily/blob/main/CONTRIBUTING.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato/blob/main/CONTRIBUTING.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource/blob/main/CONTRIBUTING.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir/blob/main/CONTRIBUTING.md" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>Issues templates</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger/tree/main/.github/ISSUE_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily/tree/main/.github/ISSUE_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato/tree/main/.github/ISSUE_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource/tree/main/.github/ISSUE_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir/tree/main/.github/ISSUE_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>Pull request template</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger/tree/main/.github/PULL_REQUEST_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily/tree/main/.github/PULL_REQUEST_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato/tree/main/.github/PULL_REQUEST_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource/tree/main/.github/PULL_REQUEST_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir/tree/main/.github/PULL_REQUEST_TEMPLATE" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
    <tr>
      <td><i>Tags</i></td>
      <td align="center"><a href="https://github.com/htmfilho/digger" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/minimily" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/controlato" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/csvsource" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="https://github.com/htmfilho/spitfhir" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
      <td align="center"><a href="/2022/01/never-soon-change.html" target="_blank"><img src="/assets/img/file-earmark-text.svg"></a></td>
    </tr>
  </tbody>
</table>

There is a reasoning behind the open source licensing of these repositories. I'm using [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) when the product targets end-users. We hope people concentrate their efforts around these GPL repositories, but if they decide to go in another direction, at least they have to keep the source open elsewhere. I'm using [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) for libraries, giving the necessary freedom developers need to fulfill the requirements of their solutions. I'm using [MIT](https://opensource.org/licenses/MIT) for tools that target developers and non-technical people. Here is the distribution:

- **GPL-3.0 License**
  - Digger
  - Minimily
  - Controlato
  - Pycific
- **Apache 2.0 License** 
  - CSVSource
  - SpitFHIR
- **MIT License**
  - Liftbox

We reached a point where all the repositories are minimally organized to welcome contributions. This is the result of implementing the RMM Level 1. At this point, we're ready to pursuit Level 2, which is delivering a minimal viable product. It means a lot of code, in different languages, solving different problems. You're welcome to participate by writing code, documentation, tests, etc.

**NOTE: I recently changed the repositories to refine my portfolio and [documented the changes in another blog post](/2022/01/never-soon-change.html)**.
