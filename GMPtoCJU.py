from selenium import webdriver
from bs4 import BeautifulSoup
import time

class GMPtoCJU:

    def __init__(self,year, month, day, place):
        driver = webdriver.Chrome('./chromedriver')
        url = f'https://flight.naver.com/flights/domestic/{place}-{year}{month}{day}?adult=1&fareType=YC'
        driver.get(url)

        time.sleep(15)

        numOfDate = 50

        for i in range(numOfDate):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(0.1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.keys = soup.select("b.name")
        index = 0
        self.airline = []
        for key in self.keys:
            index += 1
            self.airline.append([index, key.text])
            # print(key)

        self.keys2 = soup.select("b.time")

        # print(len(self.keys), len(self.keys2))
        for i in range(0, len(self.keys2), 2):
            key = self.keys2[i]
            self.airline[i // 2].append(key.text)

        self.keys3 = soup.select("i.domestic_num__2roTW")
        keys3_garbage = soup.select("i.domestic_type__30RSq")
        # print(len(self.keys3))
        # print(keys3_garbage)
        index = 0
        for i in range(len(self.keys3)):
            if (keys3_garbage[i].text == "일반석" or keys3_garbage[i].text == "특가석" or keys3_garbage[i].text == "할인석" or keys3_garbage[i].text == "비즈니스석" or keys3_garbage[i].text == "특가석-환불불가" or keys3_garbage[i].text == "특가석-수하물유료"):
                key = self.keys3[i]
                money = key.text.replace(',', '')
                self.airline[index].append(int(money))
                index += 1

    def sortStartTime(self):
        self.airline = sorted(self.airline, key = lambda x:x[0])

    def sortMoneyLowToHigh(self):
        self.airline = sorted(self.airline, key=lambda x:x[3])
        #print(self.airline)

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
