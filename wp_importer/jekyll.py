from functools import reduce
#def save_images(images):


def save_article(article):
    url = article.url
    file_name = article.date[:10] + "-" + url[url.rfind("/") + 1:-4] + "markdown"

    with open("../_posts/{}".format(file_name), "w") as post_file:
        post_file.write("---\n")
        post_file.write("layout: post\n")
        post_file.write('title: "{}"\n'.format(article.title))
        date = article.date.replace("T", " ").replace("+", " +")[:-5] + "0200"
        post_file.write("date: {}\n".format(date))
        categories = reduce((lambda x, y: "{} {}".format(x, y)), article.categories)
        post_file.write("categories: {}\n".format(categories.lower()))
        post_file.write("---\n\n")
        post_file.write(article.content)

    #save_images(article.images)
