import urllib.request
from functools import reduce


def get_image_filename(image_url):
    return image_url[image_url.rfind("/") + 1:]


def get_image_path(image_filename):
    return "/images/posts/{}".format(image_filename)


def save_image(image):
    image_url = image["src"]
    print("Saving {}".format(image_url))
    image_filename = get_image_filename(image_url)
    image_local_path = ".." + get_image_path(image_filename)
    urllib.request.urlretrieve(image_url, image_local_path)


def save_images(images):
    for image in images:
        save_image(image)


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

    save_images(article.images)
