import requests


links = ["https://ru.wikipedia.org/robots.txt", 
    "https://twitter.com/robots.txt", 
    "https://github.com/robots.txt"]

for link in links:
    robots_txt = requests.get(link)
    with open("robots_file", "a+", encoding="utf-8") as file:
        file.write(robots_txt.text)