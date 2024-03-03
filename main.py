from flask import Flask

#Flask 객체 생성
app = Flask("JobScrapper")

#decorator 루트 라우팅
@app.route("/")
#function 루트 함수
def home():
  #return "Hello World"
  return "hey there!"

#ip주소를 0.0.0.0으로 설정해줌 서버실행
app.run("0.0.0.0")