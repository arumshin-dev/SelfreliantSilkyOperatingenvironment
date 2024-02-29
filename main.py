from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

#동기화 방식으로 사용을 시작합니다.
play = sync_playwright().start()

#브라우저가 보이도록 headless옵션을 끄고, 엣지브라우저를 사용합니다.
# browser = playwright.chromium.launch(headless=False, channel="msedge")
# context = browser.new_context()
browser = play.chromium.launch(headless=False)
# browser = play.firefox.launch()

#브라우저로 웹페이지를 실행합니다
# page = context.new_page()
page = browser.new_page()

#아래 주소로 이동합니다.
page.goto("https://www.wanted.co.kr/")

#페이지의 screenshot을 저장합니다.
#page.screenshot(path="screenshot.png")

time.sleep(3)  #3초 기다림

page.click("button.Aside_searchButton__Xhqq3")  #버튼 클래스 선택 클릭
#page.locator("button.Aside_searchButton__Xhqq3").click()#버튼 클릭 동일

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(3)

page.keyboard.down("Enter")  #엔터키를 누른다

time.sleep(5)

page.click("a#search_tab_position")

for x in range(5):
  time.sleep(5)

  page.keyboard.down("End")

time.sleep(5)

content = page.content()

#playwright를 종료합니다.
play.stop()  #메모리 누수 방지 위하여 꺼주기

soup = BeautifulSoup(content, "html.parser")
