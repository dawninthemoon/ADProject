from selenium import webdriver
from bs4 import BeautifulSoup
import time

class CJUtoGMP:

    def __init__(self, month, day):
        driver = webdriver.Chrome('./chromedriver')
        url = f'https://flight.naver.com/flights/domestic/CJU-GMP-2021{month}{day}?adult=1&fareType=YC'
        driver.get(url)

        time.sleep(15)

        numOfDate = 50

        for i in range(numOfDate):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(0.1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        keys = soup.select("b.name")
        index = 0
        self.airline = []
        for key in keys:
            index += 1
            self.airline.append([index, key.text])

        keys2 = soup.select("b.time")

        for i in range(0, len(keys2), 2):
            key = keys2[i]
            self.airline[i // 2].append(key.text)

        keys3 = soup.select("i.domestic_num__2roTW")
        keys3_garbage = soup.select("i.domestic_type__30RSq")

        index = 0;
        for i in range(len(keys3)):
            if (keys3_garbage[i].text == "일반석" or keys3_garbage[i].text == "특가석" or keys3_garbage[i].text == "할인석" or keys3_garbage[i].text == "비즈니스석"):
                key = keys3[i]
                self.airline[index].append(key.text)
                index += 1

    def sortStartTime(self):
        self.airline = sorted(self.airline, key = lambda x:x[0])

    def sortMoneyLowToHigh(self):
        self.airline = sorted(self.airline, key=lambda x:x[3])

    def sortMoneyHightToLow(self):
        self.airline = sorted(self.airline, key=lambda x:x[3], reverse = True)

    def getSize(self):
        return len(self.airline)

    def getAirline(self, index):
        return self.airline[index][1]

    def getAirlineStartTime(self, index):
        return self.airline[index][2]

    def getAirlineCost(self, index):
        return self.airline[index][3]