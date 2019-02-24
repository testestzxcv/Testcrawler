from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://movie.naver.com/movie/bi/mi/review.nhn?code=143435&page=1'
webpage = urlopen(url)

source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')

# reviews = source.findAll('strong' )
reviews = source.select("#reviewTab > div > div > ul > li > a > strong")

# for review in reviews:
#     print(review.get_text().strip())

review_list=[]
for n in range(10):
    url = 'https://movie.naver.com/movie/bi/mi/review.nhn?code=143435&page={}'.format(n+1)
    webpage = urlopen(url)
    source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
    reviews = source.select("#reviewTab > div > div > ul > li > a > strong")

    for review in reviews:
        review_list.append(review.get_text().strip())

print(review_list)

file = open('okja_naver.txt','w',encoding='utf-8')

for review in review_list:
    file.write(review+'\n')

file.close()