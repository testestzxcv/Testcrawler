from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://movie.daum.net/moviedb/grade?movieId=97728&type=netizen&page=1"
print(url)
webpage = urlopen(url)
print(webpage)
source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
# print(source)
reviews = source.findAll('p',{'class': 'desc_review'})

for review in reviews:
    print(review.get_text().strip())

review_list=[]
for n in range(10):
    print(n+1)
    url='https://movie.daum.net/moviedb/grade?movieId=97728&type=netizen&page={}'.format(n+1)
    webpage = urlopen(url)
    source = BeautifulSoup(webpage,'html.parser', from_encoding='utf-8')
    reviews = source.findAll('p', {'class' : 'desc_review'})

    for review in reviews:
        review_list.append(review.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))

file = open('okja1.txt','w',encoding='utf-8')

for review in review_list:
    file.write(review+'\n')

file.close()