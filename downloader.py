import requests


def instagram_downloader(url):
    urll = "https://instagram-post-and-reels-downloader.p.rapidapi.com/"

    querystring = {"url":url}

    headers = {
        "X-RapidAPI-Key": "3ced9d8030msh7126f2d249ae58ep13c95ajsn5107fb57f8a5",
        "X-RapidAPI-Host": "instagram-post-and-reels-downloader.p.rapidapi.com"
    }

    response = requests.get(urll, headers=headers, params=querystring)
    return response.json()[0]