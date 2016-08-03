import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup

def savePict(url, restaurant):
    img = requests.get(url,stream=True)
    with open(restaurant+'.jpg', 'wb') as f:
        shutil.copyfileobj(img.raw, f)
savePict("https://www.facebook.com/photo.php?fbid=536034276499098&set=a.211653205603875.29917.100002775902125&type=3&theater", "test2")