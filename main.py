from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
month = 11
day = 30
url = f'https://flight.naver.com/flights/domestic/GMP-CJU-202111{day}/CJU-GMP-202111{day+1}?adult=1&isDirect=true&fareType=YC'
driver.get(url)

time.sleep(15)

numOfData = 50

#driver.find_element_by_class_name("inlineFilter_Tag__97qqq").click()

tempTime = "밤"
timeClassNameDic = {"오후":"time as_1qt", "밤":"time as_3qt"}

#driver.find_element_by_class_name(timeClassNameDic[tempTime]).click()

for i in range(numOfData):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(0.1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
keys = soup.select("b.name")
index = 0
airline = []
for key in keys:
    index += 1
    airline.append([index, key.text])
    #print(key)

keys2 = soup.select("b.time")

print(len(keys), len(keys2))
for i in range(0, len(keys2), 2):
    key = keys2[i]
    airline[i // 2].append(key.text)

keys3 = soup.select("i.domestic_num__2roTW")
print(len(keys3))

for i in range(0, len(keys3), 2):
    key = keys3[i]
    airline[i // 2].append(key.text)
print(airline)

