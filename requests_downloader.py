import requests


# svg+xml
def get_right_extension(content_type):
    return content_type.split("/")[1].split("+")[0]


def save_into_file(response):
    extension = get_right_extension(response.headers["Content-Type"])
    with open(f"image.{extension}", "wb") as f:
        f.write(response.content)


URL = "https://life-trip.ru/wp-content/uploads/2018/06/lanta-klong-nin.jpg"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
# stream=True - для видео, но это может быть в другой конструкции в requests
r = requests.get(URL, headers=headers)

save_into_file(r)


print()
