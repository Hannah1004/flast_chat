import requests
import random
from bs4 import BeautifulSoup

#url = "https://api.thecatapi.com/v1/images/search?mime_type=jpg"
#url = "https://api.thedogapi.com/v1/images/search?mime_types=jpg"

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('dt.tit > a')
star_tag = doc.select('div.star_t1 > a > span.num')
reserve_tag = doc.select('div.star_t1.b_star > span.num')
image_tag = doc.select('div.thumb > a > img')

movie_dic = {}
for i in range(0,10):
    movie_dic[i] = {
        "title" : title_tag[i].text,
        "star" : star_tag[i].text,
        "reserve" : reserve_tag[i].text,
        "image" : image_tag[i].get('src')
    }
    
pick_movie = movie_dic[random.randrange(0,10)]
print(pick_movie)
