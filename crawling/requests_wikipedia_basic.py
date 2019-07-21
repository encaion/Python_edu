import requests
from bs4 import BeautifulSoup as bs

lists = ["피카츄", "파이리", "꼬부기", "오쪼라고"]
for list in lists:    
    result = requests.get("https://ko.wikipedia.org/wiki/" + list)
    soup = bs(result.text, 'html.parser')
    ps = soup.select(".mw-parser-output p")
    print(list)
    
    try:
        print(ps[0].text)
    except:
        print("정보없음")
    
    print("\n\n")
