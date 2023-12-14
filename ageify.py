# ageify API
import urllib.request
import json

def ageify(name: str, value: str):
    url = f"https://api.agify.io?name={name}"

    with urllib.request.urlopen(url) as response:
        body_json = response.read()

    body_dict = json.loads(body_json)
    if body_dict["count"] == 0:
        return "There's no one with that name yet!"

    if value == "age":
        return f"People with the name {name.capitalize()} are an average of {body_dict[value]} years old." 
    else:
        return f"There are approximately {body_dict[value]} people called {name.capitalize()}." 
    




