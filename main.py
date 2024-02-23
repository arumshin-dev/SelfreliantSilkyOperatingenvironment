import requests
from bs4 import BeautifulSoup

url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

response = requests.get(url)

#print(response.content)#해당 페이지 html 찍음

soup = BeautifulSoup(response.content, 'html.parser')
jobs = soup.find("section", class_="jobs").find_all("li")
#soup.find("section", id="category-2")

print(jobs)