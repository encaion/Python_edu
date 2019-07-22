import urllib
url = "https://www.naver.com"
text = urllib.request.urlopen(url)
text.read(500)
