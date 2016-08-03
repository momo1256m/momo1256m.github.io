import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup
json_arr = []

def savePict(url, restaurant):
    img = requests.get(url,stream=True)
    with open(restaurant+'.jpg', 'wb') as f:
        shutil.copyfileobj(img.raw, f)

def dump(fileName):
	with open(fileName, 'w', encoding='UTF-8') as f:
		json.dump(json_arr, f)

def parsePage(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text)

	aLen = len(soup.select("ul.deal16 li.box-shadow2px")) 
	# ul.deal16 li.box-shadow2px是餐廳的tag
        # 建立進度條物件
	ProgreBar = pyprind.ProgBar(aLen, title = "台中 共 {} 個餐廳類別要處理".format(aLen)) 

	for i, ProgIndex in zip( soup.select('ul.deal16 li.box-shadow2px'), range(1,aLen+1)):
		product = i.select('h3.proname_3')[0].text
		restaurant = i.select('h2.ref_name_2')[0].text	
		imghref = i.select('img')[0]['src']

		tmp={}
		# dict這個型態的值是可以改變的 
		# 所以python不會自動幫你建一個新的物件而是用指標（reference）的方式連結到同一個變數
		tmp['product'] = product
		tmp['restaurant'] = restaurant
		json_arr.append(tmp)

		savePict(imghref, restaurant)
	
		ProgreBar.update(5,item_id = ProgIndex, force_flush=False)
		#item_id可以讓使用者追蹤到底執行到第幾個ID

	dump('demo.json')

parsePage('http://www.gomaji.com/index.php?city=Taichung&tag_id=28')