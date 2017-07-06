import requests
from bs4 import BeautifulSoup

latest_post_url = 'http://www.hildeberto.com/2017/02/cleaner-code-with-functional-programming.html'

class Article:
    def __init__(self, title, content, date, categories=None, images=None):
        self.title = title
        self.content = Article.clean_content(content, images)
        self.date = date
        self.categories = categories
        self.images = images

    @staticmethod
    def clean_content(content, images):
        content_html = str(content)
        markdown_content = content_html[28:-7]
        markdown_content = markdown_content.replace("<p>", "")
        markdown_content = markdown_content.replace("</p>", "\n")
        markdown_content = markdown_content.replace("<blockquote>", "> ")
        markdown_content = markdown_content.replace("</blockquote>", "\n")
        markdown_content = markdown_content.replace("<pre>", "```\n")
        markdown_content = markdown_content.replace("</pre>", "\n```")
        markdown_content = markdown_content.replace("<code>", "`")
        markdown_content = markdown_content.replace("</code>", "`")

        for image in images:
            markdown_content = markdown_content.replace(str(image), "![Alt text]({})".format(image["src"]))

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


def find_image_tags(content):
    image_tags = content.find_all("img")
    return [img for img in image_tags]


def build_article(html_content):
    article_html = html_content.find("article")

    title = article_html.header.h1.string
    content = article_html.find("div", attrs={"class": "entry-content"})
    date = article_html.header.div.span.time["datetime"]
    categories = [category.string for category in article_html.find_all("a", attrs={"rel": "tag"})]
    images = find_image_tags(content)

    return Article(title, content, date, categories, images)


def get_articles(current_post_url, articles=None):
    print(current_post_url)
    if articles is None:
        articles = []

    html_content = get_html_content(current_post_url)

    if html_content:
        articles.append(build_article(html_content))
        previus_post_url = get_previous_post(html_content)
#        if previus_post_url:
#            return get_articles(previus_post_url, articles)

    return articles

articles = get_articles(latest_post_url)

print(articles[0])
print(articles[0].content)
