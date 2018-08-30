import os
#json으로 바꾸기 위해 라이브러리 추가
import json
from flask import Flask, request,jsonify

app=Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!'
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
      "type" : "buttons",
      "buttons" : ["메뉴", "로또", "영화","고양이"]
    }
    #딕셔너리는 json으로 바꿔서 리턴 해주기 위한 코드 
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
    
@app.route('/message', methods =['POST'])
def message():
    
    # content라는 key의 value를 msg에 저장
    msg = request.json['content']
    
    json_return = {
        "message" : {
            "text" : msg
        },
        "keyboard" : {
            "type" : "buttons",
            "buttons" : ["메뉴", "로또", "영화", "고양이"]
        }
    }
    return jsonify(json_return)
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    