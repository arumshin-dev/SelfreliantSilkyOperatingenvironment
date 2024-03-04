from flask import Flask, render_template

#Flask 객체 생성
app = Flask("JobScrapper")

#decorator 루트 라우팅
@app.route("/")
#function 루트 함수
def home():
  #return "Hello World"
  # return "<h1>hey there!</h1><a href='/hello'>go to hello</a>"
  return render_template("home.html", name="arum")

@app.route("/search")
def search():
  return render_template("search.html")

#ip주소를 0.0.0.0으로 설정해줌 서버실행
app.run("0.0.0.0")