import requests
from bs4 import BeautifulSoup

#url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

all_jobs = []#리스트 생성

#페이징 페이지가 있으므로 스크랩 기능을 함수로 만들어서 사용
def scrape_page(url):
  response = requests.get(url)#페이지 요청

  #print(response.content)#해당 페이지 html 찍음

  soup = BeautifulSoup(response.content, 'html.parser')#html 파싱
  #soup.find("section", id="category-2")
  '''
  a=[1,2,3,4,5,6,7,8,9,10]
  print(a[1])#2
  print(a[0:5])#[1, 2, 3, 4, 5]
  print(a[2:])#[3, 4, 5, 6, 7, 8, 9, 10]
  print(a[1:-1])#[2, 3, 4, 5, 6, 7, 8, 9]
  '''
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]#section class jobs의 li태그를 찾아서 li태그의 1번째부터 마지막까지 찾아서 jobs라는 변수에 저장

  #print(jobs)



  for job in jobs:
    title = job.find("span", class_="title").text#제목
    #region = job.find("span", class_="region").text
    company, position, region = job.find_all("span", class_="company")#회사, 직무, 지역
    # company = company.text
    # position = position.text
    # region = region.text
    # print(title, company, position, region,"-----\n",)
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]#링크
    job_data = {
      'title': title,
      'company': company.text,
      'position': position.text,
      'region': region.text,
      'url':f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)#리스트에 저장


'''
letters = ["a", "b", "c"]
a,b,c = letters #배열 안의 개수 변수 순으로 값 집어넣는다. 개수 같아야함
print(a)#a
print(b)#b
print(c)#c
d,e,_ = letters
print(d)
print(e)
print(_)
'''

#페이징 개수를 가져오는 함수
def get_pages(url):
  response = requests.get(url)#페이지 요청
  soup = BeautifulSoup(response.content, "html.parser",)#html 파싱
  return len(soup.find("div", class_= "pagination").find_all("span",class_="page"))#페이지 개수를 리턴

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")#페이지 개수를 가져오는 함수를 호출

#페이지 개수를 가져와 스크랩 함수에 개수를 넣어 반복 호출
for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"#페이지를 가져오는 url
  scrape_page(url)#페이지를 스크랩하는 함수를 호출


print(len(all_jobs))#모든 정보를 가져왔으므로 개수를 출력