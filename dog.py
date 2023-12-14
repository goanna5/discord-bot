# dog API
import urllib.request
import json

def getDog():
    url = "https://dog.ceo/api/breeds/image/random"

    with urllib.request.urlopen(url) as response:
        body_json = response.read()

    body_dict = json.loads(body_json)
    return body_dict['message'] 