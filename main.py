from playwright.sync_api import sync_playwright

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
#page.goto("https://mandloh.tistory.com/manage/posts/")
page.goto("https://google.com")

#페이지의 screenshot을 저장합니다.
page.screenshot(path="screenshot.png")

#playwright를 종료합니다.
#playwright.stop()
#play.stop()
