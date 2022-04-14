import json
import os

import requests
from dotenv import load_dotenv

# from pprint import pprint


# относительный путь для примера, лучше использовать глобальный!
load_dotenv("./.env")


SAVE_ARTISTS_PATH = "artists.json"
RETRIEVING_ARTISTS_URL = "https://api.artsy.net/api/artists"
TOKEN_EXTRACTION_URL = "https://api.artsy.net/api/tokens/xapp_token"
client_id = os.getenv("CLIENT_ID", None)
client_secret = os.getenv("CLIENT_SECRET", None)

# f"https://{client_id}"
# curl -v -X POST "https://api.artsy.net/api/tokens/xapp_token
# ?client_id=*********&client_secret=***************************"
TOKEN_EXTRACTION_PARAMS = {
    "client_id": client_id,
    "client_secret": client_secret,
}


def get_token_info(params):
    """The function returns token and expires_at"""
    try:
        r = requests.post(TOKEN_EXTRACTION_URL, params=params)
        r.raise_for_status()
    except Exception as e:
        print(e)
        return None, None
    # print()
    # json_data = json.loads(r.text)
    # Exceptions?
    json_data = r.json()
    return json_data["token"], json_data["expires_at"]


# 'X-Xapp-Token:...some_token
def make_headers_for_api(token):
    return {"X-Xapp-Token": token}


def make_example_request(url, headers):
    try:
        r = requests.get(url, headers=headers)
        # if r.status_code == 200
        r.raise_for_status()
        json_data = r.json()
        return json_data
    except Exception as e:
        print(e)
    return None


def extract_artists_info(data):
    return data.get("_embedded", {}).get("artists", [])


def extract_next_url(data):
    return data.get("_links", {}).get("next", None)


def save_artist_info(artists_info, path):
    with open(path, "w") as f:
        json.dump(artists_info, f, indent=2)


def pipeline(path):
    # input желательно делать здесь
    artists_data = []
    # можно поработать с библиотекой datetime,
    # чтобы обработать время истечения токена
    token, expires_at = get_token_info(TOKEN_EXTRACTION_PARAMS)
    # maybe there should be logic for expires_at!
    headers = make_headers_for_api(token)
    data = make_example_request(RETRIEVING_ARTISTS_URL, headers)

    # artists_bunch = extract_artists_info(data)
    # artists_data.extend(artists_bunch)
    artists_data.extend(extract_artists_info(data))

    next_url = extract_next_url(data)
    # while next_url is not None:
    counter = 1
    while next_url:
        try:
            print(counter)
            data = make_example_request(RETRIEVING_ARTISTS_URL, headers)
            artists_data.extend(extract_artists_info(data))
            next_url = extract_next_url(data)
            counter += 1
            if counter > 2:
                break
        except Exception as e:
            print(e)
            # place to create logic about "expires_at"
            break
    save_artist_info(artists_data, path)


if __name__ == "__main__":
    # input желательно делать здесь
    pipeline(SAVE_ARTISTS_PATH)


# def make_headers(token):
#     return {"X-Xapp-Token": token}
#
#
# def get_token(client_id, client_secret):
#     # url = f"https://api.artsy.net/api/tokens/xapp_token
#     # ?client_id={client_id}&client_secret={client_secret}"
#     url = "https://api.artsy.net/api/tokens/xapp_token"
#     params = {
#         "client_id": client_id,
#         "client_secret": client_secret,
#     }
#     response = requests.post(url, params=params)
#     token_data = response.json()
#     # expires??
#     # token_data = json.loads(response.text)
#     try:
#         token = token_data["token"]
#     except Exception as e:
#         print(e)
#         return None
#     return token
#
#
# def get_artist(headers, artist="andy-warhol"):
#     url = "https://api.artsy.net/api/artists"
#     if not (artist is None or artist == ""):
#         url = f"{url}/{artist}"
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return None
#
#
# def save_artist_info(artist_info, path):
#     with open(path, "w") as f:
#         json.dump(artist_info, f)
#
#
# def pipeline(client_id, client_secret, artist, path="artist.json"):
#     token = get_token(client_id, client_secret)
#     if token is None:
#         print("Token is None!")
#         return None
#
#     headers = make_headers(token)
#     artist_info = get_artist(headers, artist)
#     if artist_info is None:
#         print("artist_info is None")
#         return None
#
#     save_artist_info(artist_info, path)
#     return artist_info
#
#
# if __name__ == "__main__":
#     # artist = "andy-warhol"
#     artist_info = pipeline(client_id, client_secret, "")
#     pprint(artist_info)
#     print()
