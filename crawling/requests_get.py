import requests 
URL = 'https://www.naver.com' 
response = requests.get(URL)
response.status_code
response.text[:500]
