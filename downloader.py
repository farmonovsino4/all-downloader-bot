import requests
from environs import Env

env = Env()
env.read_env()

def tiktok_downloader(url):
    urll = "https://tiktok-download-without-watermark.p.rapidapi.com/analysis"

    querystring = {"url": url,"hd":"0"} # https://vt.tiktok.com/ZSFy5K1Gr/

    headers = {
        "X-RapidAPI-Key": env.str('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "tiktok-download-without-watermark.p.rapidapi.com"
    }

    response = requests.get(urll, headers=headers, params=querystring)

    return {'url': response.json()['data']['play'], 'title': response.json()['data']['title']}

print(tiktok_downloader("https://vt.tiktok.com/ZSFy5K1Gr/"))