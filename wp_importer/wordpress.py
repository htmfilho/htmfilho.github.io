import requests
from bs4 import BeautifulSoup
from jekyll import save_article, get_image_filename, get_image_path

class Article:
    def __init__(self, url, title, content, date, categories=None, images=None):
        self.url = url
        self.title = title
        self.content = Article.__clean_content(content, images)
        self.date = date
        self.categories = categories
        self.images = images

    @staticmethod
    def __clean_content(content, images):
        content_html = str(content)
        markdown_content = content_html[28:-7]
        markdown_content = markdown_content.replace("<p>", "")
        markdown_content = markdown_content.replace("</p>", "\n")
        markdown_content = markdown_content.replace("<blockquote>", "> ")
        markdown_content = markdown_content.replace("</blockquote>", "\n")
        markdown_content = markdown_content.replace("<pre>", "```\n")
        markdown_content = markdown_content.replace("</pre>", "\n```\n")
        markdown_content = markdown_content.replace("<code>", "`")
        markdown_content = markdown_content.replace("</code>", "`")
        markdown_content = markdown_content.replace("&lt;", "<")
        markdown_content = markdown_content.replace("&gt;", ">")

        for image in images:
            image_filename = get_image_filename(image["src"])
            image_path = get_image_path(image_filename)
            markdown_content = markdown_content.replace(str(image), "![{}]({})".format(image_filename, image_path))

        return markdown_content

    def __str__(self):
        return "{} published on {}".format(self.title, self.date)


def get_previous_post_url(content_html):
    previous_url = content_html.find("div", attrs={"class": "nav-links"})\
                               .find("a", attrs={"rel": "prev"})
    if previous_url:
        return previous_url['href']
    else:
        return None


def build_article(post_url, content_html):
    print("Building {}".format(post_url))
    article_html = content_html.find("article")

    url = post_url
    title = article_html.header.h1.string
    content = article_html.find("div", attrs={"class": "entry-content"})
    date = article_html.find("time", attrs={"class": "entry-date"})["datetime"]
    categories = [category.string for category in article_html.find_all("a", attrs={"rel": "tag"})]
    images = [img for img in content.find_all("img")]

    return Article(url, title, content, date, categories, images)


def get_content_html(post_url):
    request = requests.get(post_url)
    return BeautifulSoup(request.text, 'html.parser')


def import_articles(current_post_url):
    content_html = get_content_html(current_post_url)

    if content_html:
        save_article(build_article(current_post_url, content_html))
        previous_post_url = get_previous_post_url(content_html)
        if previous_post_url:
            import_articles(previous_post_url)

def import_article(post_url):
    content_html = get_content_html(post_url)

    if content_html:
        save_article(build_article(post_url, content_html))
