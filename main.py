from bs4 import BeautifulSoup

import requests

URL="https://www.empireonline.com/tv/features/best-tv-shows-ever-2/"

response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")

all_shows=soup.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")

shows_titles=[show.getText() for show in all_shows]
shows=shows_titles[::-1]

with open("shows.txt",mode="w") as file:
    for show in shows:
        file.write(f"{show}\n")