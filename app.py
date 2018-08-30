import os
#json으로 바꾸기 위해 라이브러리 추가
import json
import random
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!'
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
      "type" : "buttons",
      "buttons" : ["메뉴", "로또", "영화", "고양이", "강아지"]
    }
    #딕셔너리는 json으로 바꿔서 리턴 해주기 위한 코드 
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
@app.route('/message', methods =['POST'])
def message():
    
    # content라는 key의 value를 msg에 저장
    msg = request.json['content']
    img_bool = False
    if msg == "메뉴":
        menu = ["A코스", "B코스", "멀캠 20층"]
        return_msg = random.choice(menu)
    elif msg == "로또":
        lotto = random.sample(range(1,46),6)
        return_msg = "행운의 번호 : " + json.dumps(sorted(lotto))
    elif msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_type=jpg"
        req = requests.get(url).json()
        return_msg = "나만 동물 없엉 :("
        img_url= req[0]['url']
    elif msg == "강아지":
        img_bool = True
        url = "https://api.thedogapi.com/v1/images/search?mime_types=jpg"
        req = requests.get(url).json()
        return_msg = "나만 동물 없엉 :("
        img_url= req[0]['url']
    elif msg == "영화":
        img_bool = True
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
                "img" : image_tag[i].get('src')
            }
            
        pick_movie = movie_dic[random.randrange(0,10)]
        return_msg = "%s/평점 : %s/예매율 : %s/" %(pick_movie['title'],pick_movie['star'],pick_movie['reserve'])
        img_url = pick_movie['img']
    else:
        return_msg = "안됩니다."
        
    if img_bool==True:
        json_return = {
            "message" : {
                "text" : return_msg,
                "photo": {
                    "url" : img_url,
                    "width" : 720,
                    "height" : 640
                }
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "영화", "고양이", "강아지"]
            }
        }
    else:    
        json_return = {
            "message" : {
                "text" : return_msg
            },
        "keyboard" : {
            "type" : "buttons",
            "buttons" : ["메뉴", "로또", "영화", "고양이", "강아지"]
        }
    }
    return jsonify(json_return)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    