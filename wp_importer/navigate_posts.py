import requests
from bs4 import BeautifulSoup

latest_post = 'http://www.hildeberto.com/2017/02/cleaner-code-with-functional-programming.html'

class Article:
    def __init__(self, title, content, date, categories=None):
        self.title = title
        self.content = Article.clean_content(content)
        self.date = date
        self.categories = categories

    @staticmethod
    def clean_content(content):
        markdown_content = content[28:-7]
        markdown_content = markdown_content.replace("<p>", "")
        markdown_content = markdown_content.replace("</p>", "\n")
        markdown_content = markdown_content.replace("<blockquote>", "> ")
        markdown_content = markdown_content.replace("</blockquote>", "\n")
        markdown_content = markdown_content.replace("<pre>", "```\n")
        markdown_content = markdown_content.replace("</pre>", "\n```")
        return markdown_content

    def __str__(self):
        return "{} published on {}".format(self.title, self.date)


def get_html_content(current_post):
    request = requests.get(current_post)
    return BeautifulSoup(request.text, 'html.parser')

def get_previous_post(html_content):
    link_previus = html_content.find("div", attrs={"class": "nav-links"})\
                               .find("a", attrs={"rel": "prev"})
    if link_previus:
        return link_previus['href']
    else:
        return None

def build_article(html_content):
    article_html = html_content.find("article")

    title = article_html.header.h1.string
    content = str(article_html.find("div", attrs={"class": "entry-content"}))
    date = article_html.header.div.span.time["datetime"]
    categories = [category.string for category in article_html.find_all("a", attrs={"rel": "tag"})]

    article = Article(title, content, date, categories)

    return article

def get_articles(current_post, articles=None):
    print(current_post)
    if articles is None:
        articles = []

    html_content = get_html_content(current_post)

    if html_content:
        articles.append(build_article(html_content))
        link_previus = get_previous_post(html_content)
#        if link_previus:
#            return get_articles(link_previus, articles)

    return articles

articles = get_articles(latest_post)

print(articles[0])
print(articles[0].categories)
