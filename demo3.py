import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup
json_arr = []

def dump(fileName):
	with open(fileName, 'w') as f:
		json.dump(json_arr, f)

def parsePage(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text)

	for i in soup.select('div.article-brief.img-ok'):
		title = i.select('h2')[0].text
		print(title)
		tmp={}
		# dict這個型態的值是可以改變的 
		# 所以python不會自動幫你建一個新的物件而是用指標（reference）的方式連結到同一個變數
		tmp['title'] = title
		json_arr.append(tmp)

	dump('demo2.json')

parsePage('https://www.pixnet.net/')
