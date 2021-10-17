from selenium import webdriver
from selenium.webdriver import ChromeOptions
import csv
import time
import pandas as pd

####"历史最高气温","历史最低气温"数据有问题，部分不显示，且历史最低气温原数据是错的。
#######################################################################
urllist=pd.read_csv('main_city_url.csv')
i=0
with open("中国气候.csv", "a", encoding='utf-8', newline='') as f:
    csv.writer(f).writerow(["地区","月份","平均最高气温","平均最低气温","平均降雨量","历史最高气温","历史最低气温"])
for url in urllist["网址"]:
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    option = ChromeOptions()
    option.add_argument('--headless')
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    browser.maximize_window()
    contain_list=browser.find_elements_by_css_selector("#bd > div.hd > div.qihou > table > tbody > tr")[1::]
    for contain in contain_list:
        moth=contain.find_element_by_css_selector("td:nth-child(1)").text#月份
        AR_MAX_T=contain.find_element_by_css_selector("td:nth-child(2)").text#平均最高气温
        AR_MIN_T=contain.find_element_by_css_selector("td:nth-child(3)").text#平均最低气温
        AR_rain_fall=contain.find_element_by_css_selector("td:nth-child(4)").text#平均降雨量
        H_MAX_T=contain.find_element_by_css_selector("td:nth-child(5)").text#历史最高气温
        H_MIN_T=contain.find_element_by_css_selector("td:nth-child(6)").text#历史最低气温
        with open("中国气候.csv", "a", encoding='utf-8', newline='') as f:
            csv.writer(f).writerow([urllist["地区"][i],moth,AR_MAX_T,AR_MIN_T,AR_rain_fall,H_MAX_T,H_MIN_T ])
    browser.close()
    print(("第{}个城市既{}".format(i+1,urllist["地区"][i])))
    i=i+1
            # #bd > div.hd > div.qihou > table > tbody > tr:nth-child(4) > td:nth-child(6)
