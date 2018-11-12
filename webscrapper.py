from bs4 import BeautifulSoup
import re 
import requests
import pandas as pd
i=1
# df=pd.DataFrame( columns=['name', 'normalPrice', 'NewPrice'])
titleCol=[]

while True:
    url = 'http://store.steampowered.com/search/?sort_by=Released_DESC&page='+str(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,features="html.parser")
    rows = soup.find_all( class_="search_result_row")
    for row in rows:
        m=re.findall(r"(\$\w+\.\w+)",row.find(class_="search_price").text) #filtramos los datos para extraer los precios mediante una expresion regular
        priceNew=""
        price =""
        if  m:
            price=m[0]
            if len(m)>1:
                priceNew = m[1] #row.find(class_="search_price").text
        info = {
                    "title": row.find(class_="title").text,
                    "price": price,
                    "priceNew":priceNew,
                    "releaseDate":row.find(class_="search_released").text,
                    "profileLink":row['href']

                    }
                    
        titleCol.append(info)
    i = i+1
    print ("analizando pagina: ",i)
    if ((not row) or i>1950):
        break
df=pd.DataFrame(titleCol)
print df
df.to_csv("out.csv",sep=';',  encoding='utf-8')