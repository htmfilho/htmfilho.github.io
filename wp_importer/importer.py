from wordpress import get_articles
from jekyll import save_article

latest_post_url = 'http://www.hildeberto.com/2017/02/cleaner-code-with-functional-programming.html'

articles = get_articles(latest_post_url)

for article in articles:
    save_article(article)
