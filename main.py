from flask import Flask, render_template, request, redirect, send_file
# from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

#Flask 객체 생성
app = Flask("JobScrapper")

#cache 저장 fake db
db = {}

#decorator 루트 라우팅
@app.route("/")
#function 루트 함수
def home():
  #return "Hello World"
  # return "<h1>hey there!</h1><a href='/hello'>go to hello</a>"
  return render_template("home.html", name="arum")

@app.route("/search")
def search():
  # print(request.args)
  print(db)
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    print("이미 검색한거")
    jobs = db[keyword]
  else:
    print("처음 검색")
    # indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    # jobs = indeed + wwr
    jobs = wwr
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    print("검색어 없음")
    return redirect("/")
  if keyword not in db:
    print("처음 검색")
    return redirect(f"/search?keyword={keyword}")
  else:
    print("검색 했던거 저장해")

  save_to_file(keyword, db[keyword])#파일 저장
  return send_file(f"{keyword}.csv", as_attachment=True)

#ip주소를 0.0.0.0으로 설정해줌 서버실행
app.run("0.0.0.0")