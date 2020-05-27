# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:17:25 2020

@author: scaryalberto

description: xml con python
"""









url="https://www.michiganradio.org/post/heres-what-you-need-know-about-michigans-stay-home-order"


'''
#salviamo una imagine localmente
import requests
with open('FB_IMG_1490534565948.jpg', 'wb') as f:
    f.write(requests.get('https://www.michiganradio.org/sites/michigan/files/styles/x_large/public/202003/hanson-lu-sq5P00L7lXc-unsplash.jpg').content)
'''    
    

#e se le vogliamo tutte????

import re
import requests
from bs4 import BeautifulSoup

#site = 'http://pixabay.com'
site="https://www.michiganradio.org/post/heres-what-you-need-know-about-michigans-stay-home-order"
response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)