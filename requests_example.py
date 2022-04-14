from pprint import pprint

import requests


print("EXPERIMENT 1")
print("-" * 15)
url_1 = "http://www.google.com/"
response_1 = requests.get(url_1)
pprint(dict(response_1.headers))
print("-" * 15)
print("EXPERIMENT 2")
print("-" * 15)

url_2 = "https://www.google.com/"
response_2 = requests.get(url_2)
pprint(dict(response_2.headers))
print("-" * 15)
print("EXPERIMENT 3")
print("-" * 15)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}
url_3 = "https://www.google.com/"
response_3 = requests.get(url_3, headers=headers)
pprint(dict(response_3.headers))
print(f"Status code = {response_3.status_code}")
print()
