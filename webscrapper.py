from bs4 import BeautifulSoup
import requests
url = 'http://store.steampowered.com/search/?sort_by=Released_DESC'
page = requests.get(url)
soup = BeautifulSoup(page.content,features="html.parser")
rows = soup.find_all( class_="search_result_row")
for row in rows:
    print(row.find(class_="title").text,row.find(class_="search_price"))
