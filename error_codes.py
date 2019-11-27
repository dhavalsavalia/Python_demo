#!/usr/bin/env python
# coding: utf-8

# ## 1. web scraping 1

# In[ ]:


import requests
import time
from selenium import webdriver
from PIL import Image
from io import BytesIO

url = "https://unsplash.com"

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get(url)

driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)
image_elements = driver.find_elements_by_css_selector("#gridMulti img")
i = 0

for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    # Send an HTTP GET request, get and save the image from the response
    image_object = requests.get(image_url)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1


# ## 2. GUI 1

# In[ ]:


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()


# ##  web scraping 2 flipkart 

# In[ ]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


# ## spell check code

# In[ ]:


import newspaper
from nltk import word_tokenize
import enchant
import re
url = 'https://hackernoon.com/dilemmas-of-a-digital-lifestyle-27c044940157' #input URL
my_article = newspaper.Article(url,language='en') # ### Extracting the Article Content
my_article.download()
my_article.parse()  
d = enchant.Dict("en_US") # ### Spell-Checking the tokenized words 
print(list(set([word.encode('ascii', 'ignore') for word in word_tokenize(my_article.text) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] )))


# In[ ]:




