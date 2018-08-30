import os
import json
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!'
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
      "type" : "buttons",
      "buttons" : ["메뉴", "로또", "영화","고양이","영화"]
    }
    #딕셔너리는 json으로 바꿔서 
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    