import requests
import json


r = requests.get("https://api.pushshift.io/reddit/search/comment/?q=bitcoin&subreddit=bitcoin")
data = r.json()
json_object = json.dumps(data, indent=4)

with open("comments.json", "w") as file:
    file.write(json_object)