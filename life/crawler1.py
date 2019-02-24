from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://direct.samsunglife.com/customerCenter/faq/list.eds#list?searchNode=NODE0000000109&searchText=&page=1'
webpage=urlopen(url)

source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')

reviews = source.select('a')

print(reviews)