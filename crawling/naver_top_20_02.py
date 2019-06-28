import requests
from bs4 import BeautifulSoup

keywords = BeautifulSoup(requests.get("https://www.naver.com").text, "html.parser").select('[class=ah_k]') 
[word.text for word in keywords]
