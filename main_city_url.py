from selenium import webdriver
from selenium.webdriver import ChromeOptions
import csv
import time
url="http://www.tianqihoubao.com/qihou/"
option = ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
with open("main_city_url.csv", "a", encoding='utf-8', newline='') as f:
    csv.writer(f).writerow(["地区","网址"])
main_city_url_list=browser.find_elements_by_css_selector("#content > div.box.p > ul > li")
for main_city_url in main_city_url_list:
    url=main_city_url.find_element_by_css_selector("a").get_attribute("href")
    name=main_city_url.find_element_by_css_selector("a").text
    with open("main_city_url.csv", "a", encoding='utf-8', newline='') as f:
        csv.writer(f).writerow([name,url])