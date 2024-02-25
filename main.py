import requests
from bs4 import BeautifulSoup

#url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

all_jobs = []#리스트 생성

def scrape_page(url):
  response = requests.get(url)

  #print(response.content)#해당 페이지 html 찍음

  soup = BeautifulSoup(response.content, 'html.parser')
  #soup.find("section", id="category-2")
  '''
  a=[1,2,3,4,5,6,7,8,9,10]
  print(a[1])#2
  print(a[0:5])#[1, 2, 3, 4, 5]
  print(a[2:])#[3, 4, 5, 6, 7, 8, 9, 10]
  print(a[1:-1])#[2, 3, 4, 5, 6, 7, 8, 9]
  '''
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  #print(jobs)



  for job in jobs:
    title = job.find("span", class_="title").text
    #region = job.find("span", class_="region").text
    company, position, region = job.find_all("span", class_="company")
    # company = company.text
    # position = position.text
    # region = region.text
    # print(title, company, position, region,"-----\n",)
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
    job_data = {
      'title': title,
      'company': company.text,
      'position': position.text,
      'region': region.text,
      'url':f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)


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
def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser",)
  return len(soup.find("div", class_= "pagination").find_all("span",class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)


print(len(all_jobs))