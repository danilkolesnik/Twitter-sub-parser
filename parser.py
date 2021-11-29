from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

name = input('Введите имя пользователя Twitter \n')
url = f'https://twitter.com/{name}'


def twitter_collection(url):
    driver.get(url=url)
    time.sleep(3)
    sub = driver.find_element_by_css_selector(
        "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > div:nth-child(1) > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-901oao.css-16my406.r-1fmj7o5.r-poiln3.r-b88u0q.r-bcqeeo.r-qvutc0 > span")
    print("Читатели: ", sub.text)


try:
    twitter_collection(url)
except Exception as Ex:
    print(Ex)
finally:
    driver.close
    driver.quit
