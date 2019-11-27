import requests
import csv

item = input("Enter a Item :\t")

URL = "https://www.flipkart.com/search?q="+item
r = requests.get(URL) 
print(r.content) 
name=[]
price=[]
specs=[]
rating=[]

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify())

items = soup.findAll('div',attrs ={'class':'bhgxx2 col-12-12'})
items[0]

for item in items:
    name.append(str(item.find('div',attrs={'class':'_3wU53n'}))[21:-6])
    print(str(item.find('div',attrs={'class':'_3wU53n'}))[21:-6])

for item in items:
    spec=""
    for it in item.findAll('li',attrs={'class':'tVe95H'}):
        spec += ", "+str(it)[19:-5]
        print(str(it)[19:-5])
    specs.append(spec)


for item in items:
    price.append(str(item.findAll('div',attrs={'class':'_1vC4OE _2rQ-NK'}))[30:-7])
    print(str(item.findAll('div',attrs={'class':'_1vC4OE _2rQ-NK'}))[30:-7])

for item in items:
    rating.append(str(item.findAll('div',attrs={'class':'hGSR34'}))[21:24])
    print(str(item.findAll('div',attrs={'class':'hGSR34'}))[21:24])

with open("flip.csv", 'w') as csvfile:
    fields = ['S. no.', 'Name', 'price', 'specs', 'rating']
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    count = 1
    datas=[]
    for i in range(len(price)):
        if name[i]:
            data = {}
            data['S. no.'] = count
            data['Name'] = name[i]
            data['price'] = price[i]
            data['specs'] = specs[i][2:]
            data['rating'] = rating[i]
            count+=1
            datas.append(data)
    writer.writerows(datas)