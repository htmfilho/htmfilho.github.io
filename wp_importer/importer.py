from wordpress import get_articles

latest_post_url = 'http://www.hildeberto.com/2017/02/cleaner-code-with-functional-programming.html'

articles = get_articles(latest_post_url)

print(articles[0].url)
print(articles[0])
print(articles[0].content)
