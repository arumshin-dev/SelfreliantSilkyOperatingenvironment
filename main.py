import requests
from bs4 import BeautifulSoup

url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

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
  company = company.text
  position = position.text
  region = region.text
  print(title, company, position, region,"-----\n",)

'''letters = ["a", "b", "c"]
a,b,c = letters
print(a)#a
print(b)#b
print(c)#c
'''

           