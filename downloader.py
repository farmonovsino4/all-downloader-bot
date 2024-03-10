import requests
from environs import Env


env = Env()
env.read_env()

def TikTokdDownloader(url):
    urll = "https://tiktok-download-without-watermark.p.rapidapi.com/analysis"

    querystring = {"url": url,"hd":"0"} # https://vt.tiktok.com/ZSFy5K1Gr/

    headers = {
        "X-RapidAPI-Key": env.str('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "tiktok-download-without-watermark.p.rapidapi.com"
    }

    response = requests.get(urll, headers=headers, params=querystring)

    return {'url': response.json()['data']['play'], 'title': response.json()['data']['title']}

def FacebookDownloader(url):
    urll = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"
    # hard limit 500 request per month
    querystring = {"url":url} # https://fb.watch/qGHemBLpH8/

    headers = {
    	"X-RapidAPI-Key": env.str('RAPIDAPI_KEY'),
    	"X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
    }

    response = requests.get(urll, headers=headers, params=querystring)
    try:
        return {'url': response.json()['links']['Download High Quality'], 'title': response.json()['title']}
    except KeyError:
        return {'url': response.json()['links']['Download Low Quality'], 'title': response.json()['title']}
    
def PinterestDownloader(url):
    urll = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"

    querystring = {"url": url}

    headers = {
        "X-RapidAPI-Key": env.str('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "pinterest-video-and-image-downloader.p.rapidapi.com"
    }

    response = requests.get(urll, headers=headers, params=querystring)
    return {'url': response.json()['data']['url'], 'title': response.json()['data']['title']}

print(PinterestDownloader("https://www.pinterest.com/pin/1140536674373849330/"))

#'https://youtu.be/nT1dt6j4R8g?si=z7zDZ5PiiGQ406b0'