import requests
import json
import threading


url_1 = "https://api.pushshift.io/reddit/search/comment/?subreddit=bitcoin&after=24h"
url_2 = "https://api.pushshift.io/reddit/search/comment/?subreddit=bitcoin&before=24h"


def download(url):
    r = requests.get(url)
    data = r.json()
    json_object = json.dumps(data, indent=4)
    print(json_object)
    with open("comments_threading.json", "a") as file:
        file.write(json_object)

thread_1 = threading.Thread(target=download, args=(url_1,))
thread_2 = threading.Thread(target=download, args=(url_2,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()