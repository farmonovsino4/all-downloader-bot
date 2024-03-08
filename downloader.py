import requests
from environs import Env

env = Env()
env.read_env()

def instagram_downloader(url):
    urll = "https://instagram-post-and-reels-downloader.p.rapidapi.com/"

    querystring = {"url": url}

    headers = {
        "X-RapidAPI-Key": env.str('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "instagram-post-and-reels-downloader.p.rapidapi.com"
    }

    response = requests.get(urll, headers=headers, params=querystring)
    return response.json()[0]