#!/bin/python

import requests as re
from bs4 import BeautifulSoup

webpage = re.get("https://www.shabdkosh.com/word-of-the-day/english-hindi")
soup = BeautifulSoup(webpage.content, "html5lib")

wordContainer = soup.find('p', attrs = {'class': 'pt-3'})
text = wordContainer.text.split("\xa0")

enWord = text[0]
hiWord = text[-1]

print(enWord + " | " + hiWord)