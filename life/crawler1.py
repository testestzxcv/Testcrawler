from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.mnet.com/chart/TOP100/'
webpage=urlopen(url)
print(webpage)

source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
print(source)
reviews = source.select('dd')

print(reviews)